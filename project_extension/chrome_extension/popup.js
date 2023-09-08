document.getElementById("taskForm").addEventListener("submit", function(e) {
    e.preventDefault();
    let task = document.getElementById("task").value;
    chrome.storage.sync.get(["apiKey"], function(result) {
        if (!result.apiKey) {
            // Handle the failure when apiKey is not defined
            console.error("API key is not defined. Request failed.");
            return;
        }

        // Create a script element for elements.js
        let elementsScript = document.createElement("script");
        elementsScript.src = "scripts/elements.js";
        elementsScript.onload = function() {
            // Create a script element for window.js
            let windowScript = document.createElement("script");
            windowScript.src = "scripts/window.js";
            windowScript.onload = function() {
                // Call the elements and windowFunction
                let element = elements(task);
                let windowData = windowFunction(task);

                // Send the message after everything is loaded and executed
                chrome.runtime.sendMessage({ task: task, api_key: result.apiKey, element: element, window_data: windowData });
            };

            document.head.appendChild(windowScript);
        };

        document.head.appendChild(elementsScript);
    });
});

chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    fetch("http://localhost:3000/data",
    {
        method: "POST",
        headers: {"Content-Type": "application/json",},
        body: JSON.stringify(request),
    })
        .then(response => response.json()).
            then(data => {
                chrome.tabs.query({active: true, currentWindow: true}, 
                function(tabs) {
                    chrome.tabs.sendMessage(tabs[0].id, {coordinates: data});
            });
}).catch((error) => {console.error("Error:", error);
    });
});

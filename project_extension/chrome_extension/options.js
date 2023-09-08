document.getElementById("optionsForm").addEventListener("submit", function(e) {
    e.preventDefault();
    let apiKey = document.getElementById("apiKey").value;
    chrome.storage.sync.set({apiKey: apiKey}, function() {
        console.log("API key saved");
    });
});

chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    let box = document.createElement("div");
    box.style.width = "100px";
    box.style.height = "100px";
    box.style.background = "red";
    box.style.position = "absolute";
    box.style.left = request.coordinates.left + "px";
    box.style.top = request.coordinates.top + "px";
    document.body.appendChild(box);
});

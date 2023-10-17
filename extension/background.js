chrome.action.onClicked.addListener((tab) => {
  chrome.windows.create({
    url: chrome.runtime.getURL(`main.html`),
    width: 600,
    height: 600,
    type: "popup",
  });
});
chrome.runtime.onInstalled.addListener((tab) => {
  console.log("installed")
});
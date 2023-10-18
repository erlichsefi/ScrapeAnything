const getCurrentTab = async () => {
  try {
      let [tab] = await chrome.tabs.query({
        active: true,
        currentWindow: false,
      });
    return tab;
  } catch (e) {
    console.error(e);
    return null;
  }
};


document.addEventListener("DOMContentLoaded", function () {
  console.log('DOMContentLoaded event dispatched');
  const form = document.getElementById("objective-form");
  const objectiveInput = document.getElementById("objective");
  const submitButton = document.getElementById("submit");
  const active = document.getElementById("switch");
  const errorEl = document.getElementById("error");


  form.addEventListener("submit", async (e) => {
    console.log('submit event dispatched');
    e.preventDefault();
    submitButton.setAttribute("disabled", true);
    
    const currentTab = await getCurrentTab();
    console.log('currentTab='+currentTab)

    if (!currentTab) {
      errorEl.innerHTML =
        "BrowseGPT extension could not access a tab. Try closing and re-launching the extension.";
      return;
    }

    const tabId = currentTab.id;
    const objective = objectiveInput.value;
    let body = undefined;

    try{
        const elements = await chrome.tabs.sendMessage(tabId, {
          message: "extract",
          script: "elements",
        });
        

        const url = await chrome.tabs.sendMessage(tabId, {
          message: "extract",
          script: "get_url",
        });

        const {viewpointscroll,viewportHeight} = await chrome.tabs.sendMessage(tabId, {
          message: "extract",
          script: "window",
        });

        const scroll_width = await chrome.tabs.sendMessage(tabId, {
          message: "extract",
          script: "scroll_width",
        });

        const scroll_height = await chrome.tabs.sendMessage(tabId, {
          message: "extract",
          script: "scroll_height",
        });

        const {width,height} = await chrome.tabs.sendMessage(tabId, {
          message: "extract",
          script: "get_window_size",
        });

        console.log("sending request to the server.")
        body = JSON.stringify({
          "viewpointscroll":viewpointscroll,
          "viewportHeight":viewportHeight,
          "scroll_width":scroll_width,
          "scroll_height":scroll_height,
          "width":width,
          "height":height,
          "raw_on_screen":elements,
          "url":url,
          "user_task":objective,
          "session_id":tabId,
        });
      } catch (e) {
          console.log(e.message)
          errorEl.innerText = `Extracting failed, Error: ${e.message}.`;
      }


    if (body != undefined){
      let command = {}
      try{
          const res = await fetch("http://localhost:3000/process", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body,
          });
          command = await res.json();
          //command = JSON.parse(commandResponse);
        } catch (e) {
          command = {"example_script":"show_text",'tool_input':{"text":"server is down"}}
        }
      
        chrome.tabs.sendMessage(tabId, {
          message: "run_command",
          active: active == true,
          script: command.example_script,
          args: command.tool_input, 
        });
    }
    
    submitButton.removeAttribute("disabled");
    
  });

});

module.exports = {getCurrentTab};
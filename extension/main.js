document.addEventListener("DOMContentLoaded", function () {

  const form = document.getElementById("objective-form");
  const objectiveInput = document.getElementById("objective");
  const submitButton = document.getElementById("submit");
  const errorEl = document.getElementById("error");

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


  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    submitButton.setAttribute("disabled", true);
    
    const currentTab = await getCurrentTab();

    if (!currentTab) {
      errorEl.innerHTML =
        "BrowseGPT extension could not access a tab. Try closing and re-launching the extension.";
      return;
    }

    const tabId = currentTab.id;
    
    let commandResponse = {};
    const objective =  objectiveInput.value;

    try {
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

      const {scroll_width} = await chrome.tabs.sendMessage(tabId, {
        message: "extract",
        script: "scroll_width",
      })

      const {scroll_height} = await chrome.tabs.sendMessage(tabId, {
        message: "extract",
        script: "scroll_height",
      })

      const {width,height} = await chrome.tabs.sendMessage(tabId, {
        message: "extract",
        script: "get_window_size",
      })
      
      console.log(elements)
      const body = JSON.stringify({
        viewpointscroll:viewpointscroll,
        viewportHeight:viewportHeight,
        scroll_width:scroll_width,
        scroll_height:scroll_height,
        width:width,
        height:height,
        raw_on_screen:elements,
        url: url,
        user_task:objective,
        session_id:tabId,
      });

      const res = await fetch("http://localhost:3000/process", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body,
      });


      commandResponse = await res.json();
      const command = JSON.parse(commandResponse);
    
      // command.example_script 
      // command.description 
      // command.tool_enum
      // command.tool_input 
    
      chrome.tabs.sendMessage(tabId, {
        message: "run_command",
        script: command.example_script,
        args:command.tool_input, 
      });
    } catch (e) {
      if (e.message.includes("Could not establish connection")) {
        errorEl.innerText =
          "This page doesn't allow the BrowseGPT extension. Close the extension, go to a different URL like https://google.com, and then re-launch the extension from there."+e.message;
      } else {
        errorEl.innerText = `Command: ${JSON.stringify(
          commandResponse || ""
        )}\n Error: ${e.message}. Try closing and re-launching the extension.`;
      }
    } finally {
      submitButton.removeAttribute("disabled");
    }
  });

});

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
    console.log('currentTab='+currentTab)

    if (!currentTab) {
      errorEl.innerHTML =
        "BrowseGPT extension could not access a tab. Try closing and re-launching the extension.";
      return;
    }

    const tabId = currentTab.id;
    
    let commandResponse = {};
    const objective =  objectiveInput.value;
    let call_server = true;


    try{
        const elements = await chrome.tabs.sendMessage(tabId, {
          message: "extract",
          script: "elements",
        });
        console.log("got elements "+elements)

        const url = await chrome.tabs.sendMessage(tabId, {
          message: "extract",
          script: "get_url",
        });
        console.log("got url "+url)

        const {viewpointscroll,viewportHeight} = await chrome.tabs.sendMessage(tabId, {
          message: "extract",
          script: "window",
        });
        console.log("got viewpointscroll "+viewpointscroll)
        console.log("got viewportHeight "+viewportHeight)

        const scroll_width = await chrome.tabs.sendMessage(tabId, {
          message: "extract",
          script: "scroll_width",
        });
        console.log("got scroll_width "+scroll_width)

        const scroll_height = await chrome.tabs.sendMessage(tabId, {
          message: "extract",
          script: "scroll_height",
        });
        console.log("got scroll_height "+scroll_height)

        const {width,height} = await chrome.tabs.sendMessage(tabId, {
          message: "extract",
          script: "get_window_size",
        });
        console.log("got width "+width)
        console.log("got height "+height)

        console.log("sending request to the server.")
        const body = JSON.stringify({
          viewpointscroll:viewpointscroll,
          viewportHeight:viewportHeight,
          scroll_width:scroll_width,
          scroll_height:scroll_height,
          width:width,
          height:height,
          raw_on_screen:elements,
          url:url,
          user_task:objective,
          session_id:tabId,
        });
      } catch (e) {
          console.log(e.message)
          errorEl.innerText = `Extracting failed, Error: ${e.message}.`;
          call_server = false
      }


    if (call_server){
      let command = {}
      try{
          const res = await fetch("http://localhost:3000/process", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body,
          });
          commandResponse = await res.json();
          command = JSON.parse(commandResponse);
        } catch (e) {
          command = {"example_script":"show_text",'tool_input':{"text":"server is down"}}
        }

        // command.example_script 
        // command.description 
        // command.tool_enum
        // command.tool_input 
      
        chrome.tabs.sendMessage(tabId, {
          message: "run_command",
          script: command.example_script,
          args: command.tool_input, 
        });
    }
    
    submitButton.removeAttribute("disabled");
    
  });

});

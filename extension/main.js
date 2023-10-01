const form = document.getElementById("objective-form");
const objectiveInput = document.getElementById("objective");
const submitButton = document.getElementById("submit");
const errorEl = document.getElementById("error");

/** @type Command[] */
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


// debugGetBrowserContent.addEventListener("click", async (e) => {
//   const currentTab = await getCurrentTab();
//   const tabId = currentTab.id;
//   /** @type BrowserContent */
//   const browserContent = await chrome.tabs.sendMessage(tabId, {
//     message: "get_browser_content",
//   });
//   const { html } = browserContent;
//   pre.innerText = html;
// });

// debugForm.addEventListener("submit", async (e) => {
//   e.preventDefault();
//   const currentTab = await getCurrentTab();
//   const tabId = currentTab.id;
//   chrome.tabs.sendMessage(tabId, {
//     message: "run_command",
//     command: JSON.stringify({
//       action: debugAction.value,
//       value: debugValue.value,
//       id: debugId.value,
//     }),
//   });
// });

// clearHistoryEl.addEventListener("click", async () => {
//   commandHistory.splice(0, commandHistory.length);
//   renderHistory();
//   pre.innerHTML = "";
//   errorEl.innerHTML = "";
//   const currentTab = await getCurrentTab();
//   chrome.tabs.sendMessage(currentTab.id, {
//     message: "clear_history",
//   });
// });

objectiveInput.addEventListener("keydown", (e) => {
  if (e.which === 13 && !e.shiftKey) {
    if (!e.repeat) {
      const newEvent = new Event("submit", { cancelable: true });
      e.target.form.dispatchEvent(newEvent);
    }
    e.preventDefault();
  }
});

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
      message: "elements",
    });

    const url = await chrome.tabs.sendMessage(tabId, {
      message: "get_url",
    });

    const {viewpointscroll,viewportHeight} = await chrome.tabs.sendMessage(tabId, {
      message: "window",
    });

    const {scroll_width} = await chrome.tabs.sendMessage(tabId, {
      message: "scroll_width",
    })

    const {scroll_height} = await chrome.tabs.sendMessage(tabId, {
      message: "scroll_height",
    })

    const {width,height} = await chrome.tabs.sendMessage(tabId, {
      message: "get_window_size",
    })
    
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
        "This page doesn't allow the BrowseGPT extension. Close the extension, go to a different URL like https://google.com, and then re-launch the extension from there.";
    } else {
      errorEl.innerText = `Command: ${JSON.stringify(
        commandResponse || ""
      )}\n Error: ${e.message}. Try closing and re-launching the extension.`;
    }
  } finally {
    loadingEl.classList.add("hidden");
    submitButton.removeAttribute("disabled");
  }
});

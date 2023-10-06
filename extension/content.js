import {call_action,call_extract} from './shared/entry.js'

export function main() {

  chrome.runtime.onMessage.addListener((req, sender, sendResponse) => {
    if (req.message === "run_command") {

      //  offer a action
      console.log("Running command script: "+req.script+" with args: "+req.args);
      var response = call_action(req.script,req.args);
      console.log("Response from script"+req.script+" is: "+response);
      sendResponse({
       response
      });
    
    } else if (req.message === "extract") {

      // get information about the screen
      console.log("Running extraction script: "+req.script+" with args: "+req.args);
      call_extract(req.script).then(response => {
          console.log("Response from script " + req.script + " is: " + response);
          sendResponse(response);
          console.log("sent")
        });
    }
    else {
      throw new Error('message '+req.message+" is not defined.");

    }
  });
}

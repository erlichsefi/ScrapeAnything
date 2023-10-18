import {call_act,call_extract,call_guide} from './shared/entry.js'

export function main() {

  chrome.runtime.onMessage.addListener((req, sender, sendResponse) => {
    if (req.message === "run_command") {
      var execute_function = call_guide
      if (req.active == true ){
        var execute_function = call_act
      }
      //  present the user a guidance 
      console.log("Running command script: "+req.script+" with args: "+req.args);
      var response = execute_function(req.script,req.args);
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

import call_action from './shared/index.js'
import call_extract from './shared/index.js'

chrome.runtime.onMessage.addListener((req, sender, res) => {
  if (req.message === "run_command") {
    
    //  offer a action
    console.debug("Running"+req.script+" "+req.args);
    var response = call_action(req.script,req.args);
    console.debug("Res:"+response);
    res({
      response:response
    });
  
  } else if (req.message === "extract") {

    // get information about the screen
    console.debug("Running"+req.script+" "+req.args);
    var response = call_extract(req.script,req.args);
    console.debug("Res:"+response);
    res({
      response:response
    });
  }
  else {
    throw new Error('message '+req.message+" is not defined.");

  }
});
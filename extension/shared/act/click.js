function click_coordinates(x,y){
    var element = document.elementFromPoint(x, y);
    // Click on the element
    element.click();
};

 function click_coordinates_and_text(x,y,text){
    var element = document.elementFromPoint(x, y);

    // Click on the element
    element.click();
    
    // Enter text into the input field
    element.value = text; // Assuming element is an input field
};



function keyborad_action(text){
    if (text.toLowerCase() === "esc") {
        // For "esc" key press
        var event = new KeyboardEvent("keydown", {
            key: "Escape",
        });
        document.dispatchEvent(event);
    } else if (text.toLowerCase() === "enter") {
        // For "enter" key press
        var event = new KeyboardEvent("keydown", {
            key: "Enter",
        });
        document.dispatchEvent(event);
    }
}

module.exports = {click_coordinates,click_coordinates_and_text,keyborad_action};
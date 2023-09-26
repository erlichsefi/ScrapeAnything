function draw_arrow(x,y,text){
    // Create the arrow element
    var arrowElement = document.createElement("div");
    arrowElement.style.position = "absolute";
    arrowElement.style.left = x + "px";
    arrowElement.style.top = y + "px";
    arrowElement.style.width = "0";
    arrowElement.style.height = "0";
    arrowElement.style.pointerEvents = "none";
    arrowElement.style.zIndex = 2147483647;

    // Create an arrow pointing up with CSS borders
    arrowElement.style.borderLeft = "20px solid transparent";
    arrowElement.style.borderRight = "20px solid transparent";
    arrowElement.style.borderBottom = "40px solid red";  // Adjust the color and dimensions as needed

    document.body.appendChild(arrowElement);

    if (text) {
        // Create the text element
        var textElement = document.createElement("div");
        textElement.style.position = "absolute";
        textElement.style.left = x - 20 + "px"; // Adjust the horizontal position for centering
        textElement.style.top = (y + 40) + "px"; // Adjust the vertical position for centering
        textElement.textContent = text; // Replace with your desired text
        textElement.style.textAlign = "center"; // Center the text horizontally
        textElement.style.zIndex = 2147483647;

        document.body.appendChild(textElement);
    }
}

draw_arrow({x},{y},{text})
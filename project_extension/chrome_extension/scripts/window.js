function windowFunction() {
const viewpointscroll = window.pageYOffset || document.documentElement.scrollTop;
const viewportHeight = window.innerheight || document.documentElement.clientHeight;
// Create a formatted string containing the values
const formattedValues = `viewpointscroll:${viewpointscroll}, viewportHeight:${viewportHeight}`;

// Return the formatted string
return formattedValues;
}
// Create the scroll indicator container element
const indicatorContainer = document.createElement('div');
indicatorContainer.style.position = 'fixed';
indicatorContainer.style.left = '20px'; // Change 'top' to 'left'
indicatorContainer.style.top = '50%'; // Add this line to vertically center the indicator
indicatorContainer.style.transform = 'translateY(-50%)'; // Vertically center the indicator
indicatorContainer.style.textAlign = 'center';
indicatorContainer.style.zIndex = '1000';

// Create the arrow element for scrolling left
const arrow = document.createElement('div');
arrow.style.width = '30px';
arrow.style.height = '30px';
arrow.style.border = 'solid #fff';
arrow.style.borderWidth = '0 3px 3px 0';
arrow.style.transform = 'rotate(135deg)'; // Rotate the arrow to the left
arrow.style.display = 'inline-block';
arrow.style.marginRight = '10px'; // Adjust the margin to separate the text

// Create the text element
const text = document.createElement('p');
text.style.color = '#fff';
text.style.fontSize = '16px';
text.textContent = 'Scroll Left';

// Add the indicator elements to the container
indicatorContainer.appendChild(arrow);
indicatorContainer.appendChild(text);

// Add the indicator to the document body
document.body.appendChild(indicatorContainer);

// Function to remove the indicator after a certain delay (e.g., 3 seconds)
function removeIndicator() {
    indicatorContainer.style.display = 'none';
}

// Set a timeout to remove the indicator
setTimeout(removeIndicator, 3000); // Adjust the delay as needed

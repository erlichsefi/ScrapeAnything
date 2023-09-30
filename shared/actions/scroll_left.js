const oneSixthOfViewportHeight = (window.innerHeight / 6) + 'px';

// Create the scroll indicator container element
const indicatorContainer = document.createElement('div');
indicatorContainer.style.position = 'fixed';
indicatorContainer.style.left = '20px'; // Position on the left side
indicatorContainer.style.top = '50%'; // Vertically center the indicator
indicatorContainer.style.transform = 'translateY(-50%)'; // Vertically center the indicator
indicatorContainer.style.textAlign = 'center';
indicatorContainer.style.zIndex = 2147483647;

// Create the arrow element for scrolling left
const arrow = document.createElement('div');
arrow.style.width = oneSixthOfViewportHeight; // 1/6 of the screen height
arrow.style.height = oneSixthOfViewportHeight; // 1/6 of the screen height
arrow.style.border = 'solid #666666';
arrow.style.borderWidth = '0 ' + oneSixthOfViewportHeight + ' ' + oneSixthOfViewportHeight + ' 0'; // 1/6 of the screen height
arrow.style.transform = 'rotate(135deg)'; // Rotate the arrow to the left
arrow.style.display = 'inline-block';
arrow.style.marginRight = '10px'; // Adjust the margin to separate the text

// Create the text element
const text = document.createElement('p');
text.style.color = '#666666';
text.style.fontSize = oneSixthOfViewportHeight; // 1/6 of the screen height
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
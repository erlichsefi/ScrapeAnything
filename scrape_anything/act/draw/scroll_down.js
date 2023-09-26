// Create the scroll indicator container element
const indicatorContainer = document.createElement('div');
indicatorContainer.style.position = 'fixed';
indicatorContainer.style.bottom = '20px';
indicatorContainer.style.left = '50%';
indicatorContainer.style.transform = 'translateX(-50%)';
indicatorContainer.style.textAlign = 'center';
indicatorContainer.style.zIndex = '1000';

// Create the arrow element
const arrow = document.createElement('div');
arrow.style.width = '30px';
arrow.style.height = '30px';
arrow.style.border = 'solid #fff';
arrow.style.borderWidth = '0 3px 3px 0';
arrow.style.transform = 'rotate(45deg)';
arrow.style.display = 'inline-block';
arrow.style.marginBottom = '10px';

// Create the text element
const text = document.createElement('p');
text.style.color = '#fff';
text.style.fontSize = '16px';
text.textContent = 'Scroll Down';

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

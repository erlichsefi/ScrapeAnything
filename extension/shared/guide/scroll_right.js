export default  function point_scroll_right(){
    // Calculate the size for arrow and text
    const oneSixthOfViewportHeight = (window.innerHeight / 6) + 'px';

    // Create the scroll indicator container element
    const indicatorContainer = document.createElement('div');
    indicatorContainer.style.position = 'fixed';
    indicatorContainer.style.top = 3*(window.innerHeight / 6) + 'px'; // Position at 1/6 of the viewport height
    indicatorContainer.style.right = (window.innerHeight / 6) +'px'; // Position on the right side
    indicatorContainer.style.transform = 'translateY(-50%)';
    indicatorContainer.style.textAlign = 'center';
    indicatorContainer.style.zIndex = 2147483647;

    // Create the arrow element for scrolling right
    const arrow = document.createElement('div');
    arrow.style.width = oneSixthOfViewportHeight; // 1/6 of the screen height
    arrow.style.height = oneSixthOfViewportHeight; // 1/6 of the screen height
    arrow.style.border = 'solid #666666';
    arrow.style.borderWidth = '0 ' + oneSixthOfViewportHeight + ' ' + oneSixthOfViewportHeight + ' 0'; // 1/6 of the screen height
    arrow.style.transform = 'rotate(-50deg)'; // Rotate to point right
    arrow.style.display = 'inline-block';
    arrow.style.marginLeft = '10px'; // Adjust margin for spacing

    // Create the text element
    const text = document.createElement('p');
    text.style.color = '#666666';
    text.style.fontSize = oneSixthOfViewportHeight; // 1/6 of the screen height
    text.textContent = 'Scroll Right';

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
};
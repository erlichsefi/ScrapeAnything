const refreshContainer = document.createElement('div');
refreshContainer.style.position = 'fixed';
refreshContainer.style.top = '0';
refreshContainer.style.left = '0';
refreshContainer.style.width = '100%';
refreshContainer.style.height = '100%';
refreshContainer.style.backgroundColor = 'rgba(0, 0, 0, 0.5)';
refreshContainer.style.zIndex = '9999';

// Create the refreshing text element
const refreshingText = document.createElement('div');
refreshingText.style.color = '#fff';
refreshingText.style.fontSize = '24px';
refreshingText.textContent = '{text}'; // for the python format 
refreshingText.style.position = 'absolute';
refreshingText.style.top = '50%';
refreshingText.style.left = '50%';
refreshingText.style.transform = 'translate(-50%, -50%)';

// Add the elements to the container
refreshContainer.appendChild(refreshingText);

// Add the container to the document body
document.body.appendChild(refreshContainer);

// Function to show the refresh animation
function showRefreshAnimation() {
    refreshContainer.style.display = 'block';

    // Set a timeout to hide the refresh container after 3 seconds
    setTimeout(function () {
        refreshContainer.style.display = 'none';
    }, 3000);
}

// Attach the showRefreshAnimation function to the beforeunload event
setTimeout(showRefreshAnimation, 3000);

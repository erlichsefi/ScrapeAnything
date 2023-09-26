function getScrollHeightInfo() {
  const initialScrollPosition = window.pageYOffset;

  // Scroll down a bit
  window.scrollBy(0, 100);

  // Wait for a brief moment
  setTimeout(function() {
    const scrollDownPosition = window.pageYOffset;

    // Scroll back to the initial position
    window.scrollTo(0, initialScrollPosition);

    // Wait for a brief moment
    setTimeout(function() {
      // Scroll up a bit
      window.scrollBy(0, -100);

      // Wait for a brief moment
      setTimeout(function() {
        const scrollUpPosition = window.pageYOffset;

        // Scroll back to the initial position
        window.scrollTo(0, initialScrollPosition);

        // Compare the scroll positions
        if (scrollDownPosition > initialScrollPosition && scrollUpPosition < initialScrollPosition) {
          console.log("Client can scroll both up and down!");
        } else if (scrollDownPosition > initialScrollPosition) {
          console.log("Client can scroll down!");
        } else if (scrollUpPosition < initialScrollPosition) {
          console.log("Client can scroll up!");
        } else {
          console.log("Client cannot scroll either up or down!");
        }
      }, 1000); // Wait for a brief moment
    }, 1000); // Wait for a brief moment
  }, 1000); // Wait for a brief moment
}

getScrollHeightInfo();
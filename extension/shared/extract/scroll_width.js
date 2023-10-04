function getScrolWidthInfo() {
    const initialScrollPosition = window.pageXOffset;
  
    // Scroll right a bit
    window.scrollBy(100, 0);
  
    // Wait for a brief moment
    setTimeout(function() {
      const scrollRightPosition = window.pageXOffset;
  
      // Scroll back to the initial position
      window.scrollTo(initialScrollPosition, 0);
  
      // Wait for a brief moment
      setTimeout(function() {
        // Scroll left a bit
        window.scrollBy(-100, 0);
  
        // Wait for a brief moment
        setTimeout(function() {
          const scrollLeftPosition = window.pageXOffset;
  
          // Scroll back to the initial position
          window.scrollTo(initialScrollPosition, 0);
  
          // Compare the scroll positions
          if (scrollRightPosition > initialScrollPosition && scrollLeftPosition < initialScrollPosition) {
            console.log("Client can scroll both left and right!");
          } else if (scrollRightPosition > initialScrollPosition) {
            console.log("Client can scroll right!");
          } else if (scrollLeftPosition < initialScrollPosition) {
            console.log("Client can scroll left!");
          } else {
            console.log("Client cannot scroll either left or right!");
          }
        }, 1000); // Wait for a brief moment
      }, 1000); // Wait for a brief moment
    }, 1000); // Wait for a brief moment
  }
  
console.log(getScrollInfo());
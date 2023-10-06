export default function getScrolWidthInfo() {
  return new Promise((resolve, reject) => {
    const initialScrollPosition = window.pageXOffset;
    let res = ""
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
            res = "Client can scroll both left and right!";
          } else if (scrollRightPosition > initialScrollPosition) {
            res = "Client can scroll right!";
          } else if (scrollLeftPosition < initialScrollPosition) {
            res = "Client can scroll left!";
          } else {
            res = "Client cannot scroll either left or right!";
          }
          resolve(res);
        }, 1000); // Wait for a brief moment
      }, 1000); // Wait for a brief moment
    }, 1000); // Wait for a brief moment
  });
}
  
// console.log(getScrollInfo());
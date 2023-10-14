// setup mocks
require('fetch-mock').post('http://localhost:3000/process', {
    "body": JSON.stringify({
    "example_script": "show_text",
    "tool_input": {
      "text": "server is down",
    },
  }),
})
require('../main.js'); // Import the functions you want to test


describe('Form Event Listener', () => {
  let form;
  let submitButton;
  let errorEl;

  beforeEach(() => {
    
    // Set up a fake DOM environment for testing
    document.body.innerHTML = `
      <form id="objective-form">
        <input id="objective" type="text">
        <button id="submit">Submit</button>
      </form>
      <div id="error"></div>
    `;

    form = document.getElementById('objective-form');
    submitButton = document.getElementById('submit');
    errorEl = document.getElementById('error');

    const event = new Event('DOMContentLoaded');
    document.dispatchEvent(event);  

    let mockExtract = jest.fn().mockResolvedValue({})
    let mockCommand = jest.fn().mockResolvedValue({})
    let sendMessageMock = jest.fn().mockImplementation((tabId, message) => {
      if (message.message === 'extract') {
        return mockExtract();
      } else if (message.message === 'run_command') {
        return mockCommand();
      }
      throw Error("!")
    })
    global.chrome = {
        tabs: {
          query: jest.fn().mockResolvedValue([{ id: 456 }]),
          sendMessage:sendMessageMock
        },
      };
      
  });



  it('should handle form submission and call getCurrentTab', async () => {

    // Simulate form submission
    const event = new Event('submit', { bubbles: true, cancelable: true });
    form.dispatchEvent(event);

    // Test that getCurrentTab was called and form elements were updated
    expect(submitButton.getAttribute('disabled')).toBe('true');
    expect(errorEl.innerHTML).toBe('');
    expect(sendMessageMock).toHaveBeenCalled();

  });

});

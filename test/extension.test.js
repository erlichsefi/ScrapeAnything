// setup mocks
const fetchMock = require('fetch-mock');
const mockExtract = jest.fn().mockResolvedValue({});  // Declare mockExtract in a broader scope
const mockCommand = jest.fn().mockResolvedValue({});
const sendMessageMock = jest.fn().mockImplementation((tabId, message) => {
  if (message.message === 'extract') {
    return mockExtract();
  } else if (message.message === 'run_command') {
    return mockCommand();
  }
  throw Error("!")
});

fetchMock.post('http://localhost:3000/process', {
  "body": JSON.stringify({
    "example_script": "show_text",
    "tool_input": {
      "text": "server is down",
    },
  }),
});

require('../extension/main.js'); // Import the functions you want to test

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

    global.chrome = {
      tabs: {
        query: jest.fn().mockImplementation((tabId, message) => [{ id: 456 }]),
        sendMessage: sendMessageMock,
      },
    };
  });

  it('should handle form submission and call getCurrentTab', async () => {
    // Simulate form submission
    const event = new Event('submit', { bubbles: true, cancelable: true });
    form.dispatchEvent(event);
    // wait the function will finish.
    await new Promise((resolve) => setTimeout(resolve, 0));

    // Make Sure all API are called and there is no failure.
    expect(errorEl.innerHTML).toBe('');
    expect(mockCommand).toHaveBeenCalledTimes(1);
    expect(mockExtract).toHaveBeenCalledTimes(6);
  });
});

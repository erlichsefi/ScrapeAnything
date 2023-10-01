// main.test.js
const { JSDOM } = require('jsdom');

let window;
let document;

beforeAll(() => {
  const dom = new JSDOM('<!doctype html><html><body></body></html>');
  window = dom.window;
  document = window.document;
});

afterAll(() => {
  // Clean up resources after the tests
  window.close();
});

const { getCurrentTab } = require('./main'); // Import the functions to be tested

describe('getCurrentTab', () => {
  it('should return the current tab', async () => {
    const fakeTab = { id: 1 };
    chrome.tabs.query = jest.fn().mockResolvedValue([fakeTab]);

    const tab = await getCurrentTab();

    expect(tab).toEqual(fakeTab);
  });

  it('should handle errors gracefully', async () => {
    chrome.tabs.query = jest.fn().mockRejectedValue(new Error('Test Error'));

    const tab = await getCurrentTab();

    expect(tab).toBeNull();
  });
});

// Write similar test cases for other functions in main.js

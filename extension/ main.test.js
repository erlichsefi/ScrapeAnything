// main.test.js
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

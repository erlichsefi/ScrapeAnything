// Import the functions to be tested
const {click_coordinates,click_coordinates_and_text,keyborad_action} = require('../extension/shared/act/click.js');

// Mock the document functions used in the code
document.elementFromPoint = jest.fn();
document.dispatchEvent = jest.fn();
// Mock the element returned by document.elementFromPoint
const element = {
  click: jest.fn(),
};

// Mock the document functions used in the code
document.elementFromPoint = jest.fn(() => element);
describe('Click and Keyboard Actions', () => {
  afterEach(() => {
    jest.clearAllMocks();
  });

  it('should click on element at coordinates', () => {
    click_coordinates(10, 20);
    expect(document.elementFromPoint).toHaveBeenCalledWith(10, 20);
    expect(element.click).toHaveBeenCalled(); // You should mock 'element' accordingly
  });

  it('should click on element at coordinates and set text', () => {
    const text = 'Example Text';
    click_coordinates_and_text(30, 40, text);
    expect(document.elementFromPoint).toHaveBeenCalledWith(30, 40);
    expect(element.click).toHaveBeenCalled(); // You should mock 'element' accordingly
    expect(element.value).toBe(text); // You should mock 'element' accordingly
  });

  it('should trigger "Escape" keyboard event', () => {
    const eventMock = jest.fn();
    document.dispatchEvent.mockImplementation(eventMock);
    keyborad_action('esc');
    expect(eventMock).toHaveBeenCalledWith(expect.any(KeyboardEvent));
    expect(eventMock.mock.calls[0][0].key).toBe('Escape');
  });

  it('should trigger "Enter" keyboard event', () => {
    const eventMock = jest.fn();
    document.dispatchEvent.mockImplementation(eventMock);
    keyborad_action('enter');
    expect(eventMock).toHaveBeenCalledWith(expect.any(KeyboardEvent));
    expect(eventMock.mock.calls[0][0].key).toBe('Enter');
  });
});

def get_text_with_confidence(matrix,confidence=80):
    import pytesseract
    pytesseract.pytesseract.tesseract = r'/usr/local/bin/pytesseract'

    df = pytesseract.image_to_data(matrix, output_type='data.frame')
    predictions = df[df.conf != -1]
    if predictions.shape[0] == 0:
        return ""
    predictions = predictions.nlargest(1,'conf').iloc[0]
    response = ''
    if predictions['conf'] > confidence:
        response = predictions['text']
    return response.strip()

## Method: Vision (image) -> Text

General idea:
1. take a snapshot of the browser current state
2. Segment the image to section
3. Convert each section into text by
    3.1 converting the text on the image to text.
    3.2 describe the images on screen using some method.
4. ask the LLM what action the run on the browers.
5. repeat until LLM execute 'STOP'


Advantages: This method simulate human behavior hence, this method can only be blocked by Captcha.
 
Dis-advantages: There is alot of hidden inforamtion we are ignoring, like: hover text, drop menus, etc. The LLM will only overcome this if he will move the mouse to the right location on screen.
# clipboard-img-to-text
clipboard-img-to-text is a simple Python script that converts an image from clipboard (PNG) into text using OCR, and sends notifications via notify-send to indicate success or errors.

## Usage
1. Copy an image to the clipboard using your favorite screenshot tool (e.g., Flameshot).
2. Run the script:
`python3 clipboard-img-to-text.py`
3. The recognized text will be automatically copied to your clipboard.
4. Desktop notifications indicate whether the OCR was successful or if an error occurred.

**Notice**: the code only works with PNG format. Its baked into the code. (xclip parameter)

## I3 integration example
Run the script every time when `win/super` and `prtScr` is pressed:
```bash
bindsym $mod2+Print exec flameshot-gui && python3 path/to/image-to-text.py
```

Bind the script to another key:
```bash
bindsym $mod2+o exec python3 path/to/image-to-text.py
```

## Requirements
- Python
- tesseract-ocr
  - pytesseract
- xclip
- notifyd

## Features that needed
- Better OCR engine 
- markdown support (convert the text to md)

  

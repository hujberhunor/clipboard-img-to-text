#!/usr/bin/env python3
import subprocess
from PIL import Image
import io
import pytesseract
import sys

def notify(summary, message):
    subprocess.run(['notify-send', summary, message])

def main():
    try:
        result = subprocess.run(
            ['xclip', '-selection', 'clipboard', '-t', 'image/png', '-o'],
            stdout=subprocess.PIPE,
            check=True
        )
        img = Image.open(io.BytesIO(result.stdout))

        text = pytesseract.image_to_string(img, lang='eng+hun')

        subprocess.run(
            ['xclip', '-selection', 'clipboard'],
            input=text.encode('utf-8'),
            check=True
        )

        notify("OCR DONE", text)

    except Exception as e:
        notify("OCR error", str(e))
        sys.exit(1)

if __name__ == "__main__":
    main()


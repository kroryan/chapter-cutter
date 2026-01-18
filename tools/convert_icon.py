from PIL import Image
import os
import sys

def main():
    root = os.path.dirname(os.path.dirname(__file__))
    png = os.path.join(root, 'app-icon.png')
    ico = os.path.join(root, 'app-icon.ico')
    if not os.path.exists(png):
        print('No app-icon.png found, skipping conversion')
        return
    im = Image.open(png)
    # Save as .ico with multiple sizes
    im.save(ico, sizes=[(256,256),(128,128),(64,64),(48,48),(32,32),(16,16)])
    print('Wrote', ico)

if __name__ == '__main__':
    main()

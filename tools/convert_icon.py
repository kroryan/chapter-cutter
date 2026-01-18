from PIL import Image
import os
import sys

def main():
    root = os.path.dirname(os.path.dirname(__file__))
    png = os.path.join(root, 'app-icon.png')
    ico = os.path.join(root, 'app-icon.ico')
    # If PNG exists -> build ICO. If PNG missing but ICO exists -> regenerate PNG from ICO (small)
    if os.path.exists(png):
        im = Image.open(png)
        im.save(ico, sizes=[(256,256),(128,128),(64,64),(48,48),(32,32),(16,16)])
        print('Wrote', ico)
        return

    if os.path.exists(ico):
        im = Image.open(ico)
        # save a 256x256 PNG for GUI display
        out_png = os.path.join(root, 'app-icon.png')
        im = im.convert('RGBA')
        im = im.resize((64,64), Image.LANCZOS)
        im.save(out_png)
        print('Regenerated', out_png)
        return

    print('No icon source found (app-icon.png or app-icon.ico)')

if __name__ == '__main__':
    main()

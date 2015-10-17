#!/usr/bin/env python
import os
import tempfile

from PIL import Image


def main():
    src_path = os.path.join(os.path.dirname(__file__), 'tweedledee.jpg')
    img = Image.open(src_path)

    x, y = img.size[0], img.size[1]
    bottom_half_img = img.crop((0, y / 2, x, y))
    with tempfile.NamedTemporaryFile() as fd:
        bottom_half_img.save(fd.name, 'jpeg')

        diff = img._new(img.im.chop_difference(bottom_half_img.im))
        diff_path = os.path.join(os.path.dirname(__file__), 'diff_py.jpg')
        diff.save(diff_path)


if __name__ == '__main__':
    main()

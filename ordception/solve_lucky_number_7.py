#!/usr/bin/env python
import os

from bs4 import BeautifulSoup


def decode_arr(arr_str):
    return ''.join(map(chr, eval(arr_str)))


def main():
    fd = open(os.path.join(os.path.dirname(__file__), 'lucky_number_7.htm'))
    soap = BeautifulSoup(fd.read(), 'lxml')
    fd.close()
    arr_html = soap.find('h3')
    arr_str = arr_html.contents[0]
    i = 0
    while arr_str[0] == '[':
        i += 1
        arr_str = decode_arr(arr_str)
    print i
    print arr_str


if __name__ == '__main__':
    main()

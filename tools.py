import urllib.request
import os
import shutil


d = {'а': 'a',
     'б': 'b',
     'в': 'v',
     'г': 'g',
     'д': 'd',
     'е': 'e',
     'ё': 'e',
     'ж': 'j',
     'з': 'z',
     'и': 'i',
     'й': 'i',
     'к': 'k',
     'л': 'l',
     'м': 'm',
     'н': 'n',
     'о': 'o',
     'п': 'p',
     'р': 'r',
     'с': 's',
     'т': 't',
     'у': 'ou',
     'ф': 'f',
     'х': 'kh',
     'ц': 'ts',
     'ч': 'tch',
     'ш': 'ch',
     'щ': 'cht',
     'ъ': '',
     'ы': 'y',
     'ь': '',
     'э': 'e',
     'ю': 'you',
     'я': 'ya',
     ' ': '_',
     '(': '',
     ')': '',}

def ru2en(s):
    res = []
    for c in s:
        if ord('А') <= ord(c) <= ord('Я'):
            c = chr(ord(c) - ord('А') + ord('а'))
        if c in d:
            c = d[c]
        res.append(c)
    return ''.join(res)
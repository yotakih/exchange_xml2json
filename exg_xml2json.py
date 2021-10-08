#-*- coding: utf-8 -*-

import chardet
import codecs
import xmltodict
import json
import re
import sys

def exchange(xml: object) -> dict:
    return xmltodict.parse(xml)

def readfile_auto(file: str) -> str:
    enc = ''
    with codecs.open(file, 'rb') as f:
        enc = chardet.detect(f.read())['encoding']
    # shift_jis系は誤判定が多い？
    if re.match('windows\-', enc, re.IGNORECASE):
        enc = 'cp932'
    txt = ''
    with codecs.open(file, 'r', enc) as f:
        txt = f.read()
    return txt

def format_json(jsntxt) -> str:
    return json.dumps(jsntxt, indent=4, ensure_ascii=False, sort_keys=True)

print(format_json(exchange(readfile_auto(sys.argv[1]))))

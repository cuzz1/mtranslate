#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mtranslate import translate
import getopt
import sys


def usage():
    print('''python3 main.py -c "你好啊" -f ch -t en''')

def main():

    from_language = "auto"
    to_language = "auto"
    content = ""
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'f:t:c:h', ['from=', 'to=', "content",'help'])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
            sys.exit(2)
        elif opt in ('-f', '--from_language'):
            from_language = arg
        elif opt in ('-t', '--to_language'):
            to_language = arg
        elif opt in ('-c', '--content'):
            content = arg
        else:
            usage()
            sys.exit(2)

    res = translate(content, from_language=from_language, to_language=to_language)
    print(res)


if __name__ == '__main__':
    main()

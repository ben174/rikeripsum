#!/usr/bin/env python
import re

def main():
    f = open('scripts/seasonone/11001001.htm')
    body = f.read()
    body = body.replace('\n', '').replace('\r', '').replace('<br>', '')
    matches = re.findall(r'<p> RIKER[ ]+(.*?)</p>', body, re.MULTILINE)
    for match in matches: 
        line = ' '.join(match.split())
        line = re.sub(r'\(.*?\)', '', line).strip()
        line = line.replace('&quot;', '"')
        #line = re.sub(r'\s+', ' ', match)
        print "MATCH: %s" % line



if __name__ == '__main__': 
    main()

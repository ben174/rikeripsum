#!/usr/bin/env python
import re
import os, os.path



def main():
    lines = []
    for season_dir in os.listdir('scripts'): 
        if season_dir == '.DS_Store': 
            continue
        for script_file in os.listdir('scripts/' + season_dir): 
            curr_lines = extract_riker_lines('scripts/%s/%s' % (season_dir, script_file))
            lines.extend(curr_lines)
    for line in lines: 
        print line


def extract_riker_lines(filename): 
    lines = []
    f = open(filename)
    body = f.read()
    body = body.replace('\n', '').replace('\r', '').replace('<br>', '')
    matches = re.findall(r'<p> RIKER[ ]+(.*?)</p>', body, re.MULTILINE)
    for match in matches: 
        line = ' '.join(match.split())
        line = re.sub(r'\(.*?\)', '', line).strip()
        line = line.replace('&quot;', '"')
        lines.append(line)
    return lines 



if __name__ == '__main__': 
    main()

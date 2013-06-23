#!/usr/bin/env python
import re
import os, os.path
import pickle

character = 'RIKER'
num_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',]

_ROOT = os.path.abspath(os.path.dirname(__file__))


def get_data(path):
    return os.path.join(_ROOT, 'data', path)


def main():
    lines = []
    for season_num in range(1, 7):
        season_dir = 'scripts/season%s' % num_words[season_num]
        for script_file in os.listdir(season_dir): 
            curr_lines = extract_riker_lines(season_num, script_file)
            lines.extend(curr_lines)
    lines.sort()

    pickle_file = open(get_data('%s.pickle' % character.lower()), 'wb')
    pickle.dump(lines, pickle_file)
    pickle_file.close()

    for line in lines: 
        print line


def extract_riker_lines(season_num, filename): 
    lines = []
    f = open('scripts/season%s/%s' % (num_words[season_num], filename))
    body = f.read()
    body = body.replace('\n', '').replace('\r', '')
    matches = re.findall(r'<p> ' + character + r'<br>[ ]+(.*?)</p>', body)
    for match in matches: 
        line = {}
        line['text'] = ' '.join(match.split())
        line['text'] = re.sub(r'\(.*?\)', '', line['text'])
        line['text'] = line['text'].replace('<br>', '').strip()
        line['text'] = line['text'].replace('&quot;', '"')
        line['episode'] = filename.replace('.htm', '')
        line['word_count'] = len(line['text'].split())
        lines.append(line)
    return lines 


if __name__ == '__main__': 
    main()

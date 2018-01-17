#!/usr/bin/env python
import os, os.path
import pickle

num_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',]

_ROOT = os.path.abspath(os.path.dirname(__file__))


def get_data(path):
    return os.path.join(_ROOT, 'data', path)

def main():
    lines = {}
    for season_num in range(1, 7):  # check every script for all seasons
        season_dir = 'scripts/season%s' % num_words[season_num]
        for script_file in os.listdir(season_dir):
            record = False
            dbuffer = ""
            charname = ""
            f = open('scripts/season%s/%s' % (num_words[season_num], script_file))
            for data in f.readlines():  # look for pattern indicating charector name
                if "<p>" in data and "<br>" in data:
                    splited = data.split("<p>")[-1].split("<br>")[0]
                    splited = splited.split("'S")[0].split(" ")
                    if len(splited) > 5:  # long list of words probably isnt a name
                        continue
                    for name in splited:
                        if name.isupper():  # charector names are uppercase
                            charname = name
                            record = True
                            dbuffer = ""
                            break
                elif record:  # if name was just found, extract dialog until </p>
                    dbuffer += data
                    if "</p>" in data:
                        dbuffer = dbuffer.replace("<br>", "").replace("</p>", "")
                        dbuffer = dbuffer.replace("\r", "").replace("\n", "")
                        dbuffer = dbuffer.replace("\a", "").strip()
                        dbuffer = ' '.join(dbuffer.split())
                        line = {"text": dbuffer,
                                "episode": script_file.replace('.htm', ''),
                                "word_count": len(dbuffer.split())}
                        record = False
                        if charname in lines:
                            lines[charname].append(line)
                        else:
                            lines[charname] = [line]

    pickle_file = open(get_data('all_charectors.pickle'), 'wb')
    pickle.dump(lines, pickle_file)
    pickle_file.close()

    stats = []
    for name in lines:
        stats.append([len(lines[name]), name])
    stats.sort()

    for num_lines, name in stats:
        print(name, ": ", num_lines, "lines parsed")


if __name__ == '__main__':
    main()

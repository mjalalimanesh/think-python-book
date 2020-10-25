"""
Created on Thu Oct 22 18:12:49 2020
@author: mohamad jalalimanesh
"""
import os
import shelve
from anagram_sets import all_anagrams


def walk2(dirname):
    """Prints the names of all files in dirname and its subdirectories.
    This is the exercise solution, which uses os.walk.
    dirname: string name of directory
    """
    for root, dirs, files in os.walk(dirname):
        for filename in files:
            print(os.path.join(root, filename))


####################  14_1  #####################


def sed(filename_1, filename_2, pattern_str, replacement_str):
    try:
        fin = open(filename_1)
        inputfile = fin.read()
        outputfile = inputfile.replace(pattern_str, replacement_str)
        fin.close()
    except:
        print("Error in file 1")
        return

    try:
        fout = open(filename_2, "w")
        fout.write(outputfile)
        fout.close()
    except:
        print("Error in file 2")
        return


####################  14_2  #####################


def store_anagrams(anagram_map, filename):
    """
    Stores the anagrams from a dictionary in a shelf
    """
    with shelve.open(filename) as db:
        for key, value in anagram_map.items():
            db[key] = value


def read_anagrams(key, filename):
    """
    Looks up a word in a shelf and returns a list of its anagrams.
    """
    with shelve.open(filename) as db:
        try:
            return db[key]
        except KeyError:
            return []


####################  14_3  #####################


def find_duplicate_files(dirname):
    """
    
    """
    for root, dirs, files in os.walk(dirname):
        d = {}
        for fileall in files:
            filename = os.path.join(root, fileall)
            #            print(filename)
            cmd = "md5sum " + filename
            fp = os.popen(cmd)
            res = fp.read()
            stat = fp.close()
            md5 = res[0:32]
            if md5 not in d:
                d[md5] = 1
            else:
                fname = res[32:].strip()
                print(fname, "is duplicate")


if __name__ == "__main__":
    #    walk2('/home/mohamad/Music/درهم')
    #    sed('kafka.txt', 'newfile.txt', 'Gutenberg', 'nurenberg!')
    #    anagram_map = all_anagrams('words.txt')
    #    store_anagrams(anagram_map, filename='anagram_save.db')
    #    anagrams = read_anagrams('aah', filename='anagram_save.db')
    find_duplicate_files(".")


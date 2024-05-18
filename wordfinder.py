import json
import fnmatch
import argparse

#you need to download this file https://raw.githubusercontent.com/matthewreagan/WebstersEnglishDictionary/master/dictionary_compact.json
#in the same folder as the script for it to work (not included because license)
#it's the Webster's english Dictionary from the Gutenberg Project.

#https://www.gutenberg.org/ebooks/29765 link to the original file


parser = argparse.ArgumentParser(
                    prog='The WordFinder',
                    description='Finds words lacking all the letters',
                    )

parser.add_argument("-m", "--meaning", action="store_true")
args = parser.parse_args()
show_meaning = args.meaning


word = input("Input the word: ")
word = word.replace("_","?")


f = open("dictionary_compact.json","r")
big = f.read()

clean = []

j = json.loads(big)
for a in j:
    clean.append(a)


result = fnmatch.filter(clean,word)
for r in result:
    if show_meaning:
        meaning = j[r]  
        print(f"\033[91m{r}\033[0m : {meaning}")
    else:
        print(f"\033[91m{r}\033[0m", end=", ")


import json
import fnmatch
import argparse

#you need to download this file https://raw.githubusercontent.com/matthewreagan/WebstersEnglishDictionary/master/dictionary_compact.json
#in the same folder as the script for it to work (not included because license)
#it's the Webster's english Dictionary from the Gutenberg Project.

#The script will try to download it, but you never know...

#https://www.gutenberg.org/ebooks/29765 link to the original file


DICT_URL = "https://raw.githubusercontent.com/matthewreagan/WebstersEnglishDictionary/master/dictionary_compact.json"

parser = argparse.ArgumentParser(
                    prog='The WordFinder',
                    description='Finds words lacking all the letters',
                    )

parser.add_argument("-m", "--meaning", action="store_true") #if we want the meaning of the word too, undocumented on purpose
args = parser.parse_args()
show_meaning = args.meaning

word = input("Input the word: ")
word = word.replace("_","?")

try:
    f = open("dictionary_compact.json","r")
except FileNotFoundError:
    print(f"Dictonary not found, downloading from \033[91m{DICT_URL}\033[0m")
    print("This may take a while ...")
    import urllib.request
    urllib.request.urlretrieve(DICT_URL, "dictionary_compact.json")
    try:
        f = open("dictionary_compact.json","r")
    except FileNotFoundError:
        raise

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

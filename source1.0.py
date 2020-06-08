import json
from difflib import get_close_matches

data = json.load(open("data.json")) ##Loading json file

word = input("Enter the word: ") ##Asking for input from user
key = word.lower() ##converting all letter in the word to lowercase as all words are in lowercase in our database

##Function which finds meaning

def meaning(key):

    if key in data:
        return data[key]
    
##To guess words

    elif key.upper() in data:
        return data[key.upper()]

    elif len(get_close_matches(key, data.keys())) >> 0:
        yn = input("Did you mean %s instead? Type 'Y' for yes and 'N' for no: "%get_close_matches(key, data.keys())[0])
        if yn == 'Y':
            return data[get_close_matches(key, data.keys())[0]]
        elif yn == 'N':
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word does not exist. Please check again"

output = meaning(key)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(meaning(key))


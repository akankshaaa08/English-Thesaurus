import json
from difflib import get_close_matches

data = json.load(open("app1-dict/data.json"))

def translate (word):
    if word in data:                            
        return data[word]

    elif word.title() in data :                                 #for cities name like 'Delhi' , 'Tokyo'
        return data[word.title()]

    elif word.upper() in data :
        return data[word.upper()]                               #for acronyms like 'USA' , 'NASA'

    elif len(get_close_matches(word,data.keys())) > 0 :         #returns the length of the sequence having similar matches
        new_word = get_close_matches(word,data.keys())[0]           #returns the first word(most accurate) from the sequence
        print ("Did you mean '{}' instead?".format(new_word))
        ch=input("Press 'y' for Yes and 'n' for No   :   ")
        if ch == 'y' or ch=='Y' :
            return data[new_word]
        elif ch == 'n' or ch=='N' :
            return ("word does not exist. Try Again!")
        else :    
            return ("Wrong Input!")

    else :    
        return ("Word does not exist")

print("WELCOME TO ENGLISH THESAURUS\n")
w=input("Enter Word : ")
output=translate(w.lower())

if type(output) == list :
    i=1
    for item in output :
        print(i,". ",item)
        i=i+1
else :
    print(output)
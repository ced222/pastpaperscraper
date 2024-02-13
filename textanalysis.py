import os, json
import nltk
from nltk.corpus import stopwords, wordnet
import matplotlib.pyplot as plt
cwd = os.getcwd()
#initalization
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
def has_alpha_key(key):
    if isinstance(key, str) and key.isalpha():
        return True
    for i in key:
        if i.isalpha():
            return True
    return False

for number in range(8):
    #importing the text file to process
    print("Current working directory:", cwd)
    file_path = '\\topics\\Computer Science\\ch{}comsci.txt'.format(str(number + 1))

    file_path = cwd + file_path
    print(file_path)
    with open(file_path, 'r', encoding='utf-8') as file:
        file_contents = file.read()
    words = {} #dictionary to store words
    #tokenize the text into words
    file_contents = file_contents.split() 

    #filter out stopwords
    file_contents_filtered = [word for word in file_contents if (word.lower() not in stop_words and wordnet.synsets(word))]


    for i in file_contents_filtered: #iterates through the entire text and makes key-value pairs - key is the word and value is the number of occurances
        if i in words:
            words[i] += 1 
        else:
            words[i] = 1

    wordstoDelete = [] #make a list of all invalid keys to delete
    for key, value in words.items():
        if len(key) == 1 or not has_alpha_key(key):
            wordstoDelete.append(key)
    for key in wordstoDelete:
        del words[key] #delete all invalid keys
    print(words)

    file_path_write = os.path.dirname(file_path) + "\\" + "processed chapters\\ch{}.json".format(str(number + 1))  #write a csv file to this file location
    with open(file_path_write, 'w+') as file_json:
        json.dump(words, file_json)







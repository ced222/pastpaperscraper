sentence = input("input a sentence to match topic")
import os, numpy, re, json
cwd = os.getcwd()
topic_dictionaries = {}
for number in range(8): 
    #importing the json files to process
    file_path = '\\topics\\Computer Science\\processed chapters\\ch{}.json'.format(str(number + 1))
    file_path = cwd + file_path
    
    with open(file_path, 'r') as file:
        topic_dictionaries["ch{}".format(str(number+1))] = json.load(file)
def find_highest_value(matches):
    if matches:
        maximum = max(matches.values())
        keys = [key for key, value in matches.items() if value == maximum]
        return maximum, keys
    else:
        return None
def pattern_match(string, pattern_dict): #function to match patterns 
    for pattern in pattern_dict:
        if re.search(pattern, string):
            return True
    return False
def count_matches_in_dict(pattern, dictionary): #count number of keyword matches
    total_matches = 0
    
    for value in dictionary.keys():
        if pattern == value:
            total_matches += len(matches)
    return total_matches
sentence.split() #split user inputted sentence to tokenize it
matches = {}
print(sentence)
for x in range(8):
    for i in sentence:
        if pattern_match(sentence,topic_dictionaries["ch{}".format(x+1)]):
            noMatches = count_matches_in_dict(i, topic_dictionaries["ch{}".format(x+1)])
            matches["ch{}".format(x+1)] = noMatches
        else:
            print("topic is not a match")


highestVal, keyVal = find_highest_value(matches)
print(highestVal)
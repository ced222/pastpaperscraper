import spacy
import os, json
#cleans the inputted textbook data - tbh i have no idea how the code works i copy pasted it
nlp = spacy.load("en_core_web_sm")
cwd = os.getcwd()
def openFile():
    all_topic_texts = []
    #importing the text file to process
    print("Current working directory:", cwd)
    for i in range(8):
        file_path = '\\topics\\Computer Science\\ch{}comsci.txt'.format(str(i + 1))

        file_path = cwd + file_path
        print(file_path)
        with open(file_path, 'r', encoding='utf-8') as file:
            file_contents = file.read()
            all_topic_texts.append([file_contents, "ch{}comsci".format(str(i + 1))])
    return all_topic_texts

def cleanText(complete_text, textTopic): #function for effectively processing text
    complete_doc = nlp(complete_text)
    print(complete_doc)
    blacklist = {'processes','program','purpose','Describe','candidates', 'explain','including', 'show', 'understanding', 'use', 'justify', 'notes', 'guidance', 'terms'}
    def is_token_allowed(token):
        return bool(
            token
            and str(token).strip()
            and not token.is_stop
            and not token.is_punct
            and not token.text.lower() in blacklist
        )

    def preprocess_token(token):
        
        return token.lemma_.strip().lower()
    

        
    complete_filtered_tokens = [
        preprocess_token(token)
        for token in complete_doc
        if is_token_allowed(token)
    ]
    return [complete_filtered_tokens, textTopic]

    
#initalization
complete_texts = openFile() #returns all 8 chapters of comsci AS
complete_cleaned_texts = [] #texts after they have been cleaned
for text in complete_texts:
    complete_cleaned_texts.append(cleanText(text[0], text[1]))
print(complete_cleaned_texts)


def checkSentenceMatch(sentence, topicText):
    totalScore = 0
    complete_sentence, _ = cleanText(sentence, None)
    for i in complete_sentence:
        totalScore += topicText.count(i)
    return totalScore

#mainloop
while True: 
    sentence = input("Sentence to match: ")
    totalMatches = {}
    for texts in complete_cleaned_texts:
        totalMatches[texts[1]] = checkSentenceMatch(sentence, texts[0])

    key_with_largest_value = max(totalMatches, key=totalMatches.get)
    print("Most likely topic match: " + key_with_largest_value)
import yake
import os, json
#cleans the inputted textbook data - tbh i have no idea how the code works i copy pasted it
# nlp = spacy.load("en_core_web_sm")
cwd = os.getcwd()


def openFile():
    '''Returns each chapter as a item in a list'''
    all_topic_texts = []
    #importing the text file to process
    # print("Current working directory:", cwd)
    for i in range(8):
        file_path = '\\topics\\Computer Science\\ch{}comsci.txt'.format(str(i + 1))

        file_path = cwd + file_path
        # print(file_path)
        with open(file_path, 'r', encoding='utf-8') as file:
            file_contents = file.read()
            all_topic_texts.append([file_contents, "{}".format(str(i + 1))])
    return all_topic_texts

def getKeywords(text, n=3):
    kw_extractor = yake.KeywordExtractor(n=n)
    keywords = kw_extractor.extract_keywords(text)

    return keywords

def chapterKeywords():
    language = "en"
    numOfKeywords = 200

    custom_kw_extractor = yake.KeywordExtractor(lan=language,top=numOfKeywords,n=2,features=None)

    chapterList = openFile()
    # print(len(chapterList))
    chapterKw = []


    for text in chapterList:
        keywords = custom_kw_extractor.extract_keywords(' '.join(text))
        chapterKw.append(keywords)
    return chapterKw




# def cleanText(complete_text, textTopic): #function for effectively processing text
#     complete_doc = nlp(complete_text)
#     # print(complete_doc)
#     # blacklist = {'processes','program','purpose','Describe','candidates', 'explain','including', 'show', 'understanding', 'use', 'justify', 'notes', 'guidance', 'terms'}
#     def is_token_allowed(token):
#         return bool(
#             token
#             and str(token).strip()
#             and not token.is_stop
#             and not token.is_punct
#             # and not token.text.lower() in blacklist
#         )

#     def preprocess_token(token):
        
#         return token.lemma_.strip().lower()
    

        
#     complete_filtered_tokens = [
#         preprocess_token(token)
#         for token in complete_doc
#         if is_token_allowed(token)
#     ]
#     return [complete_filtered_tokens, textTopic]

    
# #initalization
# complete_texts = openFile() #returns all 8 chapters of comsci AS
# complete_cleaned_texts = [] #texts after they have been cleaned
# for text in complete_texts:
#     complete_cleaned_texts.append(cleanText(text[0], text[1]))
# # print(complete_cleaned_texts)


# def checkSentenceMatch(sentence, topicText):
#     totalScore = 0
#     complete_sentence, _ = cleanText(sentence, None)
#     for i in complete_sentence:
#         totalScore += topicText.count(i)
#     return totalScore
# kw_extractor = yake.KeywordExtractor()
# language = "en"
# max_ngram_size = 3
# deduplication_threshold = 0.9
# numOfKeywords = 20
# custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)
# def getTopic(queation):
#     sentence = queation[1]
#     totalMatches = {}
#     keywords = custom_kw_extractor.extract_keywords(sentence)
#     sentence = ''
#     for i, j in keywords:
#         sentence += i + ' '
#     for texts in complete_cleaned_texts:
#         totalMatches[texts[1]] = checkSentenceMatch(sentence, texts[0])

#     key_with_largest_value = max(totalMatches, key=totalMatches.get)
#     print("Queation " + queation[0], "Most likely topic match: chapter " + key_with_largest_value)
# #mainloop

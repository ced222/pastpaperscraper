import os
from pdfreader import phrasePdf

cwd = os.getcwd()

#configuration for which paper to find
paperVariant = 3
paperSeries = 2022
paperSeason = "Summer"
paper = 1

paperPath = cwd + "\\past papers\\9618\\{}\\{}.pdf".format((str(paperSeries)), ("9618_" + paperSeason[0].lower() + str(paperSeries)[2:] + "_" +"qp" + "_" + str(paper) + str(paperVariant)))
questions = phrasePdf(paperPath)
numberofChapters = 8
def openFile(cwd, numberofChapters):
    all_topic_texts = {}
    #reads each computer science text file which contains manually inputted keywords and phrases
    for i in range(numberofChapters ):
        file_path = '\\topics\\Computer Science\\processed chapters\\ch{}.txt'.format(str(i + 1))

        file_path = cwd + file_path
        # print(file_path)
        with open(file_path, 'r', encoding='utf-8') as file:
            file_contents = file.readlines()
           
            all_topic_texts["{}".format(str(i + 1))] =  file_contents
    # print(all_topic_texts)
    return all_topic_texts
keywords = openFile(cwd,8) #returns all keywords in the text file
print(keywords)

def findMatch(keywords, question):
    listOfMatchesByChapter = {}
    matches = 0
    question = question.lower()
 

    for chapterIndex in range(len(keywords)):
  
        
        for key_word in keywords[str(chapterIndex + 1)]: #search through each keyword and see whether it is a substring nside the question 
            
            key_word = key_word.replace("\n", "")
            key_word = key_word.lower()
            matches += question.count(key_word) #if match found, increment matches
            
            
        listOfMatchesByChapter[str(chapterIndex+1)] = matches #add matches to dictionary
        
        matches = 0 #reset matches
    
    return listOfMatchesByChapter

#main program
# print(questions[0][1]) #format for questions is index 0 contains question number and index 1 contains question itself

for question in questions:
    
    listOfMatches = findMatch(keywords, question[1])
        #finds question with highest count
    for key, value in listOfMatches.items():
        
        if value == max(listOfMatches.values()):
            max_key = key
            break
    print( "Question " + question[0] + " topic is: Chapter {}".format(max_key))
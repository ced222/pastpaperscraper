  # importing required modules
import PyPDF2, os, re
#from textanalysis import getTopic


def openPdf(pdfFile, page):
    # creating a pdf file object
    pdfFileObj = open(pdfFile, 'rb')
    # creating a pdf reader object
    pdfReader = PyPDF2.PdfReader(pdfFileObj)
    # printing number of pages in pdf file
    pages = len(pdfReader.pages)
    # creating a page object
    pageObj = pdfReader.pages[page]
    # extracting text from page
    pageText = pageObj.extract_text()
    # closing the pdf file object
    pdfFileObj.close()
    return pageText, pages
 
def markQuestion(match, index, pageText, last_match):
    #slice the string to determine which half of the string (top/bottom) that the question detecter is supposed to iterate from
    substring = ' ['
    first_match = pageText.find(substring, index)
    return pageText[index:first_match].replace('.','')
        
def phrasePdf(filePath):
    '''Return format : [sub question number + letter, question text]'''
    pdfText = []
    #returns the number of pages in the pdf
    _, pages = openPdf(filePath, 0)
    #returns the text from each page and append them to a list (one list one pdf)
    for i in range(pages):
        pageText, _ = openPdf(filePath, i)
        pdfText.append(pageText)

    substring = r'\([a-h]\)'

    questions = []
    #the first question name is 0
    currentQuestionNum = 0
    for page in pdfText[1:]:
        last_match = 0
        found = False
        # skip if BLANK PAGE is written on the page
        if 'BLANK PAGE' in page:
            continue
        # find queation based on sub queation, as it is easy to detect
        for match in re.finditer(substring, page):
            print(match.group())
            #subquestion a marks that there is a main question
            if match.group()[1] == 'a':
                currentQuestionNum += 1
            questionText = markQuestion(match, match.start(), page, last_match)
            questions.append([str(currentQuestionNum)+match.group()[1],questionText])
            found = True
        # if no sub question found, check the page for marks given
        if found == False:
            pagetext = '\n'.join(page.split('\n')[2:])
            # print('No queation this page? Searching for marks given')

            for match in re.finditer('\[\d+\]', pagetext):
                foundIndex = match.start()
                # if marks found, find a number before the marks given. This could be a queation number or 
                # just a part of the question
                for match in re.finditer('\d+', pagetext[:foundIndex]):
                    startIndex = match.start()
                    # check if number found is on the 3rd line
                    # paper layout is 1st line page number 2nd line subject code
                    # the 3rd line therefore countain the question number if there is one
                    if match.group() in page.split('\n')[2][:4]:
                        currentQuestionNum += 1
                        questionText = pagetext[startIndex:foundIndex]
                        questions.append([str(currentQuestionNum)+'a',questionText])
            

    return questions

if __name__ == '__main__':
    cwd = os.getcwd()
    filePath = cwd + '/past papers/9618/2023/9618_s23_qp_11.pdf'
    phrasePdf(filePath)

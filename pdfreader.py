  # importing required modules
import PyPDF2, os, re
from textanalysis import getTopic
cwd = os.getcwd()
filePath = cwd + '/past papers/computer Science - 9618/2023/9618_s23_qp_11.pdf'

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
        
pdfText = []
_, pages = openPdf(filePath, 0)

for i in range(pages):
    pageText, _ = openPdf(filePath, i)
    pdfText.append(pageText)

substring = r'\([a-h]\)'

queations = []
currentQueationNum = 0
for page in pdfText:
    last_match = 0
    for match in re.finditer(substring, page):
        if match.group()[1] == 'a':
            currentQueationNum += 1
        queationText = markQuestion(match, match.start(), page, last_match)
        queations.append([str(currentQueationNum)+match.group()[1],queationText])

for i in queations:
    getTopic(i)
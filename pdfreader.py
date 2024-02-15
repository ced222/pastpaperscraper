  # importing required modules
import PyPDF2, os, re
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
 
def markQuestion(match, index, pageText):
    #slice the string to determine which half of the string (top/bottom) that the question detecter is supposed to iterate from
    substring = r='\d '
    first_match = re.search(substring, pageText)
    print("Question" + str(first_match.group()), first_match.start())
        
pdfText = []
_, pages = openPdf(filePath, 0)

for i in range(pages):
    pageText, _ = openPdf(filePath, i)
    pdfText.append(pageText)
print(pdfText[3])

substring = r'\([a-h]\)'



for i in pdfText:
    
    for match in re.finditer(substring, i):
        markQuestion(match, match.start(), i)
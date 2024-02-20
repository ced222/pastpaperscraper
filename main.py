from pdfreader import phrasePdf
from textanalysis import chapterKeywords, getKeywords
import os

cwd = os.getcwd()
filePath = cwd + '/past papers/computer Science - 9618/2023/9618_s23_qp_11.pdf'
questions = phrasePdf(filePath)
chapterKw = chapterKeywords()
blacklist = ['complete', 'definition', 'term', 'terms', 'defining', 'explain']
for i,question in questions:
    keywords = getKeywords(question)
    keywords2 = []
    for ii, ji in keywords:
        skip = False
        for ki in ii.lower().split(' '):
            if ki in blacklist:
                skip = True
        if skip == False:
            keywords2.append((ii,ji))

    keywords = keywords2
    

    if i == '1a':
        print(keywords, "ch1 keywords")
        print(keywords2, "question keywords")

    current = []
    probs = []
    fkw = []
    for kw,__ in keywords[:5]: #search through each keyword in the question
        for chapter in chapterKw: #search through each chapter
            
            for ckw,_ in chapter: #search each keyword in each chapter
                for kwi in kw.split(): 
                    if kwi in ckw and len(ckw.split(' ')) != 1:
                        matchFound = True #if there is a keyword match, its true, else false
                        current.append(chapterKw.index(chapter))
                        probs.append(__*_)
                        fkw.append([kw,ckw])
                        break
    print(probs)
    if matchFound:
        pindex = probs.index(min(probs))
    print(i, ': Chapter',current[pindex] + 1, end=' or ')
    del probs[probs.index(min(probs))]
    try:
        while fkw[pindex][0] == fkw[probs.index(min(probs))][0] and len(probs) != 1:
            del probs[probs.index(min(probs))]
        print(current[probs.index(min(probs))] + 1, end=' ')
        print(f'used keyword {fkw[pindex]} and {fkw[probs.index(min(probs))]}')
    except:
        print(f'used keyword {fkw[pindex]}')
    
    # print(queation.replace('.','').replace('\n',' '))
from pdfreader import phrasePdf
from textanalysis import chapterKeywords, getKeywords
import os

cwd = os.getcwd()
filePath = cwd + '/past papers/computer Science - 9618/2023/9618_s23_qp_11.pdf'
queations = phrasePdf(filePath)
chapterKw = chapterKeywords()
blacklist = ['complete', 'definition', 'term', 'terms', 'defining', 'explain']
for i,queation in queations:
    keywords = getKeywords(queation)
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
        print(keywords)

    current = []
    probs = []
    fkw = []
    for kw,__ in keywords[:5]:
        for chapter in chapterKw:
            for ckw,_ in chapter:
                for kwi in kw.split():
                    if kwi == ckw and len(ckw.split(' ')) != 1:
                        current.append(chapterKw.index(chapter))
                        probs.append(__*_)
                        fkw.append([kw,ckw])
                        break
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
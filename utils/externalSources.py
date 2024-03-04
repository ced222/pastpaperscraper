import requests
import traceback
import datetime
import os

NORMAL = 200
URLS = [
    'https://papers.xtremepape.rs/CAIE/AS%20and%20A%20Level/',
    'https://papers.gceguide.com/A%20Levels/',
    'https://bestexamhelp.com/exam/cambridge-international-a-level/',]
    
# https://papers.xtremepape.rs/CAIE/AS%20and%20A%20Level/Computer%20Science%20(for%20first%20examination%20in%202021)%20(9618)/9618_s21_qp_12.pdf
def getPaper(syllabusCode = '9618', paperSeries = '2022', paperSeason = "summer", paper = '2', paperVariant = '3'):
    global NORMAL, URLS
    syllabusCode = str(syllabusCode)
    paperSeries = str(paperSeries)
    paper = str(paper)
    paperVariant = str(paperVariant)
    for url in URLS:
        r = requests.get(url)
        if r.status_code == NORMAL:
            r_index = r.text.index(syllabusCode)

            syllabusName = r.text[r_index-70:r_index+4].split('"')[-1]

            # fix for gceguide
            if url == 'https://papers.gceguide.com/A%20Levels/':
                syllabusName = r.text[r_index-50:r_index+5].split('"')[-1].split('\\')[0]

            url = f'{url}/{syllabusName}/{paperSeries}/{syllabusCode}_{paperSeason[:1]}{paperSeries[2:]}_qp_{paper+paperVariant}.pdf'
            print(url)
            if not os.path.exists("past papers\\" + syllabusCode + "\\" + paperSeries):
                os.makedirs("past papers\\" + syllabusCode + "\\" + paperSeries)
            
            pdf_filename = os.path.join("past papers\\" + syllabusCode + "\\" + paperSeries, f'{syllabusCode}_{paperSeason[:1]}{paperSeries[2:]}_qp_{paper+paperVariant}.pdf')
            pdf_response = requests.get(url)

            if pdf_response.status_code == NORMAL:
                print('Found')
                with open(pdf_filename, 'wb') as pdf_file:
                    pdf_file.write(pdf_response.content)
                    print(f'Downloaded {syllabusCode}_{paperSeason[:1]}{paperSeries[2:]}_qp_{paper+paperVariant}.pdf')
                return True
            else:
                print(f'Error downloading, status code {pdf_response.status_code}')
                print('Falling back to next URL')
    


# getPaper()

if __name__ == '__main__':
    import threading
    getSyllabus = ['9618','9709','9231']
    for syllabus in getSyllabus:
        for i in range(2020, 2023+1):
            for j in range(5):
                for k in range(3):
                    threading.Thread(target=getPaper, args = (syllabus,str(i),'s',str(j),str(k))).start()
                    threading.Thread(target=getPaper, args = (syllabus,str(i),'w',str(j),str(k))).start()


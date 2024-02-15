import requests
import traceback
import datetime
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
url = "https://bestexamhelp.com/exam/cambridge-international-a-level/pp-a.php"
class webScraper:
    def __init__(self,url) -> None:
        
        self.response = requests.get(url)
        if self.response.status_code == 200:
            options = webdriver.ChromeOptions()
            options.add_experimental_option("excludeSwitches", ['enable-logging'])
            options.add_argument("--log-level=3")
            options.add_argument("start-maximized")
            options.add_argument("--headless")
            print("connection successful")
            self.driver = webdriver.Chrome(options=options) #initialize web driver object
            self.driver.get(url)
           
            pass #whether request was successful
        else:
            print("failed to establish connection")
            exit() #exit program if connection to past paper website fails to load
        self.action = ActionChains(self.driver) #initalize action chain object
    def findsyllabusCode(self, syllabusCode):
        try:
            code = WebDriverWait(self.driver, 10).until( 
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, syllabusCode)) 
            )
            print("success")
            before_url = self.driver.current_url #get the current URL before clicking
            syllabusName = code.text
            code.click() #click on the correct syllabus code
            after_url = self.driver.current_url #get url after the click
            if before_url != after_url:
                print("Clicking the element worked as expected.")
            else:
                print("Clicking the element did not work as expected.")
            return syllabusName
        except Exception as e:
            print(e)
            traceback.print_exc()
            print("failed")
            self.driver.quit()
    def download(self, syllabusName, year): #download the pdfs and sorts them into approrpriate folders
        print("download menu url: ", self.driver.current_url)
        pdf_links = WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located((By.ID, "pdf")))
        for link in pdf_links:
            pdf_url = link.get_attribute('src')
            namePdf = os.path.split(pdf_url)
            if not os.path.exists("past papers\\" + syllabusName + "\\" + year):
                os.makedirs("past papers\\" + syllabusName + "\\" + year) #if the directory doesnt exist, create one
            pdf_filename = os.path.join("past papers\\" + syllabusName + "\\" + year, namePdf[1])
            print("Downloading:", pdf_filename)
            
            with open(pdf_filename, 'wb') as pdf_file:
                pdf_response = requests.get(pdf_url)
                pdf_file.write(pdf_response.content)
        self.driver.back()
        pass
    def downloadPapers(self, syllabusName, year, paper, yearIndex, seriesIndex, noSeries): #noSeries is the number of series within a year
        print("Current page: ", self.driver.current_url)
        print(paper)
        papers = WebDriverWait(self.driver, 20).until( 
            EC.presence_of_all_elements_located((By.XPATH, f"//a[contains(@href, 'qp') and contains(@href, '-{paper}')]"))) 
        noofPapers = len(papers)
        for i in range(noofPapers):
            papers = WebDriverWait(self.driver, 10).until( 
            EC.presence_of_all_elements_located((By.XPATH, f"//a[contains(@href, 'qp') and contains(@href, '-{paper}')]"))) 
            papers[i].click()
            self.download(syllabusName, year)
        print(len(papers), " number of zones", seriesIndex, " series", noSeries[yearIndex], " number of series in year")
        for _ in range(1):
            self.driver.back() #return two pages back
        try:
            print("Current URL:", self.driver.current_url)
            seriesIndex += 1
            if seriesIndex >= noSeries[yearIndex]: #checks to see if all series in that year have been exhausted, if yes, go to the next year back
                yearIndex +=1
                seriesIndex = 0 
            return seriesIndex, yearIndex 
        except Exception as e:
            print(e)
            traceback.print_exc
    def accessPapers(self, syllabusCode, paper): #paper is just a number to determine which papers to download (paper 1, paper 2)
        try:
            syllabusName = self.findsyllabusCode(syllabusCode)
            paperYears, paperSeries = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "year"))), WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.year > li > a")))
            numberofSeries = len(paperSeries)
            
            #creates a list of the number of series per year (from most recent to oldest)
            noSeries = [len(i.find_elements(By.XPATH, ".//a")) for i in paperYears] #create a list of the number of series per year
            print(noSeries)
            yearIndex = 0 #which year to hover over
            seriesIndex = 0 #which series has already been processed (generally max 2 as there is usually only summer and winter series)
            
            #iterates through each element with year class
            for j in range(numberofSeries): #loops through each year to download past papers
                paperYears, paperSeries = self.relocateElements() #redefine list of elements so they dont become stale
                i = paperYears[yearIndex] #the link element linking to the page with all the past papers
                print(i.text, yearIndex)
                year = i.text
                self.action.move_to_element(i).perform() #hover over year element in order to uncover exam series
                paperSeries[j] = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((paperSeries[j])))
               
                paperSeries[j].click()
                seriesIndex, yearIndex = self.downloadPapers(syllabusName, year, paper, yearIndex, seriesIndex, noSeries)
           

        except Exception as e:
            print(e)
            traceback.print_exc()
            print("failed to access paper")
            self.driver.quit()
    def relocateElements(self): #when webpage reloads, elements become stale and they get relocated
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "year"))), WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.year > li > a")))
web = webScraper(url)

code = input("enter syllabus code (A level only): ")
paper = input("paper to download: ")
#enter your choice of syllabus and paper from the syllabus and this thing will download every paper from there
web.accessPapers(code, paper)

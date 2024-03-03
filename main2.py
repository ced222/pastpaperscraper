'''FILE THAT RELIES ON MANUAL JSON FILEs'''
from pdfreader import phrasePdf
import os

cwd = os.getcwd()
filePath = cwd + '/past papers/computer Science - 9618/2023/9618_s23_qp_11.pdf'
questions = phrasePdf(filePath)
chapterKw = chapterKeywords()
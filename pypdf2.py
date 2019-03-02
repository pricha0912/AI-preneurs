# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:54:42 2019

@author: Richa Patel


import PyPDF2
object = open ('C:\Python\DataPrap.pdf','rb')
reader = PyPDF2.PdfFileReader(object)
reader.numPages
page = reader.getPage(0)
page.extractText()
page1 = reader.getDocumentInfo()
page2 = reader.getOutlines()
page2

"""



from PyPDF2 import PdfFileReader
 
 
def get_info(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        info = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
 
    #print(info)
 
    author = info.author
    creator = info.creator
    producer = info.producer
    subject = info.subject
    title = info.title
    print("Title of the research paper:")
    print(title)
   
 



 
def text_extractor(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
 
        # get the first page
        page = pdf.getPage(0)
        print(page)
        print('Page type: {}'.format(str(type(page))))
 
        text = page.extractText()
        return text
 
 
if __name__ == '__main__':
    path = 'C:\Python\pdfExtraction.pdf'
    get_info(path)
    
    text = text_extractor(path)
    
    f= open("extractedData1.txt","a+")
    for i in range(len(text)):
        f.write(text)
    f=open("extractedData1.txt", "r")
    if f.mode == 'r':
        contents =f.read()
        print(contents)
        
        
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

text = text

sentence_token = sent_tokenize(text)
first_3 = sentence_token[0:3]
first_3 = str(first_five)

stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(first_3)

filtered_sentence = [w for w in word_tokens if not w in stop_words]


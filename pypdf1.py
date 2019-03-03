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




""" 
#GET AUTHOR NAME    
def find_author(some_text):
    words = some_text.split(" ")
    words = object(words)
    emails = []
    for word in words:
        if "@" in word:
            emails.append(word)
    emails_clean = emails[0].split("\n")
    actual_email = [a for a in emails_clean if "@" in a]
    actual_email = actual_email[0]
    maybe_name = actual_email.split("@")[0]
    all_words_lists = [a.split("\n") for a in words]
    words = [a for sublist in all_words_lists for a in sublist]
    words.remove(actual_email)
    return difflib.get_close_matches(maybe_name, words)



def find_intermediate_chars(text, sub1, sub2):
    pos1 = text.lower().find(sub1) + len(sub1)
    pos2 = text.lower().find(sub2)
    if(pos1 > pos2 and pos2 > 0):
        return text[pos1:pos2]
	elif(pos2 > pos1 and pos1 > 0):
	    return text[pos2:pos1]
	elif(pos1 > 0):
	    return text[pos1:]
	elif(pos2 > 0):
	    return text[pos2:]
    
"""


"""
    abstract = re.findall(r'Abstract\nŠTime(.*?)Keywords\nŠ',text)
    f= open("extractedData1.txt","a+")
    for i in range(len(text)):
        f.write(text)
    f=open("extractedData1.txt", "r")
    if f.mode == 'r':
        contents =f.read()
        print(contents)
    
    re.find('(?<=beginningstringname)(.*\n?)(?=endstringname)',text)
    


with open(r'C:/Python/papers/University_related.pdf','rb') as f:
    extracted_text = slate.PDF(f)
print(extracted_text)
"""


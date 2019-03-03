# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 13:05:10 2019

@author: Richa Patel
"""


  '''
	Filename is a name of a pdf file WITHOUT the extension
	The function will print messages, including the status code,
	and will write the XML file to <filename>.xml
	'''
    


    
import requests

url = "http://pdfx.cs.man.ac.uk"

def pypdfx(filename):
    fin = open(filename + '.pdf', 'rb')
    files = {'file': fin}
    try:
        print ('Sending', filename, 'to', url)
        r = requests.post(url, files=files, headers={'Content-Type':'application/pdf'})
        print ('Got status code', r.status_code)
    finally:
        fin.close()
        t = open(filename + '.xml', 'w')
        t.write(r.content)
        t.close()
        print ('Written to', filename + '.xml')
        
if __name__ == '__main__':
  # self promotion - get the pdf file here: http://onlinelibrary.wiley.com/doi/10.1111/j.1558-5646.2012.01576.x/abstract
	filename = 'paper1'
	pypdfx(filename)
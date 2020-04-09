# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 15:14:50 2020

@author: Arun
"""

'''

Tasks to be done in preprocessing 

1. replace punctuations with a white space
2. convert all the words into either lower or upcase ( no words to be kept duplicate)
3. do word tockenization 
4. remove all stop words 
5. do lemiitization with pos tag 


'''

# lets first import the text on which the processing to be perform. 


import pandas as pd 
import os
 import nltk as nlp
 from nltk.corpus import stopwords

# changing current working dir 
os.chdir(r"C:\Users\Arun\Desktop\NLP")

# To see different files presentunder this dir 
os.listdir()

# Reading input text file 
Input_data=open("Sample.txt").read()

Input_data=Input_data.lower() # This is the second step that I am doing first




#============= First Method to remove punctuations and tockenize ||ly
tokenizer = nlp.RegexpTokenizer(r"[^\d\W]+")

words=tokenizer.tokenize(Input_data)

print(words)




# Lemmatization 
stop_words = set(stopwords.words('english'))


final=[x for x in words if not x in stop_words ] 

print(final)

from nltk.stem import WordNetLemmatizer 
  
lemmatizer = WordNetLemmatizer() 

for x in final: 
    print("Initial:" + x, lemmatizer.lemmatize(x)) 

































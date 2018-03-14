import os
import httplib2
import sys
import numpy as np
import matplotlib.pyplot as plt
import time
import pandas as pd
import string
import statistics
import nltk
import Algorithmia

from nltk import word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import TweetTokenizer
from nltk.probability import FreqDist
from nltk.probability import FreqDist

def getFeatures(comments):
    features = {}
    
    #initialize profanity filter
    client = Algorithmia.client('simlyRpEh3jOufiSoZtvLACnR8p1')
    algo = client.algo('nlp/ProfanityDetection/1.0.0')
    
    #create combined text
    combinedText = ' '.join(comments)
    #find profanity frequency
    profanity = algo.pipe(combinedText).__dict__['result']
    profanitySum = sum(d for d in profanity.values())
    #tokenize
    tokenizer = TweetTokenizer()
    tokens = tokenizer.tokenize(text)
    
    ## WIP ##
    # #convert to nltk Text
    # words = nltk.Text(tokens)
    # #get wordCount
    # wordCount = len(words)
    # features['wordCount'] = wordCount
    # #get frequency distribution
    # fdist = FreqDist(words)
    # #store fdist in dictionary for use in creating combined fdist
    # features['fDist'] = fdist
    # #convert FreqDist to dictionary
    # fdist = dict(fdist)
    # #append FreqDist to features
    # features.update(fdist)
    
    
    
    
    return features


    
    
    
    
    

if __name__ == '__main__':
 
    #iterate through each video file
    for filename in os.listdir(os.getcwd() + '/video_csvs'):
        #obtain video_id
        video_id = filename[:-4]
        print('Processing video: ' + video_id)
        #obtain comment data
        data = pd.read_csv('video_csvs/' + filename)
        #iterate through comments
        comments = []
        for index, d in data.iterrows():
            #append comment
            comments.append(d[0])
        #obtain features
        features = getFeatures(comments)
           
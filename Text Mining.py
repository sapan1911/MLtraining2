# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 11:46:02 2019

@author: esapgup
"""
#importing Libraries
import os
import nltk
import nltk.corpus
# download all available options with nltk library
#nltk.download('all-corpora')
#nltk.download('all')
#nltk.download('punkt')
#nltk.download('all-nltk')

#print available list in corpora
print(os.listdir(nltk.data.find("corpora")))

# Print available txt files in gutenberg
nltk.corpus.gutenberg.fileids()

# Print fisrt few words of story from shakespeare-hemlet
hamlet=nltk.corpus.gutenberg.words('shakespeare-hamlet.txt')
hamlet

# Print fisrt 500 words of story from shakespeare-hemlet
for words in hamlet[:500]:
    print(words,sep=' ',end=' ')


# Creating own story
AI='''There were once two brothers who lived on the edge of a forest. The elder brother was very mean to his younger brother and ate up all the food and took all his good clothes. One day, the elder brother went into the forest to find some firewood to sell in the market. As he went around chopping the branches of a tree after tree, he came upon a magical tree. The tree said to him, ‘Oh kind sir, please do not cut my branches. If you spare me, I will give you my golden apples’. The elder brother agreed but was disappointed with the number apples the tree gave him. Greed overcame him, and he threatened to cut the entire trunk if the tree didn’t give him more apples. The magical tree instead showered upon the elder brother hundreds upon hundreds of tiny needles. The elder brother lay on the ground crying in pain as the sun began to lower down the horizon.'''
type(AI)

# tokenize words in AI (own story stored in AI)
from nltk.tokenize import word_tokenize
AI_tokens=word_tokenize(AI)
AI_tokens
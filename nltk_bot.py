from newspaper import Article
import random
import string
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings
warnings.filterwarnings('ignore')
nltk.download('punkt', quiet=True)


# scrape article content from a given url
# and return a tokenized list of sentences
def get_article(artcle_addr):
  article = Article(artcle_addr)
  article.download()
  article.parse()
  article.nlp()
  corpus = article.text
  text = corpus
  sentence_list = nltk.sent_tokenize(text)
  return sentence_list


# remove question words from query for later comparison
# to text in article content. 
def strip_question(query):
  stopwords = ['what', 'who', 'how', 'why', 'where', 'when', '?']
  querywords = query.split()
  resultwords  = [word for word in querywords if word.lower() not in stopwords]
  result = ' '.join(resultwords)
  return result


# return a list of indexes s
def index_sort(list_in):
  list_length = len(list_in)
  list_indx = list(range(0, list_length))
  x = list_in
  for i in range(list_length):
    for j in range(list_length):
      if x[list_indx[i]] > x[list_indx[j]]:
        temp = list_indx[i]
        list_indx[i] = list_indx[j]
        list_indx[j] = temp 
  return list_indx


def bot_response(query, addr):
  sentencelist = get_article(addr)
  clean_query = strip_question(query)
  sentencelist.append(clean_query)
  response = ''
  cnt_mtx = CountVectorizer().fit_transform(sentencelist)
  similar_weight = cosine_similarity(cnt_mtx[-1],cnt_mtx)
  similar_weight_list = similar_weight.flatten()
  index_list = index_sort(similar_weight_list)
  index_list = index_list[1:5]
  for x in index_list:
    inx = int(x)
    response = response + ' ' + sentencelist[inx]
  return response


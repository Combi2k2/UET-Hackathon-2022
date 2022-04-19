import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

import gensim, logging

model = gensim.models.Word2Vec.load('../models/model_Word2Vec')

job_train = pd.read_csv('/content/jobs.csv')

n_docs = len(set(job_train['job/role']))
w_freq = dict()

for title in set(job_train['job/role']):
    words = str(title.split())

    for w in set(words):
        if (w not in w_freq):
            w_freq[w] = 1
        else:
            w_freq[w] += 1

def Sentence2Vec(sentence):
    words = sentence.split()
    res = np.zeros((2000,))

    for w in words:
        weight = words.count(w) * np.log(len(job_train) / w_freq[w])
        res += weight * model[w]
    
    return  res

def Job2Vec(company_type, title, from_date, to_date, employee_lv, address):
    return  np.concatenate((np.array([company_type, from_date, to_date, address, employee_lv]), Sentence2Vec(title)), axis = 0)
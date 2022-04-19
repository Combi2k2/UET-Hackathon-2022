import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

import random

# Loading Data

train_work = pd.read_csv('../uet-hackathon-2022-data-science/work_train.csv')
test_work = pd.read_csv('../uet-hackathon-2022-data-science/work_test.csv')

# Fill the unfilled values of "job/role" columns by 'NA'

train_work['job/role'].fillna('NA', inplace = True)
test_work['job/role'].fillna('NA', inplace = True)

# Make the title all written in lower alphabet letter
train_work['job/role'] = train_work['job/role'].str.lower()
test_work['job/role'] = test_work['job/role'].str.lower()

# normalize the words
#   -   between 2 words there is only 1 blank space
#   -   there is no special character

char_list = [c for c in ''.join(train_work['job/role'])]  \
          + [c for c in ''.join(test_work['job/role'])]

char_chinh_dao = ['a', 'ă', 'â', 'b', 'c', 'd', 'đ', 'e', 'ê', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ô', 'ơ', 'p', 'q', 'r', 's', 't', 'u', 'ư', 'v', 'w', 'x', 'y', 'z',
                  'á', 'ắ', 'ấ', 'é', 'ế', 'í', 'ó', 'ố', 'ớ', 'ú', 'ứ', 'ý',
                  'à', 'ằ', 'ầ', 'è', 'ề', 'ì', 'ò', 'ồ', 'ờ', 'ù', 'ừ', 'ỳ',
                  'ả', 'ẳ', 'ẩ', 'ẻ', 'ể', 'ỉ', 'ỏ', 'ổ', 'ở', 'ủ', 'ử', 'ỷ',
                  'ạ', 'ặ', 'ậ', 'ẹ', 'ệ', 'ị', 'ọ', 'ộ', 'ợ', 'ụ', 'ự', 'ỵ',
                  'ã', 'ẵ', 'ẫ', 'ẽ', 'ễ', 'ĩ', 'õ', 'ỗ', 'ỡ', 'ũ', 'ữ', 'ỹ',
                  '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                  '(', ')', '-', '+', '&', ':', ';', ' ', '.', ',']

def process(title):
    title = ''.join([c if c in char_chinh_dao else ' ' for c in title]).strip()
    
    words = list(filter(''.__ne__, title.split(' ')))
    title = ' '.join(words)

    return  title

train_work['job/role'] = train_work['job/role'].apply(process)
test_work['job/role']  = test_work['job/role'].apply(process)

jobs_total = pd.concat([train_work['job/role'], test_work['job/role']])
jobs_total.to_csv('jobs.csv')

train_work.to_csv('../uet-hackathon-2022-data-science/work_train.csv')
test_work.to_csv('../uet-hackathon-2022-data-science/work_test.csv')

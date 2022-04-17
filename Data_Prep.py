import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

# Loading Data

train_work = pd.read_csv('uet-hackathon-2022-data-science/work_train.csv')
train_info = pd.read_csv('uet-hackathon-2022-data-science/info_train.csv')

test_work = pd.read_csv('uet-hackathon-2022-data-science/work_test.csv')
test_info = pd.read_csv('uet-hackathon-2022-data-science/info_test.csv')

y_train = pd.read_csv('uet-hackathon-2022-data-science/label_train.csv')

# Fill the unfilled values of "job/role" columns by 'NA'

train_work['job/role'].fillna('NA', inplace = True)
test_work['job/role'].fillna('NA', inplace = True)

# Make the title all written in lower alphabet letter
train_work['job/role'] = train_work['job/role'].str.lower()
test_work['job/role'] = test_work['job/role'].str.lower()

# normalize the words
#   -   between 2 words there is only 1 blank space
#   -   there is no special character

train_work['job/role'] = train_work['job/role'].apply(lambda w: ' '.join(list(filter(''.__ne__, w.split(' ')))))
test_work['job/role']  = test_work['job/role'].apply(lambda w: ' '.join(list(filter(''.__ne__, w.split(' ')))))

char_list = [c for c in ''.join(train_work['job/role'])]  \
          + [c for c in ''.join(test_work['job/role'])]

print(list(set(char_list)))

char_chinh_dao = ['ì', 'ư', '1', 'í', 'ừ', 'ụ', 'ð', ')', \
                  'ặ', '-', 'ứ', ';', '*', 'ấ', 'ù', 'ý', \
                  'z', 'é', 'c', 'ỵ', 'ề', 'r', 'â', 'b', \
                  'd', 'ả', 'à', 'ồ', 'ắ', 'o', 'ê', 'ỗ', \
                  'j', 'ỹ', 'n', ]

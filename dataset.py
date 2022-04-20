from torch.utils.data import Dataset
from torch.utils.data import DataLoader

import torch
import pandas as pd
import numpy as np

from utils.Job2Vec import Job2Vec
from utils.Job2Vec import Info2Vec


def INFO_csv2dict(df, vec_info):
    for i in range(len(df)):
        vec_info[df['id_bh'][i]] = Info2Vec(df['bithYear'][i], df['gender'][i], df['address'][i])

def JOBS_csv2dict(df, vec_jobs):
    for i in range(len(df)):
        idx = df['id_bh'][i]
        vec = Job2Vec(df['company_type'][i], df['job/role'][i], df['from_date'][i], df['to_date'][i], df['employee_lv'][i], df['address'][i])

        if (idx not in vec_jobs):
            vec_jobs[idx] = vec
        else:
            vec_jobs[idx] += vec


class MyDataset(Dataset):
    def __init__(self, df_work, df_info, label):
        super().__init__()

        # convert information of 1 person into vector
        vec_info = dict()
        vec_jobs = dict()

        INFO_csv2dict(df_info, vec_info)
        JOBS_csv2dict(df_work, vec_jobs)

        # adding their informations into training dataset
        self.inputs = []
        self.target = []

        for i in range(len(label)):
            idx = label['id_bh'][i]
            val = label['label'][i]
        
            self.inputs.append(torch.from_numpy(np.concatenate((vec_info[idx], vec_jobs[idx]), axis = 0)))
            self.target.append(val - 1)

        self.n_samples = len(self.inputs)
    
    def __getitem__(self, index):
        inputs = self.inputs[index]
        output = self.target[index]

        return  inputs, output
    
    def __len__(self):
        return  self.n_samples

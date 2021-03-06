from __future__ import print_function, division
import pdb
import unittest
import random
from collections import Counter
import pandas as pd
import numpy as np
from scipy.spatial import distance as dist
from scipy.spatial import distance
from sklearn.neighbors import NearestNeighbors as NN

def get_ngbr(df, knn):
            rand_sample_idx = random.randint(0, df.shape[0] - 1)
            parent_candidate = df.iloc[rand_sample_idx]
            ngbr = knn.kneighbors(parent_candidate.values.reshape(1,-1),3,return_distance=False)
            candidate_1 = df.iloc[ngbr[0][0]]
            candidate_2 = df.iloc[ngbr[0][1]]
            candidate_3 = df.iloc[ngbr[0][2]]
            return parent_candidate,candidate_2,candidate_3

def generate_samples(no_of_samples,df,df_name):
    
    total_data = df.values.tolist()
    knn = NN(n_neighbors=5,algorithm='auto').fit(df)
    
    for _ in range(no_of_samples):
        cr = 0.8
        f = 0.8
        parent_candidate, child_candidate_1, child_candidate_2 = get_ngbr(df, knn)
        new_candidate = []
        for key,value in parent_candidate.items():
            if isinstance(parent_candidate[key], bool):
                new_candidate.append(parent_candidate[key] if cr < random.random() else not parent_candidate[key])
            elif isinstance(parent_candidate[key], str):
                new_candidate.append(random.choice([parent_candidate[key],child_candidate_1[key],child_candidate_2[key]]))
            elif isinstance(parent_candidate[key], list):
                temp_lst = []
                for i, each in enumerate(parent_candidate[key]):
                    temp_lst.append(parent_candidate[key][i] if cr < random.random() else
                                    int(parent_candidate[key][i] +
                                        f * (child_candidate_1[key][i] - child_candidate_2[key][i])))
                new_candidate.append(temp_lst)
            else:
                new_candidate.append(abs(parent_candidate[key] + f * (child_candidate_1[key] - child_candidate_2[key])))        
        total_data.append(new_candidate)
    
    final_df = pd.DataFrame(total_data)
    if df_name == 'Adult':
        final_df = final_df.rename(columns={0:"age", 1:"workclass", 2:"education_num", 3: "marital_status", 4:"occupation", 
        	5:"relationship", 6:"race",7:"sex", 8:"capital_gain", 9:"capital_loss", 10:"hours_per_week", 11:"native_country", 12:"Probability"}, errors="raise")
    if df_name == 'Compas':
        final_df = final_df.rename(columns={0:"sex",1:"age_cat",2:"race",3:"priors_count",4:"c_charge_degree",5:"Probability"}, errors="raise")
    if df_name == 'Default':
    	final_df = final_df.rename(columns={0:"ID",1:"LIMIT_BAL",2:"sex",3:"EDUCATION",4:"MARRIAGE",5:"AGE",6:"PAY_0",7:"PAY_2",8:"PAY_3",9:"PAY_4",10:"PAY_5",11:"PAY_6",12:"BILL_AMT1",13:"BILL_AMT2",14:"BILL_AMT3",15:"BILL_AMT4",16:"BILL_AMT5",17:"BILL_AMT6",18:"PAY_AMT1",19:"PAY_AMT2",20:"PAY_AMT3",21:"PAY_AMT4",22:"PAY_AMT5",23:"PAY_AMT6",24:"Probability"}, errors="raise")
    if df_name == 'German':
        final_df = final_df.rename(columns={0:"credit_history",1:"savings",2:"employment",3:"sex",4:"age",5:"Probability"}, errors="raise")
    if df_name == 'Heart':
    	final_df = final_df.rename(columns={0:"age",1:"sex",2:"cp",3:"trestbps",4:"chol",5:"fbs",6:"restecg",7:"thalach",8:"exang",9:"oldpeak",10:"slope",11:"ca",12:"thal",13:"Probability"}, errors="raise")
    if df_name == 'Bank':
        final_df = final_df.rename(columns={0:"age",1:"default",2:"balance",3:"housing",4:"loan",5:"day",6:"duration",7:"campaign",8:"pdays",9:"previous",10:"Probability"}, errors="raise")
    if df_name == 'Titanic':
        final_df = final_df.rename(columns={0:"Pclass",1:"sex",2:"Age",3:"SibSp",4:"Parch",5:"Fare",6:"Probability"}, errors="raise")
    if df_name == 'Student':
        final_df = final_df.rename(columns={0:'sex', 1:'age', 2:'Medu', 3:'Fedu', 4:'traveltime', 5:'studytime', 6:'failures',
       7:'schoolsup', 8:'famsup', 9:'paid', 10:'activities', 11:'nursery', 12:'higher',
       13:'internet', 14:'romantic', 15:'famrel', 16:'freetime', 17:'goout', 18:'Dalc', 19:'Walc',
       20:'health', 21:'absences', 22:'G1', 23:'G2', 24:'Probability'}, errors="raise")
    if df_name == 'MEPS16':
        final_df =final_df.rename(columns={0: 'REGION',
 1: 'AGE',
 2: 'SEX',
 3: 'race',
 4: 'MARRY',
 5: 'FTSTU',
 6: 'ACTDTY',
 7: 'HONRDC',
 8: 'RTHLTH',
 9: 'MNHLTH',
 10: 'HIBPDX',
 11: 'CHDDX',
 12: 'ANGIDX',
 13: 'MIDX',
 14: 'OHRTDX',
 15: 'STRKDX',
 16: 'EMPHDX',
 17: 'CHBRON',
 18: 'CHOLDX',
 19: 'CANCERDX',
 20: 'DIABDX',
 21: 'JTPAIN',
 22: 'ARTHDX',
 23: 'ARTHTYPE',
 24: 'ASTHDX',
 25: 'ADHDADDX',
 26: 'PREGNT',
 27: 'WLKLIM',
 28: 'ACTLIM',
 29: 'SOCLIM',
 30: 'COGLIM',
 31: 'DFHEAR42',
 32: 'DFSEE42',
 33: 'ADSMOK42',
 34: 'PCS42',
 35: 'MCS42',
 36: 'K6SUM42',
 37: 'PHQ242',
 38: 'EMPST',
 39: 'POVCAT',
 40: 'INSCOV',
 41: 'Probability',
 42: 'PERWT16F'},errors='raise')
    if df_name == 'MEPS':
        final_df =final_df.rename(columns={0: 'REGION',
 1: 'AGE',
 2: 'SEX',
 3: 'race',
 4: 'MARRY',
 5: 'FTSTU',
 6: 'ACTDTY',
 7: 'HONRDC',
 8: 'RTHLTH',
 9: 'MNHLTH',
 10: 'HIBPDX',
 11: 'CHDDX',
 12: 'ANGIDX',
 13: 'MIDX',
 14: 'OHRTDX',
 15: 'STRKDX',
 16: 'EMPHDX',
 17: 'CHBRON',
 18: 'CHOLDX',
 19: 'CANCERDX',
 20: 'DIABDX',
 21: 'JTPAIN',
 22: 'ARTHDX',
 23: 'ARTHTYPE',
 24: 'ASTHDX',
 25: 'ADHDADDX',
 26: 'PREGNT',
 27: 'WLKLIM',
 28: 'ACTLIM',
 29: 'SOCLIM',
 30: 'COGLIM',
 31: 'DFHEAR42',
 32: 'DFSEE42',
 33: 'ADSMOK42',
 34: 'PCS42',
 35: 'MCS42',
 36: 'K6SUM42',
 37: 'PHQ242',
 38: 'EMPST',
 39: 'POVCAT',
 40: 'INSCOV',
 41: 'Probability',
 42: 'PERWT15F'}, errors="raise")

    return final_df
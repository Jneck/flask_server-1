import os
from tqdm import tqdm
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from scipy.sparse import csr_matrix
import json
from sklearn.metrics.pairwise import cosine_similarity
import csv
import json

def user_similarity(data):

    dic_list = data['Results']

    member_id = str(data['member_id'])

    d_list = []
    for row in dic_list:
        d_list.append([row['member_id'], row['feed_id'], row['click_count']])

    click_df = pd.DataFrame(d_list, columns=['member_id', 'feed_id', 'click_count'])

    title_user = click_df.pivot_table('click_count', index='member_id',columns='feed_id')
    title_user.fillna(0, inplace=True)

    # 유저와 유저 간의 유사도
    user_based_collab = cosine_similarity(title_user, title_user)
    user_based_collab = pd.DataFrame(user_based_collab, index=title_user.index, columns=title_user.index)


    tmplist=[]
    if 11 > len(user_based_collab.index):
        tmplist = user_based_collab[member_id].sort_values(ascending=False)[1:].index

    else:
        tmplist = user_based_collab[member_id].sort_values(ascending=False)[1:11].index

    similarlist = []
    for s in tmplist:
        similarlist.append(str(s))
    return similarlist




import numpy as np
import pandas as pd

#xy좌표를 원본 비율로 변환
def origin_rate(df):
    df_xy = df[[(a,b) for a,b in df.columns if b in ('x', 'y')]]
    df_xy.loc[:, (slice(None), 'x')] = df_xy.loc[:, (slice(None), 'x')].apply(lambda x : x*640)
    df_xy.loc[:, (slice(None), 'y')] = df_xy.loc[:, (slice(None), 'y')].apply(lambda x : x*720)

    return df_xy

#boundingbox & perspectivetransform 을 적용한 효과
def box_perspective(df_xy):
    for idx in range(len(df_xy)):
        x_min = df_xy.loc[idx, (slice(None), 'x')].min()
        x_max = df_xy.loc[idx, (slice(None), 'x')].max()
        y_min = df_xy.loc[idx, (slice(None), 'y')].min()
        y_max = df_xy.loc[idx, (slice(None), 'y')].max()
        
        if x_max != 0 and y_max != 0:
            x_rate = 640/((x_max+20)-(x_min-20))
            y_rate = 720/((y_max+20)-(y_min-20))

            df_xy.loc[idx, (slice(None), 'x')] = df_xy.loc[idx, (slice(None), 'x')].apply(lambda x : ((x-(x_min-20))*x_rate)/640)
            df_xy.loc[idx, (slice(None), 'y')] = df_xy.loc[idx, (slice(None), 'y')].apply(lambda x : ((x-(y_min-20))*y_rate)/720)
        
    return df_xy

#관절들을 벡터로 변환, 노멀라이즈
def vector_transform(joint):
    vector1 = joint[[13, 23, 14, 24, 15, 16, 17, 19, 21, 18, 20, 22, 25, 26, 27, 28, 29, 31, 30, 32], :]
    vector2 = joint[[11, 11, 12, 12, 13, 14, 15, 15, 15, 16, 16, 16, 23, 24, 25, 26, 27, 27, 28, 28], :]   
    vector = vector2 - vector1  
    
    vector = vector / np.linalg.norm(vector, axis=1)[:, np.newaxis]
    
    return vector

#점수 구하는 공식
def euclid_distance(train, test):
    euclid_list = []

    if not np.isnan(train).any() and np.isnan(test).any():
        return 0

    for x, y in zip(train, test):
        cossim = np.dot(x, y) / (np.linalg.norm(x)*np.linalg.norm(y))
        euc_d = np.sqrt(2*(1-cossim))
        score = 100 - (100 * (euc_d)/2)
        euclid_list.append(score)

    return np.nanmean(euclid_list)

def euclid_score(train, test):
    test = origin_rate(test)
    test = box_perspective(test)
    score_list=[]

    for idx in range(min(train.shape[0],test.shape[0])):
        train_v = train[idx]
        test_joint = test.iloc[idx].values.reshape(33,2)
        test_v = vector_transform(test_joint)
        score = euclid_distance(train_v, test_v)        
        score_list.append(score)

    score = np.nanmean(score_list)
    if score >= 75:
        score = 100
    elif score <= 40:
        score = 30
    elif score <=65 and score >40:
        score = (0.8*score-40)/(75-40)*(100-30)+30
    else:
        score = (score-40)/(75-40)*(100-30)+30
        
    return round(score)
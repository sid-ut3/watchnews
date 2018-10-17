#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 15:25:16 2018

@author: AntoineP
"""

import os
import pandas as pd
import pickle
import numpy as np
import lightgbm as lgb
from sklearn.metrics import accuracy_score



xtrain, xtest, ytrain, ytest = pickle.load(open('../../../train_test_data_group7', 'rb'))

#
#clf = pickle.load(open('../../../Models/CLF_LGBM', 'rb'))
#clf.predict(xtest)
#predicted = clf.predict(xtest).argmax(1)
#print('Accuracy score : %s' % accuracy_score(ytest, predicted))
#
#
#
#clf = pickle.load(open('../../../Models/CLF_SVM', 'rb'))
#clf.predict(xtest)
#predicted = clf.predict(xtest).argmax(1)
#print('Accuracy score : %s' % accuracy_score(ytest, predicted))

#####
#Juste avec les prédictions
####
xtrain_meta = pd.DataFrame()
xtest_meta = pd.DataFrame()

#####
#TF-IDF + predictions
#####
xtrain_meta = pd.DataFrame(xtrain)
xtest_meta = pd.DataFrame(xtest)



#elem = "output.pkl"
path = "../../../Models/"
listModels = os.listdir(path)
for elem in listModels:
    if elem!='.DS_Store':
        if elem == 'CLF_LGBM':
            model = pickle.load(open(path+elem,'rb'))
            x = model.predict(xtrain).argmax(1)
            z = [elem for elem in x]
            xtrain_meta[elem] = z
            x = model.predict(xtest).argmax(1)
            z = [elem for elem in x]
            xtest_meta[elem] = z
        else:
            model = pickle.load(open(path+elem,'rb'))
            x = model.predict(xtrain)
            z = [elem for elem in x]
            xtrain_meta[elem] = z
            x = model.predict(xtest)
            z = [elem for elem in x]
            xtest_meta[elem] = z
                
            






lgb_train = lgb.Dataset(xtrain_meta, ytrain)
lgb_eval = lgb.Dataset(xtest_meta, ytest, reference=lgb_train)



# Recode our output


best= {'bagging_fraction': 0.95,
 'feature_fraction': 1.0,
 'num_leaves': 100,
 'reg_alpha': 0.5,
 'metric': 'multi_error',
 'application': 'multiclass',
 'learning_rate': [0.1], 
 'bagging_seed': 1,
 'feature_fraction_seed': 2, 
 'num_class': 7}


gbm = lgb.train(best,
                lgb_train,
                num_boost_round=100,
                valid_sets=lgb_eval,
                early_stopping_rounds=1000)

#pickle.dump(gbm,open('../../../Models/CLF_LGBM', 'wb'))
predicted = gbm.predict(xtest)
predicted = predicted.argmax(1) #Proba to selected label

print('Accuracy score : %s' % accuracy_score(ytest, predicted))
print('Confusion matrix :\n%s' % confusion_matrix(ytest, predicted))
print(metrics.classification_report(ytest, predicted, target_names=labels))

#import xgboost as xgb
#gbm = xgb.XGBClassifier(
#    #learning_rate = 0.02,
# n_estimators= 2000,
# max_depth= 4,
# min_child_weight= 2,
# #gamma=1,
# gamma=0.9,                        
# subsample=0.8,
# colsample_bytree=0.8,
# objective= 'binary:logistic',
# nthread= -1,
# scale_pos_weight=1)
#gbm.fit(x_train, y_train)
#predictions = gbm.predict(x_test)




from sklearn.ensemble import RandomForestClassifier, VotingClassifier

from sklearn.preprocessing import OneHotEncoder

 
def to_dummy(dataset,colname) :
    # Attention au trap, on drop une dummy
    onehot = pd.get_dummies(dataset[colname], drop_first = True)
    onehot = onehot.rename(columns=lambda x: colname + '_' + str(x))
    dataset = dataset.join(onehot)    
    return dataset

for i in range(len(xtrain_meta.columns)):
    xtrain_meta = to_dummy(xtrain_meta, xtrain_meta.columns[i])
    

for i in range(len(xtest_meta.columns)):
    xtest_meta = to_dummy(xtest_meta, xtest_meta.columns[i])








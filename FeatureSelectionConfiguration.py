#!/usr/bin/env python
# coding: utf-8

# In[2]:


from configparser import ConfigParser #Get the configparser object
config_object = ConfigParser() 

'''max_df:float or int, default=1.0
    When building the vocabulary ignore terms that have a document frequency strictly higher than the given threshold (corpus-specific stop words). If float in range [0.0, 1.0], the parameter represents a proportion of documents, integer absolute counts. This parameter is ignored if vocabulary is not None.

min_df:float or int, default=1
    When building the vocabulary ignore terms that have a document frequency strictly lower than the given threshold. This value is also called cut-off in the literature. If float in range of [0.0, 1.0], the parameter represents a proportion of documents, integer absolute counts. This parameter is ignored if vocabulary is not None.

max_features:int, default=None
    If not None, build a vocabulary that only consider the top max_features ordered by term frequency across the corpus.
    This parameter is ignored if vocabulary is not None.
'''

config_object['FeatureSelection'] = {"raw_data" : 'IMDBtrainProcessed.csv',
                                     "pearson_correlation" : True,
                                     "chi_square_correlation" : True,
                                     "recursive_feature_elimination" : True,
                                     "lasso_regression" : True,
                                     "random_forest_classifier" : True,
                                     "odds_ratio" : True,
                                     "number_of_features" : 100,
                                     "idf_weighing" : False,
                                     "n_gram_range" : (1,2),
                                     "max_df" : 500,
                                     "min_df" : 100,
                                     "max_features" : 2000}

#Write the above sections to feature_selection.ini file
with open('feature_selection.ini', 'w') as config_file:
    config_object.write(config_file)


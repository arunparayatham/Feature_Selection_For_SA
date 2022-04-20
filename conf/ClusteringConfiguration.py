#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# ------------ CLUSTERING CONFIGURATION ------------

from configparser import ConfigParser #Get the configparser object
config_object = ConfigParser() 

config_object['Clustering'] ={"input_data_path" : '../results/PreProcessing_Results/',
                              "feature_data_path" : '../results/FeatureSelection_Results/',
                              "output_data_path" : '../results/Clustering_Results/',
                              "data_filename" : '_PreProcessed.csv',
                              "feature_filename" : 'pearson_features.csv',
                              "clustering_results_dir" : 'Clustering_Results',
                              "no_of_clusters" : 10,
                              "feature_column_numbers" : [2]
                             }

#Write the above sections to clustering.ini file
with open('../conf/clustering.ini', 'w') as config_file:
    config_object.write(config_file)



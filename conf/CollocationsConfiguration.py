#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# ------------ COLLOCATIONS CONFIGURATION ------------

from configparser import ConfigParser #Get the configparser object
config_object = ConfigParser() 

config_object['Collocations'] ={"input_filename" : 'IMDBtrain.csv',
                                "input_data_path" : '../data/',
                                "output_data_path" : '../results/Collocations_Results/',
                                "encoding":'latin',
                                "ngram_results_dir":'Ngram_Results',
                                "pmi_results_dir":'PMI_Results',
                                "PMI_threshold":'0'}

#Write the above sections to collocations.ini file
with open('../conf/collocations.ini', 'w') as config_file:
    config_object.write(config_file)


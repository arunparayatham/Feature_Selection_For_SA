from configparser import ConfigParser
#Get the configparser object
config_object = ConfigParser()
#Assume we need 2 sections in the config file, let's call them USERINFO and SERVERCONFIG



config_object['Data'] = {
    "data": "IMDBtrainProcessed.csv",
    "negation_handling":True,
    "remove_punctuation":True,
    "numbers_to_names":False,
    "stop_words_removal":True,
    "lemmatization":True,
    "number_removal":True,
    "convert_to_lowercase":True,
    "tokenization":False,
    "gibberish_word_removal":True}

#Write the above sections to preprocessing.ini file
with open('PreProcess.ini', 'w') as conf:
    config_object.write(conf)
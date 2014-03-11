from Fetcher import Fetcher
from bs4 import BeautifulSoup as BS
import re

import sys
sys.path.append('../')

import jieba
jieba.load_userdict("usrDict.txt")
import jieba.analyse
jieba.analyse.load_stop_words("stop_words_list.txt")


jieba.analyse.get_idf("corpse.txt")
content = open("corpse.txt","r").read()
tags = jieba.analyse.extract_tags(content, topK=10)

print ",".join(tags)



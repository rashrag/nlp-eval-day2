'''
feature_functions.py
Implements the feature generation mechanism
Author: Anantharaman Narayana Iyer
Date: 21 Nov 2014
6th Dec: Org gazeteer added
7th Dec: 
'''
from nltk import sent_tokenize, word_tokenize
import nltk
import json
import numpy
import pickle
import datetime
import ner_client

phones = ["phone", "phones", "smartphone", "smartphones", "mobile", "tablet", "tablets", "phablet", "phablets"]
org_list = ['Samsung', 'Apple', 'Microsoft', 'Nokia', 'Sony', 'LG', 'HTC', 'Motorola', 'Huawei', 'Lenovo', 'Xiaomi', 'Acer', 'Asus', 'BlackBerry',
            'Alcatel', 'ZTE', 'Toshiba', 'Vodafone', 'T-Mobile', 'Gigabyte', 'Pantech', 'XOLO', 'Lava', 'Micromax', 'BLU', 'Spice', 'Prestigio',
            'verykool', 'Maxwest', 'Celkon', 'Gionee', 'vivo', 'NIU', 'Yezz', 'Parla', 'Plum']
org_list1 = [m.lower() for m in org_list]
os_list = ["iOS", "Android", "Windows", "Symbian", "Bada", "Unix", "Linux", "Ubuntu", "OS", "RIM", "Firefox"]
os_list1 = [m.lower() for m in os_list]
currency_symbols = ["rs", "inr", "$", "usd", "cents", "rupees"]
size_list = ["inch", "cm", "inches", "cms", r'"', "''", "pixel", "px", "mega", "gb", "mb", "kb", "kilo", "giga", "mega-pixel" ]
price_list=["cost","price","charge","fee","terms","payment","rate","fare","levy","toll","amount","sum","total","figure","expensive","cheap","cheaper","cheapest"];
worth, (monetary) value;
outlay, expense, expenses, expenditure, bill;
valuation, quotation, estimate;
informaldamage]
brand_product_bigrams_dict = [] # use the web service from Ner_client to get this: ner.get_brand_product_bigrams() # gazeteer based 7th Dec 2014
product_names = []
client = ner_client.NerClient("1PI11CS137", "g11")

for v in client.get_brand_product_bigrams_dict().values():
    for v1 in v:
        product_names.append(v1.lower())

product_name_tokens = [] # some time product names may be strings with many words, we will split these so that we can compare it with input word token
for p in product_names:
    product_name_tokens.extend(p.split())


class FeatureFunctions(object):
    def __init__(self, tag_list = None):
        self.flist = {} #[self.f1, self.f2, self.f3, self.f4, self.f5, self.f6, self.f7, self.f8, self.f9, self.f10, self.f11, self.f12, self.f13]
        self.fdict = {}
        for k, v in FeatureFunctions.__dict__.items():
            if hasattr(v, "__call__"):
                if k[0] == 'f':
                    self.flist[k] = v # .append(v)
                    tag = k[1:].split("_")[0]
                    val = self.fdict.get(tag, [])
                    val.append(v)
                    self.fdict[tag] = val
        self.supported_tags = self.fdict.keys()        
        return

    def fPrice_1(self,wordlist,taglist,entities,relation):
        if relation[0] != "price_query":
            return 0
	synpres=[i for i in wordlist if i in price_list]
        if(!synpres):
	    return 0
        else:
	    return 1
        return 0

	if("price" not in taglist):
	    return 0        
	comparelist=["less","greater","than","for"]
        if([i for i in wordlist if i in comparelist]):
	   self.check=true
	   return 1
	else:
	   return 0
	return 0

    def fPrice_2(self,wordlist,taglist,entities,relation):
	 if relation[0] != "price_query":
            return 0       
	if("price" not in taglist):
	    return 0        
        preceed_word=wordlist[taglist.index("price")];
        comparelist=["less","greater","than","lesser","greater","under","above"]
        if(preceed_word in comparelist):
	   self.check=true
	   return 1
	else:
	   return 0
	return 0

    def ffeature_1(self,wordlist,taglist,entities,relation):
        if tag != "feature_query":
            return 0
        comparelist=["has","have","run","compare","contains"]
        if([i for i in wordlist if i in comparelist]):
	   self.check=true
	   return 1
	else:
	   return 0
	return 0

	

    def ffeature_2(self,wordlist,taglist,entities,relation):
        if tag != "feature_query":
            return 0
        if("feature" in taglist):
	    nexttag=taglist[taglist.index("feature")+1];
            if(nexttag=="feature"):
                self.check=true 
		return 1
            else:
		return 0
	else:
	    return 0
        return 0

   def ffeature_3(self,wordlist,taglist,entities,relation):
        if tag != "feature_query":
            return 0
        if("want" in wordlist):
	    return 0
	else:
	    return 1
	return 0
   
   def fIrrelevant_1(self,wordlist,taglist,entities,relation):
	 if tag != "Irrelevant":
	    return 0
	 if("when" in wordlist):
	    return 1
	 else:
	    return 0
	 return 0

   def fIrrelevant_2(self,wordlist,taglist,entities,relation):
	 if tag != "Irrelevant":
	    return 0
	 if("where" in wordlist):
	    return 1
	 else:
	    return 0
	 return 0

    def fIrrelevant_3(self,wordlist,taglist,entities,relation):
	 if tag != "Irrelevant":
	    return 0
	 if(taglist.count("Other") >= len(taglist)/2):
	    return 1
	 else:
	    return 0
	 return 0


    def evaluate(self, xi, tag):
        feats = []
        for t, f in self.fdict.items():
            if t == tag:
                for f1 in f:
                    feats.append(int(f1(self, xi, tag)))
            else:
                for f1 in f:
                    feats.append(0)
        return feats

	
  
    #------------------------------- Functions for Org tag ---------------------------------------------------------
    #------------------------------- Functions for Family tag ---------------------------------------------------------  
    #------------------------------- Functions for OS tag ---------------------------------------------------------        
    #------------------------------- Functions for Version tag ---------------------------------------------------------
    #------------------------------- Functions for Other tag ---------------------------------------------------------
    #------------------------------- Functions for Price tag ---------------------------------------------------------  
    #------------------------------- Functions for Size tag ---------------------------------------------------------  
    #------------------------------- Functions for Feature tag ---------------------------------------------------------  


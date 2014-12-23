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
import ner_client
import numpy
import pickle
import datetime
import re

phones = ["phone", "phones", "smartphone", "smartphones", "mobile", "tablet", "tablets", "phablet", "phablets"]
org_list = ['Samsung', 'Apple', 'Microsoft', 'Nokia', 'Sony', 'LG', 'HTC', 'Motorola', 'Huawei', 'Lenovo', 'Xiaomi', 'Acer', 'Asus', 'BlackBerry',
            'Alcatel', 'ZTE', 'Toshiba', 'Vodafone', 'T-Mobile', 'Gigabyte', 'Pantech', 'XOLO', 'Lava', 'Micromax', 'BLU', 'Spice', 'Prestigio',
            'verykool', 'Maxwest', 'Celkon', 'Gionee', 'vivo', 'NIU', 'Yezz', 'Parla', 'Plum']
org_list1 = [m.lower() for m in org_list]
os_list = ["iOS", "Android", "Windows", "Symbian", "Bada", "Unix", "Linux", "Ubuntu", "OS", "RIM", "Firefox"]
os_list1 = [m.lower() for m in os_list]
currency_symbols = ["rs", "inr", "$", "usd", "cents", "rupees"]
size_list = ["inch", "cm", "inches", "cms", r'"', "''", "pixel", "px", "mega", "gb", "mb", "kb", "kilo", "giga", "mega-pixel" ]

class FeatureFunctions(object):
    def __init__(self, tag_list = None):
        self.wmap = {}
        self.flist = {} #[self.f1, self.f2, self.f3, self.f4, self.f5, self.f6, self.f7, self.f8, self.f9, self.f10, self.f11, self.f12, self.f13]
        self.fdict = {}
        self.check = False
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

    def set_wmap(self, sents): # given a list of words sets wmap
        for i in range(len(sents)):
            self.wmap[i] = {'words': sents[i], 'pos_tags': nltk.pos_tag(sents[i])}
        return

    def check_list(self, clist, w):
        #return 0
        w1 = w.lower()
        for cl in clist:
            if w1 in cl:
                return 1
        return 0

    
    def fPhone_1(self, h, tag):
        if tag != "Phone":
            return 0
        words = self.wmap[h["wn"]]['words']        
        if (words[h["i"]].lower() in phones):
	    self.check = True
            return 1
        else:
            return 0
        return 0
    #Preceded by Org
    def fPhone_2(self, h, tag):
	if tag != "Phone":
		return 0
	words = self.wmap[h["wn"]]['words']
	if (h['tb'])== "Org":
	    self.check = True
            return 1
	else:
	    return 0
	return 0

    #Preceded by Version
    def fPhone_3(self, h, tag):
	if tag != "Phone":
		return 0
	words = self.wmap[h["wn"]]['words']
	if (h['tb'])== "Version":
            self.check = True
            return 1
	else:
	    return 0
	return 0
    #Preceded by Family
    def fPhone_4(self, h, tag):
	if tag != "Phone":
		return 0
	words = self.wmap[h["wn"]]['words']
	if (h['tb'])== "Family":
            self.check = True
            return 1
	else:
            return 0
        return 0
   
    def fPhone_5(self, h, tag):
	if tag != "Phone":
		return 0
	words = self.wmap[h["wn"]]['words']
	if( [h["i"]+1] < len(words)):
		if(words[h['i']+1]=="with"):
			return 1
		else:
			return 0
	return 0

    def fPhone_6(self, h, tag):
	if tag != "Phone":
		return 0
	words = self.wmap[h["wn"]]['words']
	if( [h["i"]+1] < len(words)):
		if(words[h['i']+1]=="between"):
			return 1
		else:
			return 0
	return 0
    def fOrg_1(self, h, tag):
        if tag != "Org":
            return 0
        words = self.wmap[h["wn"]]['words']        
        if (words[h["i"]].lower() in org_list1):
            self.check = True
            return 1
        else:
            return 0
        return 0

    def fOrg_2(self, h, tag):
        if tag != "Org":
            return 0
        words = self.wmap[h["wn"]]['words']        
        if (words[h["i"]].lower() in org_list1):
            index = h["i"]+ 1
            if(index < len(words)):
                if(words[h["i"]+ 1].lower() in phones):
                    self.check = True
                    return 1
        else:
            return 0
        return 0
    def fOrg_3(self, h ,tag): #low
        if tag != "Org":
            return 0
        words = self.wmap[h["wn"]]['words']
        index = h["i"] - 1
        if(index > 0):
            if(words[h["i"] - 1 ].lower() == "from"):
                if(words[h["i"]].lower() in org_list1):
                    self.check = True
                    return 1
        else:
            return 0
        return 0

    def fOrg_4(self, h, tag): #low
        if tag != "Org":
            return 0
        words = self.wmap[h["wn"]]['words']
        index = h["i"] - 1
        if(index > 0):
            if(words[h["i"] - 1 ].lower() == "by"):
                if(words[h["i"]].lower() in org_list1):
                    self.check = True
                    return 1
        else:
            return 0
        return 0
    def fOrg_5(self, h, tag): #low
        if tag != "Org":
            return 0
        words = self.wmap[h["wn"]]['words']
        index = h["i"] - 1
        if(index > 0):
            if(words[h["i"] - 1 ].lower().startswith('wh')):
                if(words[h["i"]].lower() in org_list1):
                    self.check = True
                    return 1
        else:
            return 0
        return 0

    def fOS_1(self, h, tag):
        if tag != "OS":
            return 0
        words = self.wmap[h["wn"]]['words']
        if( words[h["i"]].lower() in os_list1):
            self.check = True
            return 1
        else:
            return 0
        return 0
    def fOS_2(self, h, tag):
        if tag != "OS":
            return 0
        words = self.wmap[h["wn"]]['words']
        index = h["i"] + 1
        if(index < len(words)):
            if( words[h["i"]].lower() in os_list1 and words[h["i"]+ 1 ].lower() in phones):
                self.check = True
                return 1
            else:
                return 0
        return 0
    def fOS_3(self, h, tag): #low
        if tag != "OS":
            return 0
        words = self.wmap[h["wn"]]['words']
        index = h["i"] - 2
        if (index > 0):
            if( words[h["i"] - 2 ].lower() == "supported"   and words[h["i"]].lower() in os_list1):
                self.check = True
                return 1
        else:
            return 0
        return 0
    def fOS_4(self, h, tag): #low
        if tag != "OS":
            return 0
        words = self.wmap[h["wn"]]['words']
        index = h["i"] - 2
        if(index > 0):
            if( words[h["i"] - 2].lower() == "run" and  words[h["i"]].lower() in os_list1):
                self.check = True
                return 1
        else:
            return 0
        return 0
        
    def fOS_5(self, h, tag):
        if tag != "OS":
            return 0
        words = self.wmap[h["wn"]]['words']
        tags = self.wmap[h["wn"]]['pos_tags']
        if( words[h["i"]].lower() in os_list1):
            if(((h["i"] + 1 ) > len(words)) and tags[h["i"] + 1] == "CD"):
                self.check = True
                return 1
        else:
            return 0
        return 0

    def fPrice_1(self, h, tag): 
        if tag != "Price":
            return 0
        words = self.wmap[h["wn"]]['words']
	tags = self.wmap[h["wn"]]['pos_tags']
        if( words[h["i"]].lower().endswith('k')):
		if(tags[h["i"]]=='CD'):
            		self.check = True
            		return 1
		else:
			return 0
        else:
            return 0
        return 0

    def fPrice_2(self, h, tag): 
        if tag != "Price":
            return 0
        words = self.wmap[h["wn"]]['words']
	tags = self.wmap[h["wn"]]['pos_tags']
        if( words[h["i"]].lower().endswith('usd')):
		if(tags[h["i"]]=="JJ"):
        		self.check = True
        		return 1
        else:
            return 0
        return 0

    def fPrice_3(self, h, tag): 
        if tag != "Price":
            return 0
        words = self.wmap[h["wn"]]['words']
        tags = self.wmap[h["wn"]]['pos_tags']
        if( tags[h["i"]] == "CD"):
            if(len(words[h["i"]]) > 4):
                self.check = True
                return 1
        else:
            return 0
        return 0

    def fPrice_4(self, h, tag): 
        if tag != "Price":
            return 0
        words = self.wmap[h["wn"]]['words']
        if( "," in words[h["i"]].lower()):
            self.check = True
            return 1
        else:
            return 0
        return 0

    def fPrice_5(self, h, tag): 
        if tag != "Price":
            return 0
        words = self.wmap[h["wn"]]['words']
        if( words[h["i"]].lower() in currency_symbols):
            self.check = True
            return 1
        else:
            return 0
        return 0

    def fPrice_6(self, h, tag): 
        if tag != "Price":
            return 0
        words = self.wmap[h["wn"]]['words']
        tags = self.wmap[h["wn"]]['pos_tags']
        if( h["tb"] == "Price"):
            if(tags[h["i"]] == "CD"):
                self.check = True
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


#Preceded by family and starts with capital letter
    def fVersion_1(self, h, tag):
	if tag != "Version":
		return 0
	words = self.wmap[h["wn"]]['words']
	if (h['tb'])== "Family":
            self.check = True
	    return 1
	    if((words[h['i']][0]).isupper()):
                self.check = True
		return 1
            else:
		return 0
	else:
		return 0
	return 0


    #preceded by os or version
    def fVersion_2(self, h, tag):
	 if tag != "Version":
		return 0
	 words = self.wmap[h["wn"]]['words']
	 if (h['tb'] == "OS" or h['tb'] == "Version"):
             self.check = True
             return 1
	 else:
             return 0
         return 0

    # OS version version
    def fVersion_3(self, h, tag):
        if tag != "Version":
            return 0
        words = self.wmap[h["wn"]]['words']
        if (h['ta'] == "OS" or h['tb'] == "Version"):
            self.check = True
            return 1
        else:
            return 0
        return 0


    # preceded by family(model)
    def fVersion_4(self, h, tag):
	if tag != "Version":
		return 0
	words = self.wmap[h["wn"]]['words']
	if ( h['tb'] == "Family"):
	        self.check = True
		return 1
	else:
		return 0
	return 0




    #org,family,version
    def fVersion_5(self, h, tag):
	if tag != "Version":
		return 0
	words = self.wmap[h["wn"]]['words']
	if (h['ta'] == "Org" and h['tb'] == "Family"):
	        self.check = True
		return 1
	else:
		return 0
	return 0

    #version version - second version is text
    def fVersion_6(self, h, tag):
	if tag != "Version":
		return 0
	words = self.wmap[h["wn"]]['words']
	if (h['tb'] == "Version" and words[h['i']].isalpha() ):
	        self.check = True
		return 1
	else:
		return 0
	return 0

    #	version is a string and preceeded text is "android"
    def fVersion_7(self, h, tag):
	if tag != "Version":
		return 0
	words = self.wmap[h["wn"]]['words']
	if (words[h['i']].isalpha and ((h["i"] - 1) > 0) and (words[h['i']-1]=="Android" or words[h['i']-1]=="android")):
	        self.check = True
		return 1
	else:
		return 0
	return 0

    #version preceeded with word "with" - eg with "lolipop"
    def fVersion_8(self, h, tag):
	if tag != "Version":
		return 0
	words = self.wmap[h["wn"]]['words']
	if((h["i"] - 1) >0):
            if (words[h['i']-1]=="with"):
                self.check = True
		return 1
	else:
		return 0
	return 0

    #"upgradable" in w-1 or w-2 and w is a version
    def fVersion_9(self, h, tag):
	if tag != "Version":
		return 0
	words = self.wmap[h["wn"]]['words']
	if(h["i"]-1 > 0 and h["i"] - 2 > 0):
            if (words[h['i']-1]=="upgradable" or words[h['i']-2]=="upgradable"):
                self.check = True
		return 1
	else:
		return 0
	return 0

    #next word is "update"
    def fVersion_10(self, h, tag):
	if tag != "Version":
		return 0
	words = self.wmap[h["wn"]]['words']
	if (h["i"] + 1 < len(words)):
		if (words[h['i']+1] == "update"):
	                self.check = True
			return 1
		else:
			return 0
	return 0


    #Preceded by org and starts with capital letter 
    def fFamily_1(self, h, tag):
	if tag != "Family":
		return 0
	words = self.wmap[h["wn"]]['words']
	if (h['tb'] == "Org" and words[h['i']][0].isupper()):
	        self.check = True
		return 1
	else:
		return 0
	return 0

    #followed by numbers  
    def fFamily_2(self, h, tag):
	if tag != "Family":
		return 0
	words = self.wmap[h["wn"]]['words']
	if ((h["i"] + 1) < len(words)):
		if (words[h['i']+1].isdigit()):
	                self.check = True
			return 1
		else:
			return 0
	return 0

    #followed by word with capital letter or combination of letters and numbers
    def fFamily_3(self, h, tag):
	if tag != "Family":
		return 0
	words = self.wmap[h["wn"]]['words']
	pat = "[a-z]*.*[0-9]*"
	sub = words[h['i']]
	if (((h["i"] + 1) < len(words) )and words[h['i']+1][0].isupper() or re.search(pat,sub)):
	        self.check = True
		return 1
	else:
		return 0
	return 0
    #Family followed by [phone or others in list]
    def fFamily_4(self, h, tag):
	if tag != "Family":
		return 0
	words = self.wmap[h["wn"]]['words']
	if(h["i"] + 1 < len(words)):
            next_word = words[h['i']+1]
            if (next_word in phones):
                self.check = True
		return 1
	else:
		return 0
	return 0

    #followed by number in texts (one - 1)
    def fFamily_5(self, h, tag):
	if tag != "Family":
		return 0
	words = self.wmap[h["wn"]]['words']
	tags = self.wmap[h["wn"]]['pos_tags']
	if(h["i"] + 1 <len(words)):
            next_word = h['i']+1
            if (tags[next_word]=='CD'):
	        self.check = True
		return 1
	else:
		return 0
	return 0

    #if t-2 = phone and previous word is "with" or "has" or "have"
    def fFeature_1(self, h, tag):
	if tag !="Feature":
		return 0
	words = self.wmap[h["wn"]]['words']
	if(h["i"] - 1 > 0):
		if(h['tb']=="Phone" and (words[h['i']-1]=="with" or words[h['i']-1]=="have" or words[h['i']-1]=="has")):
	                self.check = True
			return 1
		else:
			return 0
	return 0


    #pos tag is CD and next word is inches, or inch i.e present in the size list.
    def fFeature_2(self, h, tag):
	if tag !="Feature":
		return 0
	words = self.wmap[h["wn"]]['words']
	tags = self.wmap[h["wn"]]['pos_tags']
	if(h["i"] + 1 <len(words)):
            next_word = h['i']+1
            if(tags[next_word]=='CD' and (words[next_word] in size_list)):
	        self.check = True
		return 1
	else:
		return 0
	return 0

    #if the word is an inch,inches etc and is preceded by cd tag(nltk pos tag)
    def fFeature_3(self, h, tag):
	if tag !="Feature":
		return 0
	words = self.wmap[h["wn"]]['words']
	tags = self.wmap[h["wn"]]['pos_tags']
	if(h["i"] - 1 >0):
            prev_word = h['i']-1
            if(tags[prev_word]=='CD' and (words[h['i']] in size_list)):
	        self.check = True
		return 1
	else:
		return 0
	return 0

    #previous word is a feature( for screen size etc)
    def fFeature_4(self, h, tag):
	if tag !="Feature":
		return 0
	words = self.wmap[h["wn"]]['words']
	if(h['tb']=="Feature"):
	        self.check = True
		return 1
	else:
		return 0
	return 0

    def fOther_1(self, h, tag):
        if tag != "Other":
            return 0
        if self.check == False:
            return 1
        else:
                return 0
        return 0

    def fOther_2(self, h, tag):
	if tag != "Other":
		return 0
	words = self.wmap[h["wn"]]['words']
	if(words[h['i']][0].islower()):
		return 1
	else:
		return 0



if __name__ == "__main__":
    pass

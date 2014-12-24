# input : rer_out : json: wordlist, relationship, all tags
# output : query sentence

import nltk.metrics.distance as dist
import ner_client


def feature_query():
    pass


def interest_intent():
    global rer_out, brand, product, feature, items
    count = 0
    brand = ""
    product = ""
    flag = False
    # user specifies a particular phone
    if("Org" in rer_out['taglist']):
        flag = True
        brand = rer_out['wordlist'][rer_out['taglist'].index("Org")]

    if("Family" in rer_out['taglist']):
        flag = True
        product = rer_out['wordlist'][rer_out['taglist'].index("Family")]
        if("Version" in rer_out['taglist']):
            for i in rer_out['taglist']:
                if(i == "Version"):
                    product += " " + rer_out['wordlist'][rer_out['taglist'].index(i)]

    # user wants a phone with a particular feature without specifying the brand
    if("Org" not in rer_out['taglist'] and "Family" not in rer_out['taglist'] and "Feature" in rer_out['taglist']):
        return "Feature"
        # call feature query
        pass 

    # user wants a phone in a particular price range
    elif("Org" not in rer_out['taglist'] and "Family" not in rer_out['taglist'] and "Price" in rer_out['taglist']):
        return "Price"
        # call price query
        pass

    # user wants a phone for a specific function
    elif("Org" not in rer_out['taglist'] and "Family" not in rer_out['taglist'] and "Price" not in rer_out['taglist'] and "Feature" not in rer_out['taglist']):
        return "Could you be a little more specific in terms of features, brands or price?"

    # user just says he wants to buy a phone - ask for price range
    elif("Org" not in rer_out['taglist'] and "Family" not in rer_out['taglist']):
        return "Sure, what price range are you looking at?"

    if(flag == True):
        # user has specified a particular phone without its brand
        if(brand == ""):
            for i in allprods:
                if(product in allprods[i]):
                    brand = i
                    break
            if(brand == ""): # couldn't find the appropriate brand for this product
                return "We  don't seem to have this product. Would you like to choose another?"
            else:
                return "Sure, we have this product in stock. What do you want to know about it?"
            
        elif(product == ""): # user says he wants to buy a phone of this brand but not which phone. Returns all phones of this brand, choose which you want
            for i in allprods:
                if(dist.edit_distance(i, brand) < 2):
                    brand = i
                    break
            try:
                for j in allprods[brand]:
                    items.append(j)
            except KeyError as e:
                return "We don't seem to have this device. Would you like to choose a different one?"
            
            return "These are some of the phones we have in this brand. Do you want to anything more specific in mind in terms of features or price?" + str(items[0:10])
        
        elif(len(brand) != 0): # user has specified brand and product
            if brand in allprods:
                return "Sure we have this product in stock. Just add it to your shopping cart"
                    
        return "I'm sorry, we don't seem to have this in stock. Would you like to choose a different phone?"

def make_compatible(input_str):
    for i in range(len(rer_out['taglist'])):
        if(rer_out['taglist'][i] == "Org"):
            for j in allprods:
                if(dist.edit_distance(rer_out['wordlist'][i], j) < 2):
                    rer_out['wordlist'][i] = j
                    break
        if(rer_out['taglist'][i] == "Family"):
            for j in allprods:
                for k in allprods[j]:
                    if(dist.edit_distance(rer_out['wordlist'][i], k) < 4):
                        rer_out['wordlist'][i] = k
                        break

ner = ner_client.NerClient("1PI11CS137", "g11")
brand = ""
product = ""
feature = []
items = []

allprods = eval(ner.get_brand_product_bigrams_dict())
#print(len(allprods))

sentence = "I want to buy an iphone"
words = sentence.split(" ")

rer_out = {'wordlist': words, 'relationship': 'interest_intent', 'taglist': ['Other', 'Other', 'Other', 'Other', 'Other', 'Family']}
make_compatible(" ".join(rer_out['wordlist']))
print(interest_intent())

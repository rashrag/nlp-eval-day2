#input:rer_out:wordlist,relationship,all tags
import nltk.metrics.distance as dist
import ner_client
price_below_list=["less","below","lesser"]
price_above_list=["more","above","greater","great"]
price_equal_list=["equals","is","same"]
price_between_list=["between","range"]
currency_list= ["rs", "inr", "$", "usd", "cents", "rupees"]
price_list=["cost","price","charge","fee","terms","payment","rate","fare","levy","toll","amount","sum","total","figure","expensive","cheap","cheaper","cheapest"]
currency_symbols = ["rs", "inr", "$", "usd", "cents", "rupees"]
def init():
	print "yr"
	global ner
	ner=ner_client.NerClient("1PI11CS138","G11")
def price_query(wordlist,taglist,Org,Product):
	#wordlist=rer_out['wordlist']
	#taglist=rer_out['taglist']
	make_compatible(rer_out)
	if(Product):
		get_org_Product_query = ner.get_products(Org,Product)
	else:
		get_org_Product_query = ner.get_products(Org)
	li=[]
	items=[]
	for i in get_org_Product_query:
		li.append(i["dummy_price"]);
	print li
	specified_price=[]
	i1=0
	#print wordlist,taglist
	for i in range(0,len(taglist)):
		if((taglist[i]=="Price") and(wordlist[i] not in currency_list)):
			#print i
			specified_price.append(wordlist[i]);
			i1+=1
	for i in range(0,len(specified_price)):
		if("k" in specified_price[i].lower()):
			#print "came here"
			specified_price[i]=specified_price[i].lower().strip("k");
			#print specified_price[i]
			specified_price[i]=int(specified_price[i])*1000;
			#print specified_price[i]
	for prices in specified_price:
		print prices;
	if([i for i in wordlist if i in price_below_list]):
		#write code to get products lesser than price		
		print "less"
		for i in get_org_Product_query:
			if(str(i["dummy_price"])<specified_price[0]):
				items.append(i);
		if(items):
			return items
		else:
			print "came else"
			return 0
	elif([i for i in wordlist if i in price_above_list]):		
		#write code to get products lesser than price
		print "great"
		for i in get_org_Product_query:
			if(str(i["dummy_price"])>specified_price[0]):
				items.append(i);
		if(items):
			return items
		else:
			print "came else"
			return 0
	
	elif([i for i in wordlist if i in price_between_list]):		
		print "came here"
		for i in get_org_Product_query:
			#print type(i["dummy_price"]),type(specified_price[0]),type(specified_price[1])
			if(i["dummy_price"]>=int(specified_price[0]) and i["dummy_price"]<=int(specified_price[1])):
				items.append(i);
		if(items):
			return items
		else:
			print "came else"
			return 0
	elif(len([i for i in wordlist if i in price_equal_list])!=0):		
		#write code to get products lesser than price
		print "equal"
		for i in get_org_Product_query:
			if(str(i["dummy_price"])==specified_price[0]):
				items.append(i)
		if(items):
			return items
		else:
			print "came else"
			return 0
	elif(len([i for i in wordlist if i in price_equal_list])==0 and ("Price" in taglist)):		
		#write code to get products lesser than price
		print "spl case:",specified_price[0]
		for i in get_org_Product_query:
			#print type(i["dummy_price"]),type(specified_price[0])
			if(str(i["dummy_price"])==(specified_price[0])):
				print "if"
				items.append(i)
		if(items):
			return items
		else:
			print "came else"
			return 0
	
	else:
		return 0
		#write code to get products between the two given prices
def comparison_query(wordlist,taglist,compare_base):
	#wordlist=rer_out['wordlist']
	#taglist=rer_out['taglist'
	make_compatible(rer_out)
	Org=[]
	Product=[]
	if("Org" in rer_out['taglist']):
	        Org.append(rer_out['wordlist'][rer_out['taglist'].index("Org")])
	if("Family" in rer_out['taglist']):
        	flag = True
       		product = rer_out['wordlist'][rer_out['taglist'].index("Family")]
	        if("Version" in rer_out['taglist']):
        	    for i in rer_out['taglist']:
        	        if(i == "Version"):
        	            product +=" " + rer_out['wordlist'][rer_out['taglist'].index(i)]
		for i in allprods:
			if(product in allprods[i]):
				product=i+":"+product;
				Product.append(product)
	#code to find the two things being compared[org or family version or OS]
	compare_list=[]
	if(compare_base=="feature"):
		feature()#sanjana's function
	elif(compare_base=="price"):
		if(Product):
			compare_list.append(price_query(wordlist,taglist,Product.split(":")[0],Product.split(":")[1]));
		elif(Org):
			compare_list.append(price_query(wordlist,taglist,Org.split(":")[0],Org.split(":")[1]));
		else:
			return 0;
		return compare_list
			
def interest_intent(rer_out):
    make_compatible(rer_out)
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
                return "Sure, we have this product in stock"
            
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
            
            return "These are the phones we have in this brand. Do you have anything more specific in mind in terms of features or price?" + str(items)
        
        elif(len(brand) != 0): # user has specified brand and product
            if brand in allprods:
                return "Sure we have this product in stock. Just add it to your shopping cart"
                    
        return "I'm sorry, we don't seem to have this in stock. Would you like to choose a different phone?"

def make_compatible(rer_out):
    for i in range(len(rer_out['taglist'])):
        if(rer_out['taglist'][i] == "Org"):
            for j in allprods:
                if(dist.edit_distance(rer_out['wordlist'][i], j) < 2):
                    rer_out['wordlist'][i] = j
                    break

init()	
allprods = eval(ner.get_brand_product_bigrams_dict())
wordlist=["Could","you","compare","Samsung","and","Apple","phones"]#"is","range","31728","and","60k","?"]
taglist=["Other","Other","Other","Org","Other","Org","Phone"]#,"Other","Price","Other","Price","Other"]
Org="Apple"
Product="iPhone 6"
it=price_query(wordlist,taglist,"price")


if(it==0):
	print "no phones of your choice"
else:
	print it

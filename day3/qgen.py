#input:rer_out:wordlist,relationship,all tags
import ner_client
price_below_list=["less","below","lesser"]
price_above_list=["more","above","greater","great"]
price_equal_list=["equals","is","same"]
price_between_list=["between","range"]
currency_list= ["rs", "inr", "$", "usd", "cents", "rupees"]
def init():
	print "yr"
	global ner
	ner=ner_client.NerClient("1PI11CS138","G11")
def price_query(wordlist,taglist,Org,Product):
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
def comparison_query(wordlist,taglist,Org,Product):
		



init()	
wordlist=["Could","you","suggest","some","Samsung","phones","whose","cost","is","range","31728","and","60k","?"]
taglist=["Other","Other","Other","Other","Org","Phone","Other","Other","Other","Other","Price","Other","Price","Other"]
Org="Apple"
Product="iPhone 6"
it=price_query(wordlist,taglist,Org,"")


if(it==0):
	print "no phones of your choice"
else:
	print it

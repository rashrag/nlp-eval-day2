class Memm(object):
    def __init__(self): 
        print "MEMM"
        return


    def viterbi(self,tagset, sentence, maxent_clf, sent_num):
	pi = dict()
	bp = dict()
	pi[(0, '*', '*')] = 1
	tagset.append('*')
	final_u = ""
        final_v = ""
	print (sentence)
	'''
	for k in range(1, len(sentence)+1):
            for u in tagset:
		for v in tagset:
            	    prods = {}
		    max_prod = 0
		    for t in tagset:
                	if((k-1, t, u) in pi):
				#print ((k-1,t,u))
                    		prod = pi[(k-1, t, u)] * maxent_clf.p_y_given_x({"ta":t, "tb":u, "wn": sent_num , "i":k-1}, v)
				#if "*" in tagset:
				#	tagset.remove("*")
                	else:
                    		continue
                	if(prod >= max_prod):
				print ("Enter")
                    		max_prod = prod
                   		bp[(k ,u, v)] = t
                    		pi[(k ,u, v)] = max_prod
				final_u = u
				final_v = v
		break

	if "*" in tagset:
		tagset.remove("*")
	
	'''
	for k in range(1, len(sentence)+1):
            for u in tagset:
                for v in tagset:
                    prods = {}
                    max_prod = 0
                    for t in tagset:
                        if((k-1, t, u) in pi):
                                #print ((k-1,t,u))
                                prod = pi[(k-1, t, u)] * maxent_clf.p_y_given_x({"ta":t, "tb":u, "wn": sent_num , "i":k-1}, v)
                                #if "*" in tagset:
                                #        tagset.remove("*")
                        else:
                                continue
                        if(prod > max_prod):
                                print ("Enter")
                                max_prod = prod
                                bp[(k ,u, v)] = t
                                pi[(k ,u, v)] = max_prod
                                final_u = u
                                final_v = v




	
	finaltags = {}
	finaltags[len(sentence)] = final_v
	finaltags[len(sentence) - 1] = final_u
    	print (final_u,final_v)
	for k in range(len(sentence)-2, 0, -1):
		finaltags[k] = bp[(k+2, finaltags[k+1], finaltags[k+2])]
	
	for i in range(1,len(finaltags)+1):
		if finaltags[i] == "*":
			finaltags[i] = "Other"
	return list(finaltags.values())


import rules
import ner_metrics
import cleanTags
import build_history
import feature_functions
import mymaxent
#import memm

#all_tags = build_history.supported_tags_list

cleanTags.clean();

tuple1 = build_history.call()
(history_list, expected_relations) = tuple1
##all_tags = tuple1[1]; #return is (history_list, sents, expected)
##
##print all_tags

#create feature function obj call it func
func_obj = feature_functions.FeatureFunctions()

pickle_file = r"rer_data.p"
maxentclf = mymaxent.MyMaxEnt(history_list,func_obj,reg_lambda=0.001, pic_file = pickle_file);
TRAIN = int(raw_input("Enter 1 for Train, 0 to use pickeled file:  "))
if TRAIN == 1:
        maxentclf.train();


'''
maxentclf = mymaxent.MyMaxEnt(history_list,func_obj,reg_lambda=0.001);
maxentclf.train();
'''
print("-----------------------------TRAINED-----------------------------")

#change this 10
mytaglist=[]


for hist in history_list[1200:]:
	if(rules.rule_greet(hist[0]["word_list"]) == "Greeting"):
		tag = "greeting"
	elif(rules.rule_agree(hist[0]["word_list"]) == "Agreement"):
		tag = "agreement"
	elif(rules.rule_disagree(hist[0]["word_list"]) == "Disagreement"):
		tag = "disagreement"
	elif(rules.rule_ack(hist[0]["word_list"]) == "Acknowledgement"):
		tag = "acknowledgement"
	else:
		tag = maxentclf.classify(hist[0]);
	mytaglist.append(tag);
print expected_relations[1:50]
print("$$$$$")
print mytaglist[1:50];

'''
mymemm = memm.Memm()
count = 0


predicted = []

for i in sents[1680:]:
        try:
                predicted.append(mymemm.viterbi(all_tags,i,maxentclf,count))
        except:
                print "error"
	print "count: ",count
	count += 1
'''


metrics = ner_metrics.NerMetrics(expected_relations[1200:], mytaglist)

met = metrics.compute()

print "**************************************************************************"

print met

print "**************************************************************************"

#metrics.print_results()



'''
for i in sents:
	mymemm.viterbi(all_tags,i,maxentclf,count)
	count += 1
	break
'''	

import rer_rules as rules
import rer_metrics as ner_metrics
import rer_cleanTags as cleanTags
import rer_build_history as build_history
import rer_feature_functions as feature_functions
import rer_mymaxent as mymaxent
#import memm

#all_tags = build_history.supported_tags_list

#cleanTags.clean();

#tuple1 = build_history.call()
#(history_list, expected_relations) = tuple1
##all_tags = tuple1[1]; #return is (history_list, sents, expected)
##
##print all_tags

#create feature function obj call it func
def main(history_list):
	func_obj = feature_functions.FeatureFunctions()

	pickle_file = r"rer_data.p"	
	maxentclf = mymaxent.MyMaxEnt(history_list,func_obj,reg_lambda=0.001, pic_file = pickle_file);
	#TRAIN = int(raw_input("Enter 1 for Train, 0 to use pickeled file:  "))
	#if TRAIN == 1:
     #   maxentclf.train();


	'''
	maxentclf = mymaxent.MyMaxEnt(history_list,func_obj,reg_lambda=0.001);
	maxentclf.train();
	'''
	#print("-----------------------------TRAINED-----------------------------")

	#change this 10
	mytaglist=[]


	for hist in history_list:
		if(rules.rule_greet(hist["word_list"]) == "Greeting"):
			tag = "greeting"
		elif(rules.rule_agree(hist["word_list"]) == "Agreement"):
			tag = "agreement"
		elif(rules.rule_disagree(hist["word_list"]) == "Disagreement"):
			tag = "disagreement"
		elif(rules.rule_ack(hist["word_list"]) == "Acknowledgement"):
			tag = "acknowledgement"
		else:
			tag = maxentclf.classify(hist);
		mytaglist.append(tag);
	#print expected_relations[1:50]
	#print("$$$$$")
	#print mytaglist[1:50];
	return mytaglist

	



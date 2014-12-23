#import ner_metrics
import cleanTags
import build_history
import feature_functions
#import mymaxent
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



maxentclf = mymaxent.MyMaxEnt(history_list,func_obj,reg_lambda=0.001);
maxentclf.train();

print("-----------------------------TRAINED-----------------------------")


#change this 10
mytaglist=[]


for hist in history_list[0:10]:
	tag = maxentclf.classify(hist[0]);
	mytaglist.append(tag);
print expected[0]
print("$$$$$")
print mytaglist;

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


print "PREDICTED: ", len(predicted)

metrics = ner_metrics.NerMetrics(expected[1680:], predicted)

met = metrics.compute()

print "**************************************************************************"

print met

print "**************************************************************************"

metrics.print_results()



'''
'''
for i in sents:
	mymemm.viterbi(all_tags,i,maxentclf,count)
	count += 1
	break
'''	

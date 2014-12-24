import re


# rules for greeting

greetings_list = ["Ahoy", "All right?", "Day", "How do you do", "Felicitations", "G'day", "Good afternoon", "Welcome", "Good evening", "Good morning", "Greetings", "Hello", "Hello there", "Hey", "Hey there", "Hey Brother", "Hey Sister", "Hi", "Hiya", "Hi there", "How are you", "How are you doing", "Howdy", "How's it going?", "How's it hanging?", "Salutations", "'Sup", "Welcome", "What's up?", "Yo"]
disagree_list = ["I don't think", "I do not agree", "I do not believe", "No way", "I'm afraid", "I am afraid", "disagree", "not worth", "does not have", "doesn't have", "I beg to differ", "exact opposite", "opposite", "Not necessarily", "not always true", "not always the case", "not so sure", "unsure", "do not want", "don't want", "not true", "isn't true"]
agree_list = ["I agree", "I also think", "I too", "is true", "'s true", "exactly", "I feel", "I also feel", "No doubt", "have a point", "I know", "got it right", "s right"]
ack_list = ["thanks", "thank you", "thank", "nice to meet you", "you later", "talk to you", "okay", "cool", "great", "right"]

def rule_greet(word_list):
    string = " "
    sentence = string.join(word_list)
    found = False
    for i in greetings_list:
        if(re.findall('\\b'+i.lower()+'\\b', sentence.lower())):
            print "i: ",i
            found = True
            break

    if(found == False):
        return None
    else:
        return "Greeting"


def rule_disagree(word_list):
    string = " "
    sentence = string.join(word_list)
    found = False
    for i in disagree_list:
        if(re.findall('\\b'+i.lower()+'\\b', sentence.lower())):
            found = True
            break

    if(found == False):
        return None
    else:
        return "Disagreement"


def rule_agree(word_list):
    string = " "
    sentence = string.join(word_list)
    found = False
    for i in agree_list:
        if(re.findall('\\b'+i.lower()+'\\b', sentence.lower())):
            found = True
            break

    if(found == False):
        return None
    else:
        return "Agreement"


def rule_ack(word_list):
    string = " "
    sentence = string.join(word_list)
    found = False
    for i in ack_list:
        if(re.findall('\\b'+i.lower()+'\\b', sentence.lower())):
            found = True
            break

    if(found == False):
        return None
    else:
        return "Acknowledgement"

'''
f = open("show.json", "r")
line = f.read()
obj = eval(line)
count = 0
for i in obj:
    for j in i['data']:
        print((j['sentence']))
        print(rule_greet(j['sentence'].split(" ")))
        if(count == 10):
            break
        count += 1

print(rule_greet(["Hi", "how", "are", "you"]))


print(rule_disagree(["I", "don't", "want", "to", "buy", "that"]))
print(rule_disagree(["This", "is", "not", "a", "good", "phone"]))
print(rule_disagree(["I", "don't", "think", "that's", "a", "nice", "phone"]))
'''

 

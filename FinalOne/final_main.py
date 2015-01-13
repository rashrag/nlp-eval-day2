import ner_main
import rer_main
import re
d_stop = True
ack_list = ["thanks", "thank you", "thank", "nice to meet you", "you later", "talk to you", "okay", "cool", "great", "right"]
greeting_list = ["Ahoy", "All right?", "Day", "How do you do", "Felicitations", "G'day", "Good afternoon", "Welcome", "Good evening", "Good morning", "Greetings", "Hello", "Hello there", "Hey", "Hey there", "Hey Brother", "Hey Sister", "Hi", "Hiya", "Hi there", "How are you", "How are you doing", "Howdy", "How's it going?", "How's it hanging?", "Salutations", "'Sup", "Welcome", "What's up?", "Yo"]
while(d_stop):
        sent = raw_input("Enter the sentence \n")
        sent = sent.replace("?", "")
        sent = sent.replace("!", "")

        word_list  = sent.split(" ")
        #call NER
        tag_list = ner_main.main(word_list)


        history = []
        history_list = {}
        history_list["word_list"] = word_list
        history_list["tag_list"] = tag_list
        history.append(history_list)


        

        greeting_list1 = [i.lower() for i in greeting_list]

        #call RER
        print tag_list
        new_word_list = []
        relations = rer_main.main(history)
        relation = relations[0]
        if(relation == "Agreement"):
                print("Yes. That's true")
        if(relation == "Acknowledgement"):
                string = " "
                sentence = string.join(word_list)
                found = False
                for i in ack_list:
                        if(re.findall('\\b'+i.lower()+'\\b', sentence.lower())):
                                startIn, endIn = match.span()
                                sentence.splice(startIn,endIn)
                                word_list = sentence.split()
                                found = True
                                print (word_list)
                                break

                

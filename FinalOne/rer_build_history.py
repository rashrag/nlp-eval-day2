import json
def build_history(data_list, supported_tags):
    #entity list as of now is irrelavant. sending it for features. change it if required.
    history_list = [] # list of all histories (list of tuples)
    sents = []
    count = 0
    expected = []
    expected_relation = []
    for data in data_list: # data is the inputs entered by a given student
        data1 = data['data']
        for rec in data1:
            updates = rec['updates']
            sent = rec['sentence']
            try:
                relations = rec['rels']
                value = list(relations[0].keys())[0]
                #print (value)
            except:
                value = "irrelevant"
                #print(rec)
                #print("...............**************************************************>...........")
                #continue
            
            words = []
            tags = []
            entities = []
            try:
                l = list(relations[0].keys())[0]
                expected_relation.append(value)
                for x in range(len(relations[0][l])):
                    entities.append(relations[0][l][x])
            except:
                expected_relation.append(value)
                
            for i in range(len(updates)):
                words.append(updates[i]['word'])
                tags.append(updates[i]['tag'])
            history = {}
            history["word_list"] = words
            history["tag_list"] = tags
            #history["entity_list"] = entities
            #print(history)
            try:
                history_list.append((history,list(relations[0].keys())[0] , ))
            except:
                history_list.append((history,value , ))

    return (history_list, expected_relation,)
def call():
    supported_tags_list = ["Org", "Family", "Price", "Phone", "Feature", "OS", "Version", "Other"]
    supported_relations_list = ["price_query", "feature_query", "comparison", "interest_intent", "irrelevant", "disagreement", "greeting", "agreement", "acknowledgement"]
    data = json.loads(open("new_all_data.json").read())['root']
    print("..........................................................................................................................................")
    return(build_history(data, supported_relations_list))



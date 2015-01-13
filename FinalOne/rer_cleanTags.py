import random
import json
def clean():
    data = json.loads(open("rer_all_data.json").read())['root'] #list of sentences
    #print(len(data))
    for i in range(len(data)):
        #print(i)
        #print(type(i))
        #dataOfStudent =  data[i]['data']#per data for a student
        #print(type(dataOfStudent))
        for j in range(len(data[i]['data'])):#each sentence
            #print(len(data[i]['data'][j]))
            for k in range(len(data[i]['data'][j]['updates'])):
                if(data[i]['data'][j]['updates'][k]['tag'] == "Date"):
                    data[i]['data'][j]['updates'][k]['tag'] = "Other"
                elif(data[i]['data'][j]['updates'][k]['tag'] == "Model"):
                    data[i]['data'][j]['updates'][k]['tag'] = "Version"
                elif(data[i]['data'][j]['updates'][k]['tag'] == "Location"):
                    data[i]['data'][j]['updates'][k]['tag'] = "Other"
                elif(data[i]['data'][j]['updates'][k]['tag'] == "Size"):
                    data[i]['data'][j]['updates'][k]['tag'] = "Feature"
                elif(data[i]['data'][j]['updates'][k]['tag'] == "App"):
                    data[i]['data'][j]['updates'][k]['tag'] = "Other"
                #print(data[i]['data'][j]['updates'][k]['tag'])
            try:
                l = list(data[i]['data'][j]['rels'][0].keys())[0]
                for x in range(len(list(data[i]['data'][j]['rels'][0][l]))):
                    if (data[i]['data'][j]['rels'][0][l][x] == "Date"):
                        data[i]['data'][j]['rels'][0][l][x] = "Other"
                    elif(data[i]['data'][j]['rels'][0][l][x] == "Model"):
                        data[i]['data'][j]['rels'][0][l][x] = "Version"
                    elif(data[i]['data'][j]['rels'][0][l][x] == "Location"):
                        data[i]['data'][j]['rels'][0][l][x] = "Other"
                    elif(data[i]['data'][j]['rels'][0][l][x] == "Size"):
                        data[i]['data'][j]['rels'][0][l][x] = "Feature"
                    elif(data[i]['data'][j]['rels'][0][l][x] == "App"):
                        data[i]['data'][j]['rels'][0][l][x] = "Other"
            except:
                continue
                #print(data[i]['data'][j]['rels'][0][l][x])
    newDict = {}
    newDict['root'] = data;
    newJson = json.dumps(newDict);
    f = open("new_all_data.json","w");
    f.write(newJson);
#cleanTags()

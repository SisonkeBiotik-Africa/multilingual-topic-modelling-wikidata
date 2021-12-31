from wikibaseintegrator import wbi_functions

#Getting language-neutral representations of topic clusters
with open("results.txt", "r") as f:
  topics = [line for line in f]

#Identifying the user language
lang = "fr"

#Translating language-neutral representations of topic clusters
with open("results_language_"+lang+".txt", "a") as f1:
  for topic in topics:
    topic_id = topic[:topic.find(":")+2]
    topicitems = topic[topic.find(":")+2:-1]
    topicitemslist = topicitems.split(" ")
    langtopics = []
    for item in topicitemslist:
      verif = wbi_functions.execute_sparql_query('SELECT * WHERE {wd:'+item.upper()+' rdfs:label ?label. FILTER(LANG(?label)="'+lang+'")}')
      if (verif["results"]["bindings"] == []): verif = wbi_functions.execute_sparql_query('SELECT * WHERE {wd:'+item.upper()+' rdfs:label ?label. FILTER(LANG(?label)="en")}')
      if (verif["results"]["bindings"] != []): 
        x = verif["results"]["bindings"]
        langtopics.append(x[0]["label"]["value"])
    langt1 = []
    for t in langtopics:
      st = t.replace(" ", "_")
      langt1.append(st)
    line = " ".join(langt1)
    print(topic_id+line)
    f1.write(topic_id+line+"\n")

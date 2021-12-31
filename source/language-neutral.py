from langdetect import detect
import advertools as adv
import spacy
from wikibaseintegrator import wbi_functions
import numpy as np
import lda
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import scipy

#Identifying the text language
def lang_detect(text):
    lang = detect(text)
    return lang

#Finding the Spacy Model for the text language
def spacy_model(lang):
    models = {"ca": "ca_core_news_sm", "da": "da_core_news_sm", "de": "de_core_news_sm",
              "el": "el_core_news_sm", "en": "en_core_web_sm", "es": "es_core_news_sm",
              "fr": "fr_core_news_sm", "it": "it_core_news_sm", "ja": "ja_core_news_sm",
              "nl": "nl_core_news_sm", "no": "nb_core_news_sm", "pl": "pl_core_news_sm",
              "pt": "pt_core_news_sm", "ro": "ro_core_news_sm", "ru": "ru_core_news_sm",
              "zh-cn": "zh_core_web_sm", "zh-tw": "zh_core_web_sm"}
    try:
        model = models[lang]
    except KeyError:
        model = ""
    return model

#Getting the Stop Words of the Text Language
def stop_words(lang):
    languages = {"ca": "catalan", "da": "danish", "de": "german", "el": "greek",
                 "en": "english", "es": "spanish", "fr": "french", "it": "italian",
                 "ja": "japanese", "nl": "dutch", "no": "norwegian", "pl": "polish",
                 "pt": "portuguese", "ro": "romanian","ru": "russian", "zh-cn": "chinese",
                 "zh-tw": "chinese"}
    try:
        language = languages[lang]
    except KeyError:
        language = ""
    stopwords = []
    if (language != ""): stopwords = adv.stopwords[language]
    return stopwords

#Load tokenizer, tagger, parser and NER for the language
def raw_noun_phrases(model, text, lang):
    s = []
    if (model != ""):
        nlp = spacy.load(model)
        #Defining stop words
        stopwords = stop_words(lang)
        # Process whole text
        text = text.lower()
        doc = nlp(text)
        # Analyze syntax and get all noun phrases
        s += [chunk.text for chunk in doc.noun_chunks]
    return s

#Cleaning the noun phrases
def clean_noun_phrases(raw, stopwords, model):
    #Eliminating stop words and punctuations from noun phrases
    sf = []
    for i in raw:
        word_tokens = i.split(" ")
        filtered_ngram = [w for w in word_tokens if not w.lower() in stopwords]
        ss = " ".join(filtered_ngram)
        for j in [",", ";", "(", ")", "[", "]", "{", "}", "."]:
            ss = ss.replace(j,"")
        #Singularizing noun phrases
        if (ss != ""):
            nlp = spacy.load(model)
            prep = nlp(ss)
            sing = [chunk1.lemma_ for chunk1 in prep.noun_chunks]
            if (sing != []): ss = sing[0]
        if (ss != ""): sf.append(ss)
    return sf

#Adding n-grams of the noun phrases
def augment(nphr):
    sf = nphr
    for item in nphr:
        substr = item.split(" ")
        for i in range(len(substr)-1):
            for j in range(i):
                sf.append(" ".join(substr[len(substr)-i-1:len(substr)-j]))
    return sf

#Substituting noun phrases by corresponding Wikidata items       
def langneutral(nphr, lang):
    wid = []    
    for item in nphr:
        wikidata_id = wbi_functions.search_entities(item, language=lang)
        if (wikidata_id != []): 
          considered_items = []
          for wikidata_item in wikidata_id[:2]:
            verif = wbi_functions.execute_sparql_query("SELECT * WHERE { {wd:"+wikidata_item+" ?prop wd:Q13442814} UNION {wd:"+wikidata_item+" wdt:P17 ?prop} }")
            if (verif["results"]["bindings"] == []): considered_items.append(wikidata_item)
          wid += considered_items
        wid = list(dict.fromkeys(wid))         
    return wid

#Converting raw text to a language-independent representation   
def langn_rep(text):
    lang = lang_detect(text)
    model = spacy_model(lang)
    stopwords = stop_words(lang)
    s = raw_noun_phrases(model, text, lang)
    if (s != []): 
        s = clean_noun_phrases(s, stopwords, model)
        s = augment(s)
        s = langneutral(s, lang)
    return s

#Extraction of the statements from the corpus
with open("corpus.txt", "r") as f:
    statements = [line for line in f]

titles = []
#Converting statements into language-neutral Wikidata-driven representations
for text in statements:
    wikidata_representation = langn_rep(text)
    wikidatast = " ".join(wikidata_representation)
    titles.append(wikidatast)
    print(titles)

#Latent Dirichlet Allocation with Term Frequency and Gibbs Sampling
vec = CountVectorizer()
X1 = vec.fit_transform(titles)
df = pd.DataFrame(X1.toarray(), columns=vec.get_feature_names())
X = scipy.sparse.csr_matrix(df.values)
vocab = vec.get_feature_names()
print(X)
X.shape
X.sum()
model = lda.LDA(n_topics=20, n_iter=1500, random_state=1)
model.fit(X)  # model.fit_transform(X) is also available
topic_word = model.topic_word_  # model.components_ also works
n_top_words = 8
for i, topic_dist in enumerate(topic_word):
  with open("results_LN.txt", "a") as f1:
     topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n_top_words+1):-1]
     topic_text = 'Topic {}: {}'.format(i, ' '.join(topic_words))
     print(topic_text)
     f1.write(topic_text+"\n")

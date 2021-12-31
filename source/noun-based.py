from langdetect import detect
import advertools as adv
import numpy as np
import lda
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import scipy

#Identifying the text language
def lang_detect(text):
    lang = detect(text)
    return lang

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

#Eliminating punctuations and stopwords  
def stop_words_elimination(text):
    lang = lang_detect(text)
    for j in [",", ";", "(", ")", "[", "]", "{", "}", "."]: text = text.replace(j,"")
    input = text.split(" ")
    stopwords = stop_words(lang)
    for s in stopwords: 
      while s in input: input.remove(s)
    text = " ".join(input)
    return text

#Extraction of the statements from the corpus
with open("corpus.txt", "r") as f:
    statements = [line for line in f]

titles = []
#Eliminating punctuations and stopwords
for text in statements:
    clean = stop_words_elimination(text)
    titles.append(clean)
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
print(enumerate(topic_word))
for i, topic_dist in enumerate(topic_word):
  with open("results_N.txt", "a") as f1:
     topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n_top_words+1):-1]
     topic_text = 'Topic {}: {}'.format(i, ' '.join(topic_words))
     print(topic_text)
     f1.write(topic_text+"\n")

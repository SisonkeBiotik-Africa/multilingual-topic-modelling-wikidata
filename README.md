# Multilingual-Topic-Modelling-Wikidata
An algorithm for language-independent LDA-based multilingual topic modelling based on Spacy and Wikidata
## Description
* This project aims to develop three algorithms that allows the topic modelling of multilingual texts related to the same field of interest. These algorithms are based on a combination of *Language Identification*, *Stopword and Punctuation Elimination*, *Spacy Pre-Trained Language Models*, *Latent Dirichlet Allocation*, and *Semantic Alignement to Wikidata*.
* The developed algorithms works for texts in sixteen natural languages: *Catalan* (ca), *Danish* (da), *German* (de), *Greek* (el), *English* (en), *Spanish* (es), *French* (fr), *Italian* (it), *Japanese* (ja), *Dutch* (nl), *Norwegian* (no), *Polish* (pl), *Portuguese* (pt), *Romanian* (ro), *Russian* (ru), and *Chinese* (zh).
## Files
* **Source**: We propose four algorithms in this research project. LDA here stands for Latent Dirichlet Allocation using collapsed Gibbs sampling. Explanation is also available in French at Topic_Modelling_with_Wikidata_Code_Source.ipynb:
  * *noun-based.py*: This algorithm includes all the terms of a sentence except stopwords in the LDA Algorithm. Here, punctuations are also eliminated before LDA. Nouns are not singularized or translated before LDA.
  * *noun-phrase-based.py*: This algorithm extracts the noun phrases in every analyzed sentence and singularizes them using Spacy mono-lingual pre-trained models. Then, the n-grams included in noun phrases are retrieved. The LDA is performed on noun phrases and on the n-grams they include.
  * *language-neutral.py*: This algorithm does the same as *noun-phrase-based.py*. However, prior to performing LDA, it converts extracted noun-phrases and n-grams into their Wikidata ID allowing an entity to be represented the same regardless the input language.
  * *language-neutral-representation-conversion.py*: This algorithm converts the output of *language-neutral.py* into a human-readable topic representation in a given natural language.
* **Corpus**: To test our approaches, we use four corpora of 500 sentences:
  * *en-500*: English sentences randomly extracted from relevant biomedical literature reviews on COVID-19 as available in PubMed Central Database.
  * *es-500*: Spanish sentences randomly extracted from relevant biomedical literature reviews on COVID-19 as available in PubMed Central Database.
  * *fr-500*: French sentences randomly extracted from relevant biomedical literature reviews on COVID-19 as available in PubMed Central Database.
  * *multi-500*: Sentences in English, French and Spanish randomly extracted from relevant biomedical literature reviews on COVID-19 as available in PubMed Central Database.
* **Corpus_prep:** The creation and sampling process of the corpora is available in a ZIP File and an Excel File.
* **Output:** We apply the four algorithms on the three generated datasets and we provide the results of our experiments:
 * *stat.csv*: This provides the values of Log-likelihood at 1500 iterations as well as the runtime of the applications for every dataset.
  * *N_results.txt:* This provides the output of applying *noun-based.py* to a dataset.
 * *NP_results.txt:* This provides the output of applying *noun-phrase-based.py* to a dataset.
 * *LN_results.txt:* This provides the output of applying *language-neutral.py* to a dataset.
 * *results-language-en.txt:* This provides the output of applying *language-neutral-representation-conversion.py* to a dataset with English as a target natural language.
## Dependencies
* langdetect=1.0.9
* advertools=0.12.3
* spacy=2.2.4
* numpy=1.19.5
* lda=2.0.0
* pandas=1.1.5
* sklearn=1.0.1
* scipy=1.4.1
* wikibaseintegrator=0.11.1
* fr_core_news_sm=2.2.5
* es_core_news_sm==2.2.5
* en_core_web_sm==2.2.5
## Team
* Houcemeddine Turki, Data Engineering and Semantics Research Unit, University of Sfax, Tunisia
* René Fabrice Bile, École nationale supérieure polytechnique de Maroua, University of Maroua, Cameroon
* Mohamed Ali Hadj Taieb, Data Engineering and Semantics Research Unit, University of Sfax, Tunisia
* Mohamed Ben Aouicha, Data Engineering and Semantics Research Unit, University of Sfax, Tunisia

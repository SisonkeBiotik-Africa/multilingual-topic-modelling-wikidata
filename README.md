# Multilingual-Topic-Modelling-Wikidata
An algorithm for language-independent LDA-based multilingual topic modelling based on Spacy and Wikidata
## Description
* This project aims to develop three algorithms that allows the topic modelling of multilingual texts related to the same field of interest. These algorithms are based on a combination of *Language Identification*, *Stopword and Punctuation Elimination*, *Spacy Pre-Trained Language Models*, *Latent Dirichlet Allocation*, and *Semantic Alignement to Wikidata*.
* The developed algorithms works for texts in sixteen natural languages: *Catalan* (ca), *Danish* (da), *German* (de), *Greek* (el), *English* (en), *Spanish* (es), *French* (fr), *Italian* (it), *Japanese* (ja), *Dutch* (nl), *Norwegian* (no), *Polish* (pl), *Portuguese* (pt), *Romanian* (ro), *Russian* (ru), and *Chinese* (zh).
## Files
* We propose four algorithms in this research project. LDA here stands for Latent Dirichlet Allocation using collapsed Gibbs sampling:
** : This algorithm includes all the terms of a sentence except stopwords in the LDA Algorithm. Here, punctuations are also eliminated before LDA. Nouns are not singularized or translated before LDA.
** :
** :
** :
* To test our approaches, we use four corpora of 500 sentences:
** en-500: English sentences randomly extracted from relevant biomedical literature reviews on COVID-19 as available in PubMed Central Database.
** es-500: Spanish sentences randomly extracted from relevant biomedical literature reviews on COVID-19 as available in PubMed Central Database.
** fr-500: French sentences randomly extracted from relevant biomedical literature reviews on COVID-19 as available in PubMed Central Database.
** multi-500: Sentences in English, French and Spanish randomly extracted from relevant biomedical literature reviews on COVID-19 as available in PubMed Central Database.
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

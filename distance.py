from re import sub
from gensim.utils import simple_preprocess
from nltk.corpus import stopwords
from nltk import word_tokenize
import gensim.downloader as ap
from gensim.corpora import Dictionary
from gensim.models import TfidfModel
from gensim.models import WordEmbeddingSimilarityIndex
from gensim.similarities import SparseTermSimilarityMatrix
from gensim.similarities import SoftCosineSimilarity
import numpy as np
import ipfsapi

glove = ap.load("glove-wiki-gigaword-50")
api = ipfsapi.connect('127.0.0.1', 5001)
STOPWORDS = set(stopwords.words('english'))



class Reputation:

    

    def __init__(self,author_address,author_reputation,hashes,timestamp,m, T):

        self.cs = 1
        self.author_address = author_address
        self.author_reputation = author_reputation
        self.hashes = hashes
        self.timestamp = timestamp
        self.m = m
        self.T = T

    def calculate_distance(self,query_string,documents):
       

    
        def preprocess(doc):
            # Tokenize, clean up input document string
            doc = sub(r'<img[^<>]+(>|$)', " image_token ", doc)
            doc = sub(r'<[^<>]+(>|$)', " ", doc)
            doc = sub(r'\[img_assist[^]]*?\]', " ", doc)
            doc = sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', " url_token ", doc)
            return [token for token in simple_preprocess(doc, min_len=0, max_len=float("inf")) if token not in STOPWORDS]

        # Preprocess the documents, including the query string
        corpus = [preprocess(document) for document in documents]
        query = preprocess(query_string)


        # Load the model: this is a big file, can take a while to download and open
            
        similarity_index = WordEmbeddingSimilarityIndex(glove)

        # Build the term dictionary, TF-idf model

        dictionary = Dictionary(corpus+[query])
        tfidf = TfidfModel(dictionary=dictionary)

        # Create the term similarity matrix.  
        similarity_matrix = SparseTermSimilarityMatrix(similarity_index, dictionary, tfidf)

        query_tf = tfidf[dictionary.doc2bow(query)]

        index = SoftCosineSimilarity(
                    tfidf[[dictionary.doc2bow(document) for document in corpus]],
                    similarity_matrix)

        doc_similarity_scores = index[query_tf]

        # Output the sorted similarity scores and documents
        sorted_indexes = np.argsort(doc_similarity_scores)[::-1]
        if len(documents) > 1:
            for idx in sorted_indexes:
                print(f'{idx} \t {doc_similarity_scores[idx]:0.3f} \t {documents[idx]}')
        # print(doc_similarity_scores)
        return doc_similarity_scores

    def Quality(self,text1,text2,text3):

        similarity_scores = self.calculate_distance(text3,[text1,text2])         #calculates similarity score of text1 and text2 with text3

        sc = self.calculate_distance(text1,[text2])
        print("\n\n",sc)
        self.sc = sc
        if sc[0] == 0:
            return 0
        qual = (similarity_scores[0] - similarity_scores[1])/sc[0]

        return qual

    def Increase(self):

        if self.author_address[self.i] == self.author_address[self.k]:
            increase = 0
        else:
            increase = self.cs * self.Quality(self.text1,self.text2,self.text3) * self.sc[0] * np.log(1.1 + self.author_reputation[self.k])


        return increase

    def basic_algorithm(self,author_reputation ):

        author_reputation[self.j] = author_reputation[self.j]+self.Increase()
        return author_reputation


    def reputation_cap_algorithm(self, author_reputation):


        inc = self.Increase()
        if inc > 0:
            
            author_reputation[self.j] = max(author_reputation[self.j], min(author_reputation[self.i],author_reputation[self.k],author_reputation[self.j]+inc))

        else:
            author_reputation[self.j] = author_reputation[self.j]+inc

        return author_reputation

    def reputation_cap_nix_algorithm(self, author_reputation):
        nix = 0
        if self.Quality(self.text1,self.text2,self.text3) < 0 and (self.timestamp[self.k] - self.timestamp[self.i]) <= self.T:
            nix = 1
        elif self.k - self.i >= self.m  and  (self.timestamp[self.k] - self.timestamp[self.i]) <= self.T :
            nix = 1


        if nix == 1:
            return self.reputation_cap_algorithm(author_reputation)
        else:
            return self.basic_algorithm(author_reputation)
            

     



    def update_reputation(self):
        self.text1 = api.cat(self.hashes[self.i]).decode("utf-8")
        self.text2 = api.cat(self.hashes[self.j]).decode("utf-8")
        self.text3 = api.cat(self.hashes[self.k]).decode("utf-8")
        return self.reputation_cap_nix_algorithm(self.author_reputation)

        


    def final_updation(self):
        print("final_updation")
        l = len(self.hashes)
        for a in range(self.m):
            if l - a- 3 >= 0:
                self.i = l - a -3
                self.j = l-2
                self.k = l-1 
                
                self.author_reputation = self.update_reputation()
                
            else:
                break

        return self.author_reputation        








### array of hashes, m, 
## retrieve last m articles from their hashes
## calculate distance between each triplet
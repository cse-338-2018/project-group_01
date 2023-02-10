import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk, string
# from keras.preprocessing.sequence import pad_sequences
# from transformers import BertTokenizer,  AutoModelForSequenceClassification
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import TruncatedSVD
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import pickle
import dill
# nltk.download()

data_path = "combined.csv"
pd.set_option('display.max_colwidth', None)
# Initialize the stemmer and tokenizer
stemmer = PorterStemmer()
tokenizer = word_tokenize
# Create a TfidfVectorizer object to convert the text data into numerical features
tfidf = TfidfVectorizer()

def preprocess_data(data_path, sample_size):

  # Read the data from specific path
  data = pd.read_csv(data_path, index_col=0)
  # data = pd.read_csv(data_path, low_memory=False, quoting=3, error_bad_lines=False)

  # Drop articles without Abstract
  data = data.dropna(subset = ['abstract']).reset_index(drop = True)

  # Get "sample_size" random articles
  #data = data.sample(sample_size)[['abstract']]

  return data

# Define a function to preprocess the text data
def preprocess_text(text):
    # Tokenize the text
    tokens = tokenizer(text)
    
    # Stem each token
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    
    # Join the stemmed tokens back into a single string
    stemmed_text = ' '.join(stemmed_tokens)
    
    return stemmed_text

source_data = preprocess_data(data_path, 44000)
preprocessed_data = [preprocess_text(text) for text in source_data['abstract'].tolist()]
training_data = tfidf.fit_transform(preprocessed_data)

def get_cosine_similarity(text1, text2):
    tfidf = TfidfVectorizer().fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]

def is_similar(similarity_score, similarity_threshold):

  is_similar = False

  if(similarity_score >= similarity_threshold):
    is_similar = True

  return is_similar

def run_similarity_analysis(query_text, similarity_threshold=0.8):

    top_N=10

    # Preprocess the given document
    preprocessed_document = preprocess_text(query_text)
    
    # Convert the given document into numerical features
    X_new = tfidf.transform([preprocessed_document])
    
    # Compute cosine similarity between the given document and each research paper
    similarities = cosine_similarity(training_data, X_new)

    # Sort the research papers based on their similarity with the given document
    indices = np.argsort(similarities, axis=0)
    indices = indices[::-1]
    
    # Get the top N research papers with the highest similarity
    top_n_indices = indices[:top_N, 0]
    
    # Compute the similarity percentage with the top 10 research papers
    similarity_percentage = similarities[top_n_indices, 0] * 100

    # assign data of lists.
    texts = source_data['abstract'].tolist();
    similar_articles = {'abstract': [texts[i] for i in top_n_indices], 'similarity': similarity_percentage}  
  
    # Create DataFrame  
    formated_result = pd.DataFrame(similar_articles)
    
    # Create JSON Array
    similarity_decision=[]
    for x in formated_result.iloc:
        json={'similarity_score': x["similarity"], 
                           'similarity_percentage': str(round(x["similarity"])) + '%',
                            'most_similar_article': x["abstract"]
                        }
        similarity_decision.append(json)
    return similarity_decision


new_incoming_text = "BACKGROUND: Human infection studies (HIS) are valuable in vaccine development. Deliberate infection, however, creates challenging questions, particularly in low and middle-income countries (LMICs) where HIS are new and ethical challenges may be heightened. Consultation with stakeholders is needed to support contextually appropriate and acceptable study design. We examined stakeholder perceptions about the acceptability and ethics of HIS in Malawi, to inform decisions about planned pneumococcal challenge research and wider understanding of HIS ethics in LMICs. METHODS: We conducted 6 deliberative focus groups and 15 follow-up interviews with research staff, medical students, and community representatives from rural and urban Blantyre. We also conducted 5 key informant interviews with clinicians, ethics committee members, and district health government officials. RESULTS: Stakeholders perceived HIS research to have potential population health benefits, but they also had concerns, particularly related to the safety of volunteers and negative community reactions. Acceptability depended on a range of conditions related to procedures for voluntary and informed consent, inclusion criteria, medical care or support, compensation, regulation, and robust community engagement. These conditions largely mirror those in existing guidelines for HIS and biomedical research in LMICs. Stakeholder perceptions pointed to potential tensions, for example, balancing equity, safety, and relevance in inclusion criteria. CONCLUSIONS: Our findings suggest HIS research could be acceptable in Malawi, provided certain conditions are in place. Ongoing assessment of participant experiences and stakeholder perceptions will be required to strengthen HIS research during development and roll-out."

# Run the plagiarism detection
# analysis_result = run_similarity_analysis(new_incoming_text)
# print(analysis_result)
class Myclass:
  def predict(self,new_incoming_text):
      decision=run_similarity_analysis(new_incoming_text)
      return decision
model=Myclass()
pickle.dump(model, open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))
print(model.predict("lslslslss"))
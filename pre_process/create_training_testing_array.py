import pickle
from vectorize_text import vectorize, features_selection

from sklearn.model_selection import train_test_split

def preprocess(words_file = "../../data/word_data.pkl", authors_file="../../data/email_authors.pkl"):
    '''
    This function takes a list of email texts in pkl format, and the corresponding
    authors, vectorize them into tfidf matrix and get the most important features.
    The features and the labels are then put into arrays and the train/test sets
    are generated and ready to be used with a Machine Learning model.

    :param words_file: pickle containing the content from  Sara and Chris' emails
    :param authors_file: authors (Sara = 0 or Chris = 1) associated to the content in words_file
    :return: 4 objects: training/testing features & training/testing labels
    '''

    print("Getting authors and emails content.")
    # Get features/words and labels/authors from the input .pkl files
    authors_file_handler = open(authors_file, "rb")
    authors = pickle.load(authors_file_handler)
    authors_file_handler.close()

    words_file_handler = open(words_file, "rb")
    words_data = pickle.load(words_file_handler)
    words_file_handler.close()


    # Split features and labels into train and test datasets
    features_train, features_test, labels_train, labels_test = train_test_split(words_data, authors,
                                                                                                 test_size=0.1,
                                                                                                 random_state=42)

    print("Performing text vectorization.")
    # Perform text vectorization
    features_train_transformed, features_test_transformed = vectorize(features_train, features_test)


    print("Selecting most helpful features.")
    # Select most helpful features
    features_train_transformed, features_test_transformed = features_selection(features_train_transformed,
                                                                                 features_test_transformed,
                                                                                 labels_train)

    print("Train and test datasets generated:")
    print("no. of Chris training emails:", sum(labels_train))
    print("no. of Sara training emails:", len(labels_train) - sum(labels_train))
    return features_train_transformed, features_test_transformed, labels_train, labels_test


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectPercentile, f_classif

def vectorize(features_train, features_test):
    '''
        Given an array of words, the following function vectorize the text.
        Vectorization (or feature extraction) is the process to encode words
        as integers or floating point values, in order to be use as input to
        a machine learning algorithm.

        In this case we use TfidfVectorizer from sklearn, that transform words
        into word frequency vectors.
    '''

    vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words='english')
    features_train_transformed = vectorizer.fit_transform(features_train)
    features_test_transformed = vectorizer.transform(features_test)

    return features_train_transformed, features_test_transformed


def features_selection(features_train_transformed, features_test_transformed, labels_train):
    '''
        Because text is super high dimensional and can be really computationally
        expensive, so we select/keep the most helpful features (words).
    '''

    # features_test_transformed = features_test_transformed.toarray()
    # features_train_transformed = features_train_transformed.toarray()
    selector = SelectPercentile(f_classif, percentile=90)
    selector.fit(features_train_transformed, labels_train)
    features_train_transformed = selector.transform(features_train_transformed).toarray()
    features_test_transformed = selector.transform(features_test_transformed).toarray()

    return features_train_transformed, features_test_transformed
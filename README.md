# Application of classification algorithms
This project is based on the [course project material for the ML Udacity course UD120](https://github.com/udacity/ud120-projects). The aim is to apply different ML _classification_ algorithms to some datasets.

### Mini Project 1
We have a set of emails, half of them written by one person and the other half written by another person at the same company. The aim is to classify the emails as written by one person or the other based on the analysis of the text of the email. The set of email used is the [Enron Corpus](https://en.wikipedia.org/wiki/Enron_Corpus) email set.

The classification algorithms used are:

- [Naive Bayes](classification_algorithms/naive_bayes)
- [Support Vector Machine](classification_algorithms/svm)
- [Decision Trees](classification_algorithms/decision_trees)

### Mini Project 2
We have random generated data about terrain type, either bumpy or with slopes. The aim is too figure out whether a self-driving car can go fast or slow according to the type of terrain - a combination of different grades of slopiness and bumpiness.

The classification algorithms used for the terrain dataset are:
- [K Nearest Neighbour (k-NN)](classification_algorithms/knn)
- [Random Forest](classification_algorithms/random_forest)
- [Adaboost (boosted decision tree)](classification_algorithms/adaboost)

___

## How to start
1. Check out that you have a working Python installation, preferably Python 3
2. Git clone the [repo][add link] and cd inside directory
3. Install requirements: 

    `pip install -r requirements.txt`
4. Check that all the modules have been installed and download the Enron datasets : 
    
    `python startup.py`
5. In each algorithm folder, run: 
    
    `python main.py`
    
    to get the results of the algorithm applied to the dataset.
    
Finally, the folder [pre_process](process) contains some Python code to pre-process the dataset to be used with the algorithms.

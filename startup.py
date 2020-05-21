# Check Python module installation
print("Checking requirements...")

print("Is nltk installed?")
try:
    import nltk
    print("Yes")
except ImportError:
    print("No. Please install nltk before continuing.")

print("Is numpy installed?")
try:
    import numpy
    print("Yes")
except ImportError:
    print("No. Please install numpy before continuing.")

print("Is scikit-learn installed?")
try:
    import sklearn
    print("Yes")
except ImportError:
    print("No. Please install scikit-learn before continuing.")

print("Is scipy installed?")
try:
    import scipy
    print("Yes")
except ImportError:
    print("No. Please install scipy before continuing.")


# Downloading dataset
print("Downloading Enron Corpus dataset. This may take a while...")
import urllib.request
import sys

#show % download
def report(count, blockSize, totalSize):
    percent = int(count*blockSize*100/totalSize)
    sys.stdout.write("\r%d%%" % percent + ' complete')
    sys.stdout.flush()

url = "https://www.cs.cmu.edu/~./enron/enron_mail_20150507.tar.gz"
urllib.request.urlretrieve(url, filename="./data/enron_mail_20150507.tar.gz", reporthook=report)
print("\nDownload complete! Yeah!")


# Unzipping dataset
print("Unzipping dataset...")
import tarfile
import os
tfile = tarfile.open("./data/enron_mail_20150507.tar.gz", "r:gz")
tfile.extractall("./data")
print("Done. Have fun using ML!")




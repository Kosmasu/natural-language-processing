#conda install -n nlp beautifulsoup4
#conda install -n nlp lxml

from bs4 import BeautifulSoup 

with open('hasil/corpus.xml', 'r') as f:
  corpus = BeautifulSoup(f.read(), 'xml') 

# - berapa jumlah kata unik
# - rata-rata kata per kalimat
# - rata-rata panjang kalimat per dokumen

from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+')

wordCount = 0
sentenceCount = 0
documentCount = 0
uniqueWords = set()

documents = corpus.findAll('doc')
documentCount = len(documents)
for document in documents:
  sentences = document.findAll('s')
  sentenceCount += len(sentences)
  for sentence in sentences:
    words = tokenizer.tokenize(sentence.string)
    wordCount += len(words)
    for word in words:
      uniqueWords.add(word)
  break

print("wordCount:", wordCount)
print("sentenceCount:", sentenceCount)
print("documentCount:", documentCount)

print("amount of unique words:", len(uniqueWords))
print("avg word in sentence:", wordCount/sentenceCount)
print("avg sentence in document:", sentenceCount/documentCount)
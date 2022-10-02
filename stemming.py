from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

ps = PorterStemmer()

examples = ["python", "pythoner", "pythonly", "pythoned", "pythoning"]

stoppers = set(stopwords.words("english"))

sentence = "I am a python, I pythoned the problem last night, I acted pythonly, I know, but pythoning is hard. But, I guess that is the price to pay to be a pythoner"

for word in examples:
    print(ps.stem(word))
    
for word in word_tokenize(sentence):
    if word not in stoppers:
        print(ps.stem(word))
        

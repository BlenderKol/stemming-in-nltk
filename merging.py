from nltk import PorterStemmer
from nltk.corpus import stopwords, state_union
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

ps = PorterStemmer()

stoppers = set(stopwords.words("english"))

text = state_union.raw("2005-GWBush.txt")

print(dir(nltk.pos_tag))
for sentence in sent_tokenize(text):
    words = word_tokenize(sentence)
    list = [word for word in words if word not in stoppers]
    tagged = nltk.pos_tag(list)
    for word in tagged:
        print("word => {} stem=> {} P.O.S=> {}".format(word[0], ps.stem(word[0]), word[1]))

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Tutorial from https://www.youtube.com/watch?v=w36-U-ccajM&list=PLQVvvaa0QuDf2JswnfiGkliBInZnIC4HL&index=2

example_sentence = "This is an example showing off stop word filtration."
#print(sent_tokenize(example_text))

stop_words = set(stopwords.words("english"))
#stop_words.remove('off')
#stop_words = set(stopwords.words("spanish"))

print(stop_words)


words = word_tokenize(example_sentence)

#filtered_sentence = []
#
#for w in words:
#    if w not in stop_words:
#        filtered_sentence.append(w)

filtered_sentence = [ w for w in words if w not in stop_words ]


print(filtered_sentence)

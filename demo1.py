from nltk.tokenize import sent_tokenize, word_tokenize

example_text = "Hello Mr. Li, what a great day! Have you ever been to Beijing before? The weather is great and Python is awesome. The sky is pinkish-blue. You should not eat cardboard."

#print(sent_tokenize(example_text))

for i in word_tokenize(example_text):
    print(i)

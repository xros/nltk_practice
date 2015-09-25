# I was taking a ride in the car.
# I was riding in the car.


# ride and riding mean the same thing

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize


ps = PorterStemmer()

example_words = ["python", "pythoner", "pythoning", "pythoned", "pythonly"]
example_words = ["fish", "fisher", "fishing", "fished", "fishes"]

for w in example_words:
    print(ps.stem(w))


print('-- stem in sentense ---')

new_text = "It is very important to be pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."


words = word_tokenize(new_text)

for w in words:
    print(ps.stem(w))

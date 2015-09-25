"""
From http://pythonprogramming.net/part-of-speech-tagging-nltk-tutorial/

POS tag list:

CC	coordinating conjunction
CD	cardinal digit
DT	determiner
EX	existential there (like: "there is" ... think of it like "there exists")
FW	foreign word
IN	preposition/subordinating conjunction
JJ	adjective	'big'
JJR	adjective, comparative	'bigger'
JJS	adjective, superlative	'biggest'
LS	list marker	1)
MD	modal	could, will
NN	noun, singular 'desk'
NNS	noun plural	'desks'
NNP	proper noun, singular	'Harrison'
NNPS	proper noun, plural	'Americans'
PDT	predeterminer	'all the kids'
POS	possessive ending	parent's
PRP	personal pronoun	I, he, she
PRP$	possessive pronoun	my, his, hers
RB	adverb	very, silently,
RBR	adverb, comparative	better
RBS	adverb, superlative	best
RP	particle	give up
TO	to	go 'to' the store.
UH	interjection	errrrrrrrm
VB	verb, base form	take
VBD	verb, past tense	took
VBG	verb, gerund/present participle	taking
VBN	verb, past participle	taken
VBP	verb, sing. present, non-3d	take
VBZ	verb, 3rd person sing. present	takes
WDT	wh-determiner	which
WP	wh-pronoun	who, what
WP$	possessive wh-pronoun	whose
WRB	wh-abverb	where, when
"""
import nltk
from nltk.corpus import state_union


from nltk.tokenize import PunktSentenceTokenizer

from nltk.stem import PorterStemmer

ps = PorterStemmer()

#print(type(state_union))
#print(type(state_union.raw()))

train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

#print(train_text)
#print(sample_text)

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)


def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)

            print(tagged)

    except Exception as e:
        print(str(e))


"""
tagging from defined text files
"""
def process_my_content_get_noun():
    try:
        the_noun_set = set()
        with open('i_have_a_dream.txt', 'r') as f:
            lines = f.readlines()
            for l in lines:
                my_text_tokenized = nltk.word_tokenize(l)
                
                the_noun_set |= set(my_text_tokenized)

                my_text_tokenized = list(set(my_text_tokenized))



                for w in my_text_tokenized:
                    #print(ps.stem(w))
                    # stemming if you want
                    #the_noun_set.add(ps.stem(w))
                    pass


                #print(my_text_tokenized)
                #tagged = nltk.pos_tag(my_text_tokenized)
                #print(tagged)
                #print(type(tagged))                # It's a pure list
                # Which looks like this
                '''
                [('And', 'CC'), ('when', 'WRB'), ('this', 'DT'), ('happens', 'VBZ'), (',', ','), ('when', 'WRB'), ('we', 'PRP'), ('allow', 'VBP'), ('freedom', 'NN'), ('to', 'TO'), ('ring', 'VB'), (',', ','), ('when', 'WRB'), ('we', 'PRP'), ('let', 'VBP')]
                '''
                # Use this to filter it
                '''
                >>> the_dict = dict(the_list)
                >>> for i in the_dict:
                >>>     if i in ('NN', 'NNP'):
                >>>         print(i)
                '''


                # Write some filteration here
                # logics

                #the_dict = dict(tagged)
                #for i in the_dict:
                #    # Only get noun
                #    if the_dict[i] in ('NN', 'NNP', 'NNS', 'NNPS'):
                #        print(i)


        # output only noun
        tagged = nltk.pos_tag(list(the_noun_set))
        new_dict = dict(tagged)
        for i in new_dict:
            # Only get noun
            if new_dict[i] in ('NN', 'NNP', 'NNS', 'NNPS'):
                print(i)            
    except Exception as e:
                print('error')
                print(str(e))


process_my_content_get_noun()

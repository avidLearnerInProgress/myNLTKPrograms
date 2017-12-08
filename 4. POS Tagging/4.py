# -*- coding: utf-8 -*-
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

#------------POS Tagging-------------

'''
POS tag list:

    CC coordinating conjunction
    CD cardinal digit
    DT determiner
    EX existential there (like: "there is" ... think of it like "there exists")
    FW foreign word
    IN preposition/subordinating conjunction
    JJ adjective 'big'
    JJR adjective, comparative 'bigger'
    JJS adjective, superlative 'biggest'
    LS list marker 1)
    MD modal could, will
    NN noun, singular 'desk'
    NNS noun plural 'desks'
    NNP proper noun, singular 'Harrison'
    NNPS proper noun, plural 'Americans'
    PDT predeterminer 'all the kids'
    POS possessive ending parent's
    PRP personal pronoun I, he, she
    PRP$ possessive pronoun my, his, hers
    RB adverb very, silently,
    RBR adverb, comparative better
    RBS adverb, superlative best
    RP particle give up
    TO to go 'to' the store.
    UH interjection errrrrrrrm
    VB verb, base form take
    VBD verb, past tense took
    VBG verb, gerund/present participle taking
    VBN verb, past participle taken
    VBP verb, sing. present, non-3d take
    VBZ verb, 3rd person sing. present takes
    WDT wh-determiner which
    WP wh-pronoun who, what
    WP$ possessive wh-pronoun whose
    WRB wh-abverb where, when
'''

text=u'''
CLEANLINESS NEEDS OUR PARTICIPATION
Indians’ indifference towards cleanliness has led the country to avoidable uncleanliness, diseases and social menaces. Cleanliness is a responsibility every citizen must undertake, says DR. APPASAHEB DHARMADHIKARI
There are certain essential factors that we all keep in mind for good health of our family. Unfortunately, we are not so  alert  when  it  comes  to  social  life. This  indifference  towards  cleanliness  over the years has led to avoidable uncleanliness, diseases and social menaces across the coun-try. The problems built a setting where it was required  to  take  one  of  the  most  important national  decisions  ever.  The  Government  of India’s  Swachh  Bharat  Abhiyan,  today  run-ning on a large scale at Centre and State lev-els, has definitely brought advantages to peo-ple. While the Government is on the job, there is a lot the citizens have to do.
THE PROBLEM AT HAND
Epidemics  such  as  cholera,  gastroenteritis, typhoid  and  others  spread  due  to  uncleanli-ness.  Many  types  of  mosquitoes  proliferate on  rubbish  and  give  us  lethal  diseases  like malaria  and  dengue  that  take  away  many lives.  Environmental  pollution  is  another issue.  Besides,  the  trash  makes  our  villages and cities dirty and filthy.
People  staying  at  clean  and  tidy  homes are  frustrated  with  the  dirtiness  of  the  sur-rounding area and express anguish. However, these  persons  also  inadvertently  contribute to making the area dirty. We ourselves throw household  waste  out.  Thus,  a  controversy  is observed  in  humans  between  cleanliness  at home  and  the  area  around.  Observing  the unclean  area  around,  a  frustrated  man  asks questions  such  as  “What  is  the  Government doing?” and “Is the Municipal Council aware of  this  or  not?”  The  fact  is  that  the  Govern-ment is always carrying out its duties. A small number  of  local  self-government  employees are clearing wastes created by majority of the people. A man, however, places everything on them and absolves himself.
Dr. Appasaheb Dharmadhikari flanked by Chief Minister Devendra Fadnavis and other dignitaries at a cleanliness drive programme.
'''


trainText=state_union.raw("2005-GWBush.txt")
testText=state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer=PunktSentenceTokenizer(trainText)
tokenized=custom_sent_tokenizer.tokenize(testText)

try:
	for i in tokenized:
		words=nltk.word_tokenize(i)
		tagged=nltk.pos_tag(words)
		print(tagged)

except Exception as e:
	print(str(e))
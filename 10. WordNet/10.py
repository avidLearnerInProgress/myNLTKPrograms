from nltk.corpus import wordnet
syns=wordnet.synsets("programs")
print syns
print syns[0].name()
print syns[0].lemmas()[0].name()
print syns[0].definition()
print syns[0].examples()
print "\n"

synonyms=[]
antonyms=[]

for syn in wordnet.synsets("good"):
	for l in syn.lemmas():
		print "l:",l
		synonyms.append(l.name())
		if l.antonyms():
			antonyms.append(l.antonyms()[0].name())

print "\n"
print set(synonyms)
print set(antonyms)

# find semantic similarity
w1=wordnet.synset("good.n.01")
w2=wordnet.synset("better.n.01")
print w1.wup_similarity(w2)

w1=wordnet.synset("ship.n.01")
w2=wordnet.synset("car.n.01")
print w1.wup_similarity(w2)

w1=wordnet.synset("ship.n.01")
w2=wordnet.synset("boat.n.01")
print w1.wup_similarity(w2)







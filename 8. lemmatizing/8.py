
#similar to stemming

from nltk.stem import WordNetLemmatizer

lemmatizer=WordNetLemmatizer()

print lemmatizer.lemmatize("cats")
print lemmatizer.lemmatize("cacti")
print lemmatizer.lemmatize("rocks")
print lemmatizer.lemmatize("python")
print lemmatizer.lemmatize("better",pos="a")
print lemmatizer.lemmatize("best",pos="a")
print lemmatizer.lemmatize("ruined",pos="v")






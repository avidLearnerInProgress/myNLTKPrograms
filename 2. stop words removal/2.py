# -*- coding: utf-8 -*-

#------------Stop Words Removal-------------

import nltk
text=u'''
CLEANLINESS NEEDS OUR PARTICIPATION

Indians’ indifference towards cleanliness has led the country to avoidable uncleanliness, diseases and social menaces. Cleanliness is a responsibility every citizen must undertake, says DR. APPASAHEB DHARMADHIKARI

There are certain essential factors that we all keep in mind for good health of our family. Unfortunately, we are not so  alert  when  it  comes  to  social  life. This  indifference  towards  cleanliness  over the years has led to avoidable uncleanliness, diseases and social menaces across the coun-try. The problems built a setting where it was required  to  take  one  of  the  most  important national  decisions  ever.  The  Government  of India’s  Swachh  Bharat  Abhiyan,  today  run-ning on a large scale at Centre and State lev-els, has definitely brought advantages to peo-ple. While the Government is on the job, there is a lot the citizens have to do.

THE PROBLEM AT HAND
Epidemics  such  as  cholera,  gastroenteritis, typhoid  and  others  spread  due  to  uncleanli-ness.  Many  types  of  mosquitoes  proliferate on  rubbish  and  give  us  lethal  diseases  like malaria  and  dengue  that  take  away  many lives.  Environmental  pollution  is  another issue.  Besides,  the  trash  makes  our  villages and cities dirty and filthy.

People  staying  at  clean  and  tidy  homes are  frustrated  with  the  dirtiness  of  the  sur-rounding area and express anguish. However, these  persons  also  inadvertently  contribute to making the area dirty. We ourselves throw household  waste  out.  Thus,  a  controversy  is observed  in  humans  between  cleanliness  at home  and  the  area  around.  Observing  the unclean  area  around,  a  frustrated  man  asks questions  such  as  “What  is  the  Government doing?” and “Is the Municipal Council aware of  this  or  not?”  The  fact  is  that  the  Govern-ment is always carrying out its duties. A small number  of  local  self-government  employees are clearing wastes created by majority of the people. A man, however, places everything on them and absolves himself.

Dr. Appasaheb Dharmadhikari flanked by Chief Minister Devendra Fadnavis and other dignitaries at a cleanliness drive programme.

'''

stop_words=set(nltk.corpus.stopwords.words("english"))
#print(stop_words)
words=nltk.tokenize.word_tokenize(text)
filtered_text=[]
for w in words:
	if w not in stop_words:
		filtered_text.append(w)

print(filtered_text)

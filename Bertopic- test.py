# -*- coding: utf-8 -*-
"""

@author: roman
"""

#import spacy
import nltk


#nltk.download('punkt')

#from sklearn.datasets import fetch_20newsgroups
#docs = fetch_20newsgroups(subset='all',  remove=('headers', 'footers', 'quotes'))['data']

text = """
text
"""


docs0 = nltk.sent_tokenize(text)

docs1 = []
for nr, sent in enumerate(docs0):
    if nr%4 ==0 :
        acc_str = ""
    if nr%5 == 2:
        docs1.append(acc_str)
    else:
        acc_str = acc_str + " "+  sent
    #print(nr%5)


from bertopic import BERTopic



topic_model = BERTopic(language="english", calculate_probabilities=True, verbose=True)
topics, probs = topic_model.fit_transform(docs0)

freq = topic_model.get_topic_info(); freq.head(5)


topic_model.get_topic(4)  # Select the most frequent topic

hhtt = topic_model.visualize_topics()

html_str = hhtt.to_html()
Html_file= open("topic_clusters.html","w")
Html_file.write(html_str)
Html_file.close()



#topic_model.visualize_distribution(probs[2], min_probability=0.015)


structure_html = topic_model.visualize_hierarchy(top_n_topics=5).to_html()
Html_file= open("topic_struct.html","w")
Html_file.write(structure_html)
Html_file.close()


bar_html = topic_model.visualize_barchart(top_n_topics=5).to_html()
Html_file= open("topic_bars.html","w")
Html_file.write(bar_html)
Html_file.close()



###########


sim_html = topic_model.visualize_heatmap(n_clusters=5, width=1000, height=1000).to_html()
Html_file= open("topic_similarity.html","w")
Html_file.write(sim_html)
Html_file.close()


#############

term_score_decline = topic_model.visualize_term_rank().to_html()
Html_file= open("topic_sterm_score_decline.html","w")
Html_file.write(term_score_decline)
Html_file.close()




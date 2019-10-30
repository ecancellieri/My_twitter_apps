# Thest code for "AI for social good" project

**One part of the code generates what I call a "semantic group"**
The aim is to start from one word and to find the word most correlated with that one.
Then to download the word mostly correlated with the second one, then the words mostly correlated with the third one, etc, etc.
Until no new words are found.

For example:
0: set of words = ['Furniture]
1: Download the tweets that on a given day containing "#furniture"
2: Find the most highly ranked hashtags in this set. For example: "#design" and "#architecture".
3: Add the term "design" in the initial set: ['Furniture', 'Design']
4: Go back to step 1 using the hashtag "#Design'

Repeat until no new words are added to the set.

**The second part of the code analyses the downloaded tweets**
<p>
The first analysis consists in creating a directional graph of the semantic group:

<img src="https://github.com/ecancellieri/My_twitter_apps/blob/master/creating_semantic_group/graph_0.1.png" width="48">
![](https://github.com/ecancellieri/My_twitter_apps/blob/master/creating_semantic_group/graph_0.1.png){:height="50%" width="50%"}
<p>
Graph for "semantic group" = furniture, homedecor, interiordesign. The graph is based on the data downloaded on the 15th of October 2019

![](https://github.com/ecancellieri/My_twitter_apps/blob/master/creating_semantic_group/graph_0.2.png){:height="50%" width="50%"}
<p>
Graph for highly used hashtags. The graph is based on the data downloaded on the 15th of October 2019

![](https://github.com/ecancellieri/My_twitter_apps/blob/master/creating_semantic_group/cloud_of_words_0.1.png)
<p>
Cloud of most used words. The graph is based on the data downloaded on the 15th of October 2019


**TO DO LIST:**
- Study the graph and the cloud of words as a function of time
- Study of the links present in the downloaded tweets. Which are the most linked domains? Which is the information present in the linked pages?
- Study the "most used" expressions in the downloaded set (I.e. not just the words but also the pairs or longer groups)
- Study the retweet history to find "influencers"

This is a code to generate what I call a "semantic group"

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

After the group is created it is possible to plot it in a directional graph:

![](https://github.com/ecancellieri/My_twitter_apps/blob/master/creating_semantic_group/test_0.1.gv.png)
<p>
Directional graph for: furniture, homedecor, interiordesign. The graph is based on the data downloaded on the 15th of October 2019
# Overview
The aim of the competition is to predict a Starcraft player based on a set of behavioral traces.


# Description
Can you predict who is playing a game of Starcraft 2?
We consider the video game StarCraft 2. This real-time strategy game is played competitively by cyber-athletes as an electronic sport (esport), and most of the competitions are played online. A major issue for competition organizers is that they need to verify the identify of a player, for being sure that it is not another player (a friend with better chances, …).

For that matter, we propose to study how it is possible to determine who is playing given a behavioral trace (game events produced by the player) by designing a prediction model using machine learning techniques.

You are provided with a large set of SC2 replay data, from which you need to build features and train a model. Once your model is ready, apply it on the test data and submit your result!

Good luck and happy learning!
# Evaluation
## Evaluation metric
The evaluation metric for this competition is Mean F1-Score. The F1 score, commonly used in information retrieval, measures accuracy using the statistics precision p and recall r. Precision is the ratio of true positives (tp) to all predicted positives (tp + fp). Recall is the ratio of true positives to all actual positives (tp + fn). The F1 score is given by:
F1=2p⋅rp+r   where  p=tptp+fp,  r=tptp+fn

The F1 metric weights recall and precision equally, and a good retrieval algorithm will maximize both precision and recall simultaneously. Thus, moderately good performance on both will be favored over extremely good performance on one and poor performance on the other.


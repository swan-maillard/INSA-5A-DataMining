
## Dataset Description

## File descriptions

*   train.csv - the training set: labelled behavioral traces
*   test.csv - the test set: unlabelled behavioral traces (you need to predict the player)

## Raw input data (train.csv and test.csv)

Binary replay files have been parsed for you to produce an interpretable text file where each line denotes the actions made by one player in a single game. An example is the following:

> 5, Protoss, Base, s, s, s, s, s, t5, Base, s, hotkey30, hotkey00, t10, t15

Values are coma separated and denotes :

*   battlenetcode: The first field gives the unique ID of the player that generates the behavioral trace (given only for train.CSV)
*   played_race: The second field gives the race played (Protoss, Zerg or Terran) The rest of the fields are actions
*   Selection: a base (nexus, command center, hatchery) has been selected (sBase), a mineral has been selected (sMineral) or anything else (s).
*   Hotkey: a hotkey has been used. hotkey62 means that the button 6 (0 to 9 values possible) has been used (0=created, 1=updated, 2=used). The principle of hotkeys can be understood thanks to the picture below (Yan et. al, SIGCHI'15)
*   Fields tXX where XX is an integer that gives time windows in seconds. For example, all actions before t20 where done before 20 seconds of games, those between t20 and t30 where made in the interval \[20;30\], …  
    ![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F16350382%2F19c145b3e0895d16a7cce6a710c43ba9%2FHotkeys_yan_SIGCHI15%20Stripped.png?generation=1699002298664190&alt=media)

The number of time windows and actions varies from line to line, as players don't play at the same speed and games don't all last the same time.

**Important note**: Participants should be able to answer questions like these after reading the data description: What files do I need? What should I expect the data format to be? What am I predicting? What acronyms will I encounter?  
Be sure to know these answers, and ask the professor otherwise!

## Submission Format
An example is given:

RowId,prediction
1,2
2,5
3,64
4,128
...,...
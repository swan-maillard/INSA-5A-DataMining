# INSA-5A-DataMining
The aim of this project is to predict a Starcraft player based on a set of behavioral traces.

## Overview
```
.
├── data
│   └── Download the datasets from Kaggle here
├── agent
│   ├── data - Slighly preprocessed datasets for the agent
│   ├── prompts - Prompts for the agent
│   ├── resources - Kaggle problem overview and data description
│   └── agent.ipynb - The agent
├── ml
│   ├── notebook-rf-v0.ipynb - Random forest v0 
│   ├── notebook-rf-v1.ipynb - Random forest v1
│   ├── notebook-log-reg.ipynb - Logistic regression
│   ├── notebook-svm.ipynb - Support vector machine
│   ├── notebook-xgb.ipynb - XGBoost
│   ├── notebook-voting.ipynb - Voting classifier
│   └── notebook-stacking.ipynb - Stacking classifier
├──  LICENSE
└──  README.md 
```

## Machine Learning
For the Machine Learning part (`ml` folder), each notebook is self-contained and contains the following sections:
1. Reading datasets
2. Visualize the data
3. Preprocessing
4. Feature extraction
5. Training
6. Submission
7. Evaluation (if applicable)

## Agent-based workflow
The agent-based workflow can be executed by running the `agent.ipynb` notebook.
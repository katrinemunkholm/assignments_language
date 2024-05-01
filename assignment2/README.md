# Assignment 2 - Text classification benchmarks

- Author: Katrine Munkholm Hygebjerg-Hansen
- Elective: Visual Analytics, Cultural Data Science Spring 2024
- Teacher: Ross Deans Kristensen-McLachlan

## Description

This repository contains Python scripts for text classification benchmarks using scikit-learn. The purpose of these scripts is to train simple (binary) classification models on text data from the Fake News Dataset. The repository includes two separate scripts:

#### Logistic Regression Classifier:
- Trains a logistic regression classifier on the Fake News Dataset.
- Performs train-test split and vectorizes text data.
- Saves the classification report to a text file in the `out` folder.
- Saves the trained logistic regression classifier and vectorizer to the `models` folder.

#### MLP Classifier:
- Trains a Multi-Layer Perceptron (MLP) classifier on the same Fake News Dataset.
- Performs train-test split and vectorizes text data.
- Saves the classification report to a text file in the `out` folder.
- Saves the trained MLP classifier and vectorizer to the `models` folder.


## Data

The dataset, 'Fake or real news', is used for this analysis. 
It is a data set containing news articles along with the binary information of whether they are real or fake.
More information about the dataset as well as a download link can be found [here.](https://github.com/lutzhamel/fake-news/blob/master/README.md)


## Requirements

- python 3 
- pandas 
- scikit-learn 
- numpy 
- matplotlib 
- joblib

## Reproduction

1. The script assumes the following structure of the repository:
```
assignment2/
│
├── data/
│  └── fake_or_real_news.csv
│
├── models/
│  
├── out/
│
├── src/
│ └── utils
│ └── Log_Reg_Classifier.py
│ └── MLP_Classifier.py
│
├── requirements.txt
└── README.md
```

2. Install required packages by running the following code in the command line:

```pip install -r requirements.txt```

3. Run the scripts by executing:

``` python Log_Reg_Classifier.py ```

and / or

``` python MLP_Classifier.py ```

## Output and results

Upon running the provided scripts, the following outputs will be generated:

#### Classification Report: 
A textual summary of the performance of the classifiers, detailing metrics such as precision, recall, and F1-score for each class.
The reports offer insights into the performance of the trained classifiers. A comparative analysis of the classification reports shows that the logistic regression classifier outperforms the designed MLP, achieving an F1-score of 0.91, whereas the MLP attains a score of 0.83. 
The MLP could potentially be improved by fine tuning parameters and number of hidden layers. 

#### Trained Models: 
The trained logistic regression classifier (for the logistic regression script) or the MLP classifier (for the MLP script), saved as a .joblib file.

#### Vectorizers:
The vectorizer used to transform the text data into numerical features, saved as a .joblib file.

These outputs are saved in designated folders (out for the classification report and models for the trained models and vectorizers). 


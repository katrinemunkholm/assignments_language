
# Assignment 2 - Text Classification Benchmarks

## Description

This repository contains Python scripts for text classification benchmarks using scikit-learn. The primary aim of these scripts is to train binary classification models on the Fake News Dataset. The project includes scripts to train a logistic regression classifier and a Multi-Layer Perceptron (MLP) classifier. The outputs include classification reports, trained models, and vectorizers, each stored appropriately in the project directory.

### Task Overview

The main objectives of this assignment are:
1. Train a logistic regression classifier to categorize text data into 'fake' or 'real' news.
2. Similarly, train an MLP classifier on the same dataset.
3. Save classification reports to the `out` folder.
4. Save the trained models and vectorizers to the `models` folder.

## Data Source

The data used is the 'Fake or Real News' dataset, which includes articles categorized as 'real' or 'fake'. 
The Dataset can be downloaded [here](https://www.kaggle.com/datasets/jillanisofttech/fake-or-real-news)


## Setup and Running the Analysis

### Requirements

Ensure you have Python 3 and the following libraries installed:
`joblib==1.4.0`
`matplotlib==3.8.4`
`numpy==1.26.4`
`pandas==2.2.2`
`scikit_learn==1.4.2`
`seaborn==0.13.2`
`codecarbon==2.3.`


### Environment Setup and Execution

1. **Environment Setup**:
   To set up a virtual environment and install the required packages, run the following in the command line:
   ```bash
   bash setup.sh
   ```

2. **Running the Scripts**:
   - For Logistic Regression classifier:
     ```bash
     bash runLogReg.sh
     ```
     
   - For MLP classifier:
     ```bash
     bash runMLP.sh
     ```


## Output and results

Upon running the provided scripts, the following outputs will be generated:

#### Classification Report: 
A textual summary of the performance of the classifiers, detailing metrics such as precision, recall, and F1-score for each class.
The reports offer insights into the performance of the trained classifiers. 
A comparative analysis of the classification reports shows that the logistic regression classifier outperforms the designed MLP, achieving a weighted average F1-score of 0.91, whereas the MLP attains a score of 0.83. 
The MLP could potentially be improved by fine tuning parameters and number of hidden layers. 


#### Trained Models: 
The trained logistic regression classifier (for the logistic regression script) and the MLP classifier (for the MLP script), saved as a .joblib file.

#### Vectorizers:
The vectorizer used to transform the text data into numerical features, saved as a .joblib file.

These outputs are saved in designated folders (out for the classification report and models for the trained models and vectorizers). 

## Limitations and Possible Steps to Improvement

### Limitations

1. **Model Complexity**: The current MLP classifier uses a simple architecture, which might not capture all the nuances in complex text data. This limitation can impact the model's ability to generalize well on unseen data.
2. **Hyperparameter Optimization**: Both classifiers have been trained with a basic set of hyperparameters. This approach may not yield the best model performance, as optimal settings can vary significantly across different data sets and model architectures.
3. **Evaluation Robustness**: The evaluation methodology currently lacks the robustness that could be provided by techniques like cross-validation, which ensures that the model's performance is reliable and replicable across different subsets of the dataset.

### Future Steps to Improvement

1. **Enhance Model Architecture**: To address the complexity limitation, one could explore more sophisticated neural network architectures, such as Convolutional Neural Networks (CNNs), which are particularly well-suited for handling textual data. This could potentially lead to improved classification accuracy.
2. **Implement Cross-Validation**: To enhance the evaluation robustness, integrate k-fold cross-validation into the training process. This method involves dividing the data into k subsets and iteratively training the model k times, each time with a different subset held out for testing. This approach provides a more comprehensive assessment of model performance and helps prevent overfitting.

By addressing these limitations and implementing the suggested improvements, the classifiers' ability to accurately categorize text as 'fake' or 'real' news could be enhanced.


## File Structure

The repository is organized as follows:
```
assignment2/
│
├── data/
│   └── fake_or_real_news.csv
│
├── models/
│
├── out/
│
├── src/
│   └── utils
│   └── Log_Reg_Classifier.py
│   └── MLP_Classifier.py
│
├── README.md
├── requirements.txt
├── setup.sh
├── runLogReg.sh
└── runMLP.sh
```


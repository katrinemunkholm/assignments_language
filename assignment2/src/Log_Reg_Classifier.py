"""
Assignment 2 - Text classification benchmarks (Script for Logisitc Regression Classifier)
Author: Katrine Munkholm Hygebjerg-Hansen
Elective: Language Analytics, Cultural Data Science spring 2024
Teacher: Ross Deans Kristensen-McLachlan

"""

#Importing needed modules and libraries
import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
from joblib import dump
from codecarbon import EmissionsTracker


# Load data from CSV file
def load_data(data_path):
    """
    Args:
    data_path (str): Path to the CSV file containing text data.

    Returns:
    pd.DataFrame: DataFrame containing loaded data.
    """
    return pd.read_csv(data_path, index_col=0)


# Process text data, perform train-test split, and vectorize text.
def process_text_data(x, y):
    """
    Args:
    x (Series): Series containing text data.
    y (Series): Series containing labels.

    Returns:
    tuple: A tuple containing train-test split data and vectorized features.
    """
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    vectorizer = TfidfVectorizer(ngram_range=(1, 2), lowercase=True, max_df=0.95, min_df=0.05)
    x_train_feats = vectorizer.fit_transform(x_train)
    x_test_feats = vectorizer.transform(x_test)
    return x_train_feats, x_test_feats, y_train, y_test, vectorizer


# Train logistic regression classifier
def train_classifier(x_train_feats, y_train):
    """

    Args:
    x_train_feats: Vectorized features of the training data.
    y_train (array-like): Target labels for the training data.

    Returns:
    Trained logistic regression classifier.
    """
    classifier = LogisticRegression(random_state=42).fit(x_train_feats, y_train)
    return classifier


# Save classification report, trained models, and vectorizers to files
def save_results(out_folder, models_folder, classifier_report, classifier, vectorizer):
    """
    Args:
    out_folder (str): Path to the folder to save the classification report.
    models_folder (str): Path to the folder to save the trained models and vectorizers.
    classifier_report (str): Classification report as a string.
    classifier (LogisticRegression): Trained logistic regression classifier.
    vectorizer (TfidfVectorizer): Trained vectorizer.
    """
    if not os.path.exists(out_folder):
        os.makedirs(out_folder)
    with open(os.path.join(out_folder, "LogReg_classification_report.txt"), "w") as report_file:
        report_file.write(classifier_report)
    
    if not os.path.exists(models_folder):
        os.makedirs(models_folder)
    dump(classifier, os.path.join(models_folder, "logreg_classifier.joblib"))
    dump(vectorizer, os.path.join(models_folder, "tfidf_vectorizer.joblib"))


# Defining main() to perform task from functions
def main():
    # Defining path to folders 
    data_path = os.path.join("in", "fake_or_real_news.csv")
    out_folder = "out"
    models_folder = "models"

    # Create out directory if it does not exist
    if not os.path.exists(os.path.join("out","emissions")):
        os.makedirs(os.path.join("out","emissions"))

   # Start CodeCarbon tracker
    tracker = EmissionsTracker(project_name="Text Classification", 
                              experiment_id="text_classifier",
                              output_dir = os.path.join("out" , "emissions"))

    # Load data
    tracker.start_task("load_data")
    data = load_data(data_path)
    tracker.stop_task()

    # Creating variables
    x = data["text"]
    y = data["label"]

    # Process text data
    tracker.start_task("process_text_data")
    x_train_feats, x_test_feats, y_train, y_test, vectorizer = process_text_data(x, y)
    tracker.stop_task()

    # Train classifier
    tracker.start_task("train_classifier_logreg")
    classifier = train_classifier(x_train_feats, y_train)
    tracker.stop_task

    # Predict on test data
    tracker.start_task("prediction_logreg")
    y_pred = classifier.predict(x_test_feats)
    tracker.stop_task

    # Get classification report
    classifier_report = metrics.classification_report(y_test, y_pred)

    # Save results
    save_results(out_folder, models_folder, classifier_report, classifier, vectorizer)
   

    print("Classification report saved to 'out' folder as LogReg_classification_report.txt")
    print("Trained models and vectorizers saved to 'models' folder")

    _ = tracker.stop()

# Run main()
if __name__ == "__main__":
    main()

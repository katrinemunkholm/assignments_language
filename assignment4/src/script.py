"""
Assignment 4 - Emotion analysis with pre-trained language models
Author: Katrine Munkholm Hygebjerg-Hansen
Elective: Visual Analytics, Cultural Data Science spring 2024
Teacher: Ross Deans Kristensen-McLachlan
"""


import os
import pandas as pd
import matplotlib.pyplot as plt
from transformers import pipeline
from collections import Counter
import numpy as np

def load_data(csv_file):
    """Load data from a CSV file"""
    return pd.read_csv(csv_file)

def get_emotion_pipeline():
    """Initialize and return emotion classification pipeline"""
    return pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

def predict_emotion(text, classifier):
    """Predict emotion scores for a given text using a preloaded classifier"""
    result = classifier(text)
    return result[0]['label'], result[0]['score']

def calculate_relative_frequency(data, out_dir, classifier):
    """Calculate the relative frequency of each emotion across all seasons using a preloaded classifier"""
    total_lines = len(data)
    emotion_counts = Counter()

    seasons = sorted(data['Season'].unique())
    for season in seasons:
        season_data = data[data['Season'] == season]
        for sentence in season_data['Sentence']:
            emotion_label, _ = predict_emotion(sentence, classifier)
            emotion_counts[emotion_label] += 1

    relative_frequencies = {emotion: count / total_lines for emotion, count in emotion_counts.items()}
    counts = list(emotion_counts.values())

    colormap = plt.cm.Pastel1  # Use the same pastel colormap as in analyze_season_emotions
    color_cycle = [colormap(i) for i in np.linspace(0, 1, len(relative_frequencies))]

    # Plotting pie chart with bold fonts, colormap colors, and detailed labels
    plt.figure(figsize=(8, 8))
    plt.pie(relative_frequencies.values(), labels=relative_frequencies.keys(), colors=color_cycle,
            autopct=lambda p: f'{p:.1f}%\n({int(p/100*total_lines)})', textprops={'weight': 'bold'})
    plt.title("Relative Frequency of Emotions Across All Seasons", fontdict={'weight': 'bold'})
    plt.savefig(os.path.join(out_dir, "relative_frequency_emotions.png"))
    plt.close()

    return relative_frequencies


def analyze_season_emotions(data, out_dir, classifier):
    """Analyze the emotional profile for each season using the preloaded classifier"""
    seasons = sorted(data['Season'].unique())
    colormap = plt.cm.Pastel1  # Use a pastel colormap
    for season in seasons:
        season_data = data[data['Season'] == season]
        emotions = []
        for sentence in season_data['Sentence']:
            emotion_label, _ = predict_emotion(sentence, classifier)
            emotions.append(emotion_label)
        
        # Get unique emotion labels and their counts
        unique_emotions, emotion_counts = np.unique(emotions, return_counts=True)
        color_cycle = [colormap(i) for i in range(len(unique_emotions))]
        
        # Plotting pie chart with bold fonts and detailed labels
        plt.figure(figsize=(8, 8))
        plt.pie(emotion_counts, labels=unique_emotions, colors=color_cycle, autopct=lambda p: f'{p:.1f}%\n({int(p/100*len(emotions))})', textprops={'weight': 'bold'})
        plt.title(f"{season} Emotion Distribution", fontdict={'weight': 'bold'})
        
        # Save the plot
        plt.savefig(os.path.join(out_dir, f"{season}_emotion_distribution.png"))
        plt.close()

def main():
    csv_file = "../in/Game_of_Thrones_Script.csv"
    data = load_data(csv_file)
    out_dir = "../out"
    classifier = get_emotion_pipeline()
    
    analyze_season_emotions(data, out_dir, classifier)
    calculate_relative_frequency(data, out_dir, classifier)

if __name__ == "__main__":
    main()

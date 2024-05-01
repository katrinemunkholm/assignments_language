"""
Assignment 3 - Query expansion with word embeddings
Author: Katrine Munkholm Hygebjerg-Hansen
Elective: Visual Analytics, Cultural Data Science spring 2024
Teacher: Ross Deans Kristensen-McLachlan

"""

# Loading necessary libraries and modules
import sys
import os
import argparse
import pandas as pd
import numpy as np
import gensim
import gensim.downloader
import gensim.downloader as api
from gensim.models import KeyedVectors
model = api.load("glove-wiki-gigaword-50")

# Add parent directory to python module path
sys.path.append(os.path.join('..'))


# Defining function to load data. File path is specified in main()
def load_lyric_data(file_path):
    """
    Args:
    - file_path: Path to the CSV file containing the data.

    Returns:
    - DataFrame: Loaded data as a pandas dataFrame.
    """
    data = pd.read_csv(file_path)
    return data


# Expand the query by finding the most similar words using word embeddings.
def expand_query(model, search_term, top_n=5):
    """
    Args:
    - model (KeyedVectors): Pre-trained word embedding model.
    - search_term (str): The target word for query expansion.
    - top_n (int): Number of similar words to retrieve.

    Returns:
    - list: Expanded query terms.
    """
    try:
        similar_words = model.most_similar(search_term, topn=top_n)
        expanded_query = [word for word, _ in similar_words]
        return expanded_query
    except KeyError:
        print(f"Error: '{search_term}' not found in the vocabulary.")
        return []


# Calculate the percentage of songs by a given artist containing words related to the expanded query.
def calculate_percentage(data, artist, expanded_query):
    """
    Args:
    - data: Song lyric data, [text] in dataset.
    - artist: Name of the artist. [artist] in dataset.
    - expanded_query: Expanded query terms.

    Returns:
    Percentage of songs by the artist containing words related to the expanded query.
    """
    # Finds total no. of songs by artist in dataset
    artist_songs = data[data['artist'] == artist]
    total_songs = len(artist_songs)
    
    # Count songs containing words related to the expanded query
    songs_with_terms = artist_songs['text'].str.contains('|'.join(expanded_query), case=False).sum()
    
    # Calculate percentage in dataset
    percentage = (songs_with_terms / total_songs) * 100 if total_songs != 0 else 0
    return percentage

# Save results to a CSV file. Append new results to existing CSV
def save_to_csv(Search_results, output_file):
    """
    Args:
    - Search_results: Dictionary containing the results.
    - output_file: Path to the output CSV file.
    """
    if not os.path.exists(os.path.dirname(output_file)):
        os.makedirs(os.path.dirname(output_file))

    # Check if the file exists
    if os.path.isfile(output_file):
        # Append to the existing file
        df = pd.read_csv(output_file)
        df = df._append(Search_results, ignore_index=True)
    else:
        # Create a new file with headers
        df = pd.DataFrame([Search_results])

    # Save to CSV
    df.to_csv(output_file, index=False)

# Defining a main() to run the task using the functions from the script
def main():
    # Argument parsing
    parser = argparse.ArgumentParser(description="Query expansion with word embeddings")
    parser.add_argument("--artist", type=str, help="Name of the artist", required=True)
    parser.add_argument("--search-term", type=str, help="Target word for query expansion", required=True)
    args = parser.parse_args()

    # Load the song lyric data
    data = load_lyric_data("../in/Spotify Million Song Dataset_exported.csv")

    # Load the word embedding model
    model = api.load("glove-wiki-gigaword-50")

    # Expand the query
    expanded_query = expand_query(model, args.search_term, top_n=5)

    if expanded_query:
        # Calculate the percentage of songs by the artist containing words related to the expanded query
        percentage = calculate_percentage(data, args.artist, expanded_query)
        print(f"{percentage:.2f}% of {args.artist}'s songs contain words related to {args.search_term} and similar terms.")

        # Prepare results dictionary
        Search_results = {'artist': args.artist, 'Search Term': args.search_term, 'Percentage': percentage}

        # Save results to CSV
        output_file = "../out/Search_results.csv"
        save_to_csv(Search_results, output_file)
        print("Results saved to:", output_file)
    else:
        print("Query expansion failed. Please try another search term.")

if __name__ == "__main__":
    main()

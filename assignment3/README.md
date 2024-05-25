# Assignment 3 - Query Expansion with Word Embeddings

## Description

This repository contains a script for query expansion with word embeddings on a corpus of song lyrics. The process involves selecting a keyword, finding terms related to this keyword using the "glove-wiki-gigaword-50" model from Gensim, and computing how many songs by a given artist contain any of these terms.

### Task Overview

The primary objectives of this assignment are:
1. Load song lyrics data.
2. Utilize a pre-trained word embeddings model to expand a given query.
3. Calculate the percentage of songs by a specified artist that include terms related to the expanded query.
4. Output and save these results in a structured format.

## Data Source

The dataset used is the "57,650 English-language songs" corpus, which can be accessed for download [here] (https://www.kaggle.com/datasets/joebeachcapital/57651-spotify-songs)

### Environment Setup and Execution

1. **Environment Setup**:
To set up a virtual environment and install the required packages, run the following in the command line:

```bash
bash setup.sh
```

2. **Running the Script**:
To run the script, run the following command and write arguments of your choice:

```bash
bash run.sh --artist "Artist Name" --search-term "Search Term"
```

***Example: bash run.sh --artist "Michael Jackson" --search-term "world"***

### Command Line Arguments

The script accepts and requires the following command line arguments:
- `--artist`: Specifies the artist to analyze.
- `--search-term`: The keyword for which to expand the query.

## Summary of Key Points from the Outputs

The outputs include the percentage of songs by the specified artist that contain words related to the expanded query term. These results are printed on the console and saved to a CSV file in the `out` directory.

Example of results:

| Artist            | Search Term | Percentage          |
|-------------------|-------------|---------------------|
| Justin Timberlake | baby        | 68.33               |
| Justin Bieber     | baby        | 54.96               |
| Madonna           | love        | 98.86               |
| Khruangbin        | love        | 0.00                |
| Stevie Wonder     | life        | 89.93               |
| Michael Jackson   | world       | 66.48               |

Where 'Percentage' specify the percentage of songs by the artist that contain words related to the search term.
A result of 0.00%, as for Khruangbin, likely indicates that the dataset does not include any lyrics from Khruangbin. 

## Discussion of Limitations and Possible Steps to Improvement

The current implementation relies on a specific word embedding model, which may limit its applicability to diverse linguistic contexts or slangs in lyrics. Future improvements could include:
- Using different or multiple embedding models to capture a broader range of linguistic nuances.
- Implementing more complex query expansion techniques such as semantic similarity.
- Implementing a statement to check if the artist exists in the dataset.

## File Structure

The expected file structure for running this script is as follows:
```
assignment3/
│
├── in/
│   └── SpotifyMillionSongDataset_exported.csv
│
├── out/
│   └── Search_results.csv
│
├── src/
│   └── Lyrics_search.py
│
├── README.md
├── requirements.txt
├── setup.sh
└── run.sh
```

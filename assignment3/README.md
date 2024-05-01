# Query Expansion with Word Embeddings

- Author: Katrine Munkholm Hygebjerg-Hansen
- Elective: Visual Analytics, Cultural Data Science Spring 2024
- Teacher: Ross Deans Kristensen-McLachlan

## Description

This script performs query expansion with word embeddings on a corpus of song lyrics. It allows users to specify an artist and a target word for query expansion, and then calculates the percentage of songs by that artist containing words related to the expanded query. The script utilizes pre-trained word embeddings from the "glove-wiki-gigaword-50" model via Gensim.


## Features

- **Loading Data:** The script loads song lyric data from a CSV file.
- **Query Expansion:** It expands the query by finding the most similar words using word embeddings. This number is set to "5", meaning that it includes the 5 words that are most similar to the search term in the search.
- **Percentage Calculation:** It calculates the percentage of songs by a given artist containing words related to the expanded query.
- **Results Saving:** The results are saved to a CSV file, with new results appended to the existing file.

## Reproduction

The script assumes the following structure of the repository:
```
assignment3/
│
├── data/
│ └── SpotifyMillionSongDataset_exported.csv
│ 
├── out/
│     └── Search_results.csv
│ 
├── src/
│ └── env
│ └── Lyrics_search.py
│
├── requirements.txt
└── README.md
```

1. Install required packages by running the following code in the command line:

```pip install -r requirements.txt```


2. To run the script, use the following command:

```bash
python Lyrics_search.py --artist "Artist Name" --search-term "Search Term"
```

## Output

After running the script, the following output is displayed:

- The percentage of songs by the specified artist containing words related to the search term and similar terms is printed to the console.
- If the query expansion is successful and results are saved to the CSV file, a confirmation message indicating the location of the saved file is displayed.

Example Output:
"68.33% of Justin Timberlake's songs contain words related to baby and similar terms."
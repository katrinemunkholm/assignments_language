# Assignment 1 - Linguistic Feature Extraction using spaCy

- Author: Katrine Munkholm Hygebjerg-Hansen
- Elective: Language Analytics, Cultural Data Science, Spring 2024
- Teacher: Ross Deans Kristensen-McLachlan


## Description

This repository contains a Python script designed for extracting linguistic features from the Uppsala Student English Corpus (USE). The script leverages the spaCy library to analyze the frequency and diversity of grammatical categories in the text data, as well as identifying unique named entities. The main objective is to facilitate linguistic analysis across multiple texts, generating insights into the usage of nouns, verbs, adjectives, adverbs, and named entities like persons, locations, and organizations.

### Task Overview

The task involves:
- Parsing through each text file in the 'in' folder.
- Computing the relative frequency per 10,000 words of various parts of speech (nouns, verbs, adjectives, adverbs).
- Counting the total number of unique named entities categorized into persons, locations, and organizations.
- Storing the results in CSV files, one for each sub-folder in the 'in' directory, containing linguistic metrics for each file.

## Data Source

The data used in this analysis is the Uppsala Student English Corpus (USE), a comprehensive collection of essays written by Swedish university students. More detailed documentation and access to the corpus can be found [here](https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/2457).

The USEcorpus can be downloaded directly [here](https://ota.bodleian.ox.ac.uk/repository/xmlui/bitstream/handle/20.500.12024/2457/USEcorpus.zip?sequence=5&isAllowed=y)

See file structure below to name and place the downloaded folder correctly. 


## Setup and Running the Analysis

### Requirements

Ensure Python 3 and the following libraries are installed:
- `pandas`
- `spacy` (with `en_core_web_md` model)
- `pandas==2.2.`
- `spacy==3.7.`
- `codecarbon==2.3.5`


### Environment Setup and Execution

1. **Environment Setup**:
   To set up a virtual environment and install the required packages, run the following in the command line:
   ```bash
   bash setup.sh
   ```

2. **Running the Script**:
     ```bash
     bash run.sh
     ```


### Command Line Arguments

The script supports,but doesn't require, the following command line arguments to customize its execution:
- `--data-path`: Path to the USE corpus directory (default is `in/USEcorpus`)
- `--output-dir`: Directory where output CSV files are saved (default is `out`)

## Summary of Key Points from the Outputs

The output consists of CSV files for each subfolder in the 'in' directory. Each file details:
- Relative frequencies of nouns, verbs, adjectives, and adverbs.
- Counts of unique named entities (persons, locations, organizations).

There is a noticeable increase in unique organization mentions from the first term to the second term. For example, a3 essays have minimal organization mentions, while b3 essays average 3.07 unique organizations per text, with a maximum of 66 in one essay. This increase likely reflects the students' progression and increased engagement with more complex, research-oriented topics in their second term.

## Discussion of Limitations and Possible Steps to Improvement

### Limitations
- The analysis is based solely on the lexical categories and named entities recognized by spaCy, which may not cover all relevant linguistic aspects.
- Performance and accuracy are dependent on the spaCy model's capabilities and the characteristics of the text data.

### Future Steps
- Implement additional linguistic feature extraction, such as syntactic complexity measures.
- Integrate more robust data cleaning processes to handle various text anomalies.

## File Structure

The repository is structured as follows:
```
assignment1/
│
├── in/
│   └── USEcorpus/
│       └── a1/
│       └── a2/
│       └── ...
├── out/
│   └── a1_linguistic_information.csv
│   └── a2_linguistic_information.csv
│   └── ...
├── src/
│   └── script_linguistic_features.py
├── setup.sh
├── run.sh
├── README.md
├── requirements.txt
```

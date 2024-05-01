# Linguistic Feature Extraction using spaCy

- Author: Katrine Munkholm Hygebjerg-Hansen
- Elective: Visual Analytics, Cultural Data Science Spring 2024
- Teacher: Ross Deans Kristensen-McLachlan

## Description

The script "script_linguistic_features.py" performs linguistic analysis on text files using SpaCy. The USECorpus is analyzed for this project. 
Tables with lingustic information is saved for each subfolder of the corpus, allowing the reader to gain insights into the linguistic contents of the files, namely the relative frequency of nouns, verbs, adjectives and adverbs per 10,000 words as the as total number of unique PER, LOC and ORG entities. 

The script does the following:

#### Loading Packages:
Imports necessary packages such as os, pandas, spacy, and re.

#### Defining Functions:
clean_text(text): Removes HTML tags from the input text.
processing_text(file_path): Processes the text in a file, extracting linguistic features such as part-of-speech (POS) tags and named entities.

#### Main Function:
Defines paths to input and output directories.
Iterates through subfolders within the input directory, processing each text file.
Generates a DataFrame containing linguistic features for each text file.
Saves the DataFrame as a CSV file in the output directory with the name "{subfolder}_linguistic_information.csv".
Prints a confirmation message for each folder processed.

#### Execution:
Executes the main() function when the script is run directly.
Performs linguistic analysis on the text data within the subfolders and saves the results as CSV files.


## Data

The data used for this feature extraction is the USEcorpus, which consist of text files arranged in 14 subfolders.
The corpus consists of 1,489 essays written by 440 Swedish university students of English at three different levels, the majority in their first term of full-time studies. The total number of words is 1,221,265, which means an average essay length of 820 words. A typical first-term essay is somewhat shorter, averaging 777 words.
More info as well as the download link can be accessed [here.](https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/2457)


## Requirements

- Python > 3.10.12
- `pandas` library
- `spacy` library
- `en_core_web_md` model for spaCy (downloadable using `python -m spacy download en_core_web_md`)

## Reproduction


1. The script assumes the following structure of the repository:
```
assignment1/
│
├── in/
│ └── USEcorpus
│   └── a1
│      └── 0100.a1.txt
│      └── 0101.a1.txt
│      └── ...
│   └── a2
│      └── 0100.a2.txt
│      └── 0101.a2.txt
│      └── ...
│   └── ...
│
├── out/
│
├── src/
│ └── script_linguistic_features.csv.py
│
├── requirements.txt
└── README.md
```

2. Install required packages by running the following code in the command line:

```pip install -r requirements.txt```


3. Download spaCy model by running the following in the command line:

```python -m spacy download en_core_web_md```


4. Run the script by executing:

``` python script_linguistic_features.py ```

## Output

The data after processing is stored as CSV files within the `out` directory. In total, there are 14 CSV files, one corresponding to each subfolder.
Information about relative frequency of nouns, verbs, adjectives and adverbs are stored as well as number of unique PER(persons), LOC(locations) and ORG(organizations) entities.



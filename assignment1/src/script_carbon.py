"""
Assignment 1 - Linguistic Analysis with SpaCy
Author: Katrine Munkholm Hygebjerg-Hansen
Elective: Visual Analytics, Cultural Data Science Spring 2024
Teacher: Ross Deans Kristensen-McLachlan

"""

# Loading in packages
import os
import pandas as pd
import spacy
import re
from codecarbon import EmissionsTracker

# Loading spacy
## Download spaCy module by: python -m spacy download en_core_web_md
nlp = spacy.load("en_core_web_md")


# Defining functions

# Cleaning the text
def clean_text(text):
    return re.sub(r'<.*?>', '', text)

#  Function for processing the text
def processing_text(file_path):
     # Opening file, cleaning the text and loading into spacy and creating a doc object
    with open(file_path, "r", encoding="latin-1") as file:
        # Read the content of the file and name of the file
        text = clean_text(file.read())
        
    doc = nlp(text)
    
    # Making dictonaries for the POS tags and entities
    pos_tags = {"NOUN": 0, "VERB": 0, "ADJ": 0, "ADV": 0}
    unique_entities = {"PER":0, "LOC":0, "ORG":0}
    
    # Looping through the tokens for the pos tags and entities
    for token in doc:
        if token.pos_ in pos_tags:
            pos_tags[token.pos_] += 1
    
    for ent in doc.ents:
        if ent.label_ in unique_entities:
            unique_entities[ent.label_] += 1
        
    # Calculating the relative frequency of the pos tags
    total_pos = sum(pos_tags.values())
    relative_freq_pos = {key : value/total_pos for key, value in pos_tags.items()}
    
    # Arranging the data in a dictionary
    data = {
        "Relative Frequency of NOUN": relative_freq_pos.get("NOUN", 0),
        "Relative Freqency of VERB": relative_freq_pos.get("VERB", 0),
        "Relative Freqency of ADJ": relative_freq_pos.get("ADJ", 0),
        "Relative Freqency of ADV": relative_freq_pos.get("ADV", 0),
        "Unique PER": unique_entities.get("PER", 0),
        "Unique LOC": unique_entities.get("LOC", 0),
        "Unique ORG": unique_entities.get("ORG", 0)
    }
    
    return data

# Defining main() function to run the functions 
def main():
    # Defining path to folders 
    data_path = os.path.join("in", "USEcorpus")
    output_path = os.path.join("out")
    dirs = sorted(os.listdir(data_path))

    # Create out directory if it does not exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    all_emissions_data = []

    # Looping through the folders and creating a dataframe for each folder that contains the relative frequency of the pos tags and the unique entities for each text file
    for directory in dirs:
        subfolder = os.path.join(data_path, directory)
        filenames = sorted(os.listdir(subfolder))

        results = []

        # Initialize emissions tracker for each assignment
        tracker = EmissionsTracker(project_name=f"emissions_{directory}", 
                                   experiment_id=f"emissions_{directory}",
                                   output_dir=os.path.join(output_path),
                                   output_file=f"emissions.csv")
        tracker.start()

        for text_file in filenames:
            file_path = os.path.join(subfolder, text_file)
            file_data = processing_text(file_path)

            results.append({"Filename": text_file, **file_data})

        df = pd.DataFrame(results)
        # Saving as a csv file
        df.to_csv(os.path.join(output_path, f"{directory}_linguistic_information.csv"), index=False)

        # Stop tracking emissions for the assignment
        tracker.stop()

        # Print statement for the user of the progress
        print(f"A .csv file with linguistic features of {directory} folder has been successfully saved in the folder 'out'")



if __name__ == "__main__":
    main()

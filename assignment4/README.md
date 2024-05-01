# Emotion Analysis in Game of Thrones 

- **Author**: Katrine Munkholm Hygebjerg-Hansen
- **Elective**: Visual Analytics, Cultural Data Science Spring 2024
- **Teacher**: Ross Deans Kristensen-McLachlan

## Description

This script conducts text classification for emotions using pre-trained language models via HuggingFace. The analysis aims to explore the emotional expressions in the dialogues of 'Game of Thrones' across its seasons, as expressed by the characters. It seeks to understand the distribution of these expressed emotions. The script predicts emotion scores for each line in the dataset and then visualizes the emotional distribution for each season. Additionally, it plots the relative frequency of each emotion label across all seasons.

## Features

- **Data Loading**: The script loads dialogue data from a CSV file which includes metadata about who spoke each line and the context of the dialogue.
- **Emotion Prediction**: Each line of dialogue is analyzed to predict the underlying emotion using a pretrained emotion classification model.
- **Seasonal Emotion Analysis**: The script plots the distribution of emotion labels for each season to visualize how emotional expressions change over time.
- **Overall Emotion Frequency Calculation**: It calculates and visualizes the relative frequency of each emotion across all seasons.
- **Output Generation**: The results, including charts for each season and the overall series, are saved in a specified output directory.

## Reproduction

The script assumes the following structure of the repository:
```
assignment4/
│
├── data/
│ └── Game_of_Thrones_Script.csv
│ 
├── out/
│    └── relative_frequency_emotions.png
│    └── Season1_emotion_distribution.png
│    └── Season2_emotion_distribution.png
│    └── ...
│ 
├── src/
│ └── script.py
│
├── requirements.txt
└── README.md
```

1. Install required packages by running the following code in the command line:

```bash
pip install -r requirements.txt
```

2. To run the script, use the following command:

```bash
python script.py
```

## Output

After running the script, the following outputs are generated: 

- Pie charts for each season showing the distribution of emotions.
- A pie chart showing the relative frequency of each emotion throughout all seasons.
- The charts are saved in the `out` directory under the appropriate filenames indicating the type of analysis.


## Example Output

- `Season 1_emotion_distribution.png`: Shows the emotional distribution in Season 1.
- `relative_frequency_emotions.png`: Shows the relative frequencies of emotions across all seasons.


## Results and interpretation

Upon reviewing the plots for each season's emotion distribution, it appears that the distributions remain fairly consistent across the series. A significant majority of the lines, representing 48.1%, are categorized as 'neutral'. Other notable emotions identified in the analysis include surprise and anger. It’s crucial to note that these labels reflect the emotions expressed in the dialogues by the characters and should not be directly equated to the viewers’ emotional reactions. For example, although 11.5% of lines are labeled as "surprise," this does not necessarily indicate the presence or absence of surprising elements in the show, nor does it suggest that the intensity of surprise remains constant across different seasons.

In summary, while the emotional distribution does not show substantial variation, I am cautious about drawing any definitive conclusions regarding the overall emotional trajectory of the series based on this data alone.

# Project Overview

**All-in-One.py** is an advanced real-time facial analysis tool designed to capture live video feed and deliver comprehensive insights into individuals' emotional states and demographic attributes. This Python script not only detects emotions, gender, age, and race in real time but also provides accurate identification of individuals by name. Powered by the DeepFace library, **All-in-One.py** offers a unified solution for facial recognition and attribute analysis.

## Key Features

- **Real-time Attribute Detection:** **All-in-One.py** captures live video feed and performs real-time analysis, displaying attributes such as emotions, gender, age, and race of individuals.

- **Person Identification:** Before running the program, users create a folder within the 'photos' directory named after the person and add three photos of the individual. During execution, the program accurately identifies individuals based on the provided photos.

- **Customizable Deep Learning Models:** Users can choose their preferred deep learning model and backend connector for facial analysis. The program supports various models and connectors, allowing users to tailor the analysis to their specific requirements.

## Usage

1. **Prepare the Photos Folder:**
   - Create a folder within the 'photos' directory with the person's name.
   - Add three photos of the person inside this folder.

2. **Run the Program:**
   - Execute the script in your Python environment.
   - Choose the deep learning model and backend connector based on your preference.
   - The program will start capturing the live video feed and display real-time attribute analysis.

3. **View Real-time Analysis:**
   - The program displays the live video feed with overlays showing emotions, gender, age, and race of individuals.
   - Based on the cosine similarity score, the person's name (corresponding to the highest similarity) is accurately listed.

## Customization

The program allows users to customize the deep learning model and backend connector used for facial analysis. Choose the most suitable model and connector based on your performance and resource requirements.


## The other files ('Emotion Detector.py, Live Stream Identifier.py and Person Name Finder.py) are simply parts of the main 'all in one.py' py created to understand the whole code in parts if needed.

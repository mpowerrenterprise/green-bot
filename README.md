# GreenBot


## Repo Structure

    ├── docs                                   # Contains documents  
    ├── research                               # Contains pre-research. 
    ├── source                                 # Contains project source code.
    │   ├── main.py                                # Main app file
    │   ├── train.py                               # To train the model.
    └── README.MD                              # Readme Content.
    

## Introduction

A simple machine learning-based chatbot prototype, this repository showcases an interactive conversational agent built using natural language processing techniques. Designed to demonstrate the fundamental principles of machine learning in dialogue systems, the chatbot can understand user inputs and generate appropriate responses. This project is perfect for those looking to explore the basics of creating intelligent chatbots, from data preprocessing and model training to deploying a functional conversational AI.

![alt text](docs/media/2.png)

## Technology Stack

- Python 3.8
- Pickle
- NLTK
- Tensorflow
- TFLearn

## Setup

- Step 01: Install Python

  ```
    https://python.org/
  ```

- Step 02: Navigate to docs folder

  ```
     cd docs
  ```

- Step 03: Install the requirements.txt

  ```
      pip install -r requirements.txt
  ```


- Step 04: (Anaconda Env Only): Install the environment.yml if you are using Anaconda.

  ```
      conda env create -f environment.yml
  ```

  - Step 04: Install NLTK Models

  ```
      Open CMD
      Type: Python
      Type: import nltk
      Type: nltk.download('punkt')
  ```

## Usage

### Launch the app

- Step 01: Navigate to source folder

  ```
     cd source 
  ```

- Step 02: Run train.py

  ```
      python train.py 
  ```

- Step 03: Run main.py

  ```
      python main.py 
  ```

## Output

![alt text](docs/media/output.PNG)

## Development

### Retrain the model

- Step 01: Open **"source/dataset/intents.json"** and your data according to the format.

  ```
      python main.py 
  ```

- Step 02: Navigate to **source** folder

  ```
      cd source
  ```

- Step 02: Run train.py to start training

  ```
      python train.py
  ```

   
## Documentation

### Sample Chat Inputs

- Command 1: What is Your Name ?
- Command 2: What is Your Age ?
- Command 3: Do you like nature?
- Command 5: Do you go to school?
- Command 6: Do you have a pet?
- Command 6: Do you enjoy art?



# Contact

### 🌐 Website:
[![Visit](https://img.shields.io/badge/Visit%3A%20www.mpowerr.com-%23007ACC?style=flat&logo=google-chrome&logoColor=white&labelWidth=200)](https://www.mpowerr.com)

---

### 📱 Social Media:

[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/company/mpowerr-info)
[![Facebook](https://img.shields.io/badge/Facebook-%231877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.com/mpowerr.info)
[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/mpowerr.info)
[![X (Twitter)](https://img.shields.io/badge/X-%231DA1F2?style=for-the-badge&logo=x&logoColor=white)](https://x.com/MpowerrInfo)
[![TikTok](https://img.shields.io/badge/TikTok-%23000000?style=for-the-badge&logo=tiktok&logoColor=white)](https://www.tiktok.com/@mpowerr.info)
[![YouTube](https://img.shields.io/badge/YouTube-%23FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@mpowerrinfo)

---

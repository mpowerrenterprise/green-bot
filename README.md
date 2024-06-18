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

### Website: 

[![Visit](https://img.shields.io/badge/Visit%3A%20www.gunarakulan.info-%23E01E5A?style=flat&logo=realm&logoColor=white)](https://www.gunarakulan.info)

### Social Media:

[![LinkedIn](https://img.shields.io/badge/-LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gunarakulangunaretnam)
[![Facebook](https://img.shields.io/badge/-Facebook-196dcc?style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.com/gunarakulangunaretnam)
[![WhatsApp](https://img.shields.io/badge/-WhatsApp-07a647?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/94740001141?text=WhatsApp%3A%20%2B9740001141)
[![Instagram](https://img.shields.io/badge/-Instagram-bd3651?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/gunarakulangunaretnam)
[![X.COM](https://img.shields.io/badge/-X.COM-0066ff?style=for-the-badge&logo=x&logoColor=white)](https://x.com/gunarakulangr)
[![Kaggle](https://img.shields.io/badge/-Kaggle-3295bd?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/gunarakulangr)
[![TikTok](https://img.shields.io/badge/-TikTok-579ea3?style=for-the-badge&logo=tiktok&logoColor=white)](https://www.tiktok.com/@gunarakulangunaretnam)
[![YouTube](https://img.shields.io/badge/-YouTube-a82121?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/channel/UCjMOdgHFAjAdBKiqV8y2Tww)
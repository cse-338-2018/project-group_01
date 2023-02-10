# Project - Group 01
### Team Name - TeamUno
### Project Title - Similarity Analyzer (UnoCheck)


## About UnoCheck 
The UnoCheck application employs AI technology that leverages Natural Language Processing (NLP) and machine learning algorithms to evaluate the similarity between two or more articles. The application works by taking an article, comparing it with existing research articles, and then identifying similar articles with similarity percentage.

\
\
<img width="1440" alt="image" src="https://user-images.githubusercontent.com/52996563/216214340-c07a8eb3-ce00-4522-b36b-53571ba6851d.png">


## Motivation Behind Project
The Internet has brought a vast source of resources to our fingertips. With so much content available, it’s sometimes hard to know when something has been plagiarized. Moreover, similarity analyzer is used in recommendation systems, finding relevance among documents and so on. From authors checking for their posts being stolen and posted elsewhere to checking for recommendations,  similarity analyzer has become a must nowadays.

## Overview
The application contains the interface of text area for checking. In order to analyze, simply copy and paste the text in the text area and click the analyze button. Then the result will be shown on screen after a few moment.
<img width="481" alt="image" src="https://user-images.githubusercontent.com/52996563/218121730-4d912970-f2a8-40d4-ac59-7e810e3e7b52.png">


The result consists of a table of some papers which have:
- Abstract header of the paper
- Similarity percentage
- View button

After pressing the View button, the abstract of the research paper will be shown.
<img width="481" alt="image" src="https://user-images.githubusercontent.com/52996563/218104188-05c7922b-e938-4c32-b518-d9d969b8d8d9.png">



## Prerequisites 
Install the followings in this order. (NB. If already installed then update it to latest version)
1. any IDE software for python
2. Python3
3. pip
4. Flask
5. nltk
6. punkt
## Starter 
- Clone the project. 
- Download the dataset from the [link](https://drive.google.com/file/d/1n2JtTLAiDpcYx6u-PMTKIBo7S3BZ3FPv/view?usp=sharing). You will get a file named as **combined.csv**. Put this file in the project structure.
- Run the project by the below commands
```
python3 -m venv .venv
source .venv/bin/activate
python3 app.py
```
- It would take time to run server depending on your GPU. 
## Updating Dataset 

- Replace the existing combined.csv file by your csv file .
- Your csv file must contain one column named abstract.
- Run model.py by the below commands.
```
python3 -m venv .venv
source .venv/bin/activate
python3 model.py
```

 ## Developers
#### **Ananna Dristy**
       Email - anannadristy03@gmail.com
       Github Profile - Dristy03
       Contribution - Building Model
       Reg - 2018331049
#### **Kawchar Husain**
       Email - kawsarhn1@gmail.com
       Github - kawchar85
       Contribution - Model Processing
       Reg - 2018331085
#### **Kaifa Tabassum**
       Email - tabassumkaifa2@gmail.com
       Github - kaifatab
       Contribution - Dataset Preparation
       Reg - 2018331037
#### **Omar Sultan**
       Email - omarsultan@gmail.com
       Github - omarsultan054
       Contribution - Application
       Reg - 2018331077
#### **Debpriya Dhar**
       Email - debpriya.susmoy1999@gmail.com
       Github - debpriya65
       Contribution - Application
       Reg - 2018331065


# UET-Hackathon-2022

## Preparing Data:
- Use [Wordcloud analysis model](https://www.kaggle.com/code/aashita/word-clouds-of-various-shapes/notebook) to make the model understand the meaning of aspects like **address**, **job/role**.
- Clean the data:
    * Fill the **Null** values of "worker's address" columns by the "flexible location".
    * Fill the **Null** values of "job/role" columns by "unemployeed"
    * Fill the **Null** values of "office's address" columns by the address of the office with the same *id_office*
    * Represent the "work experience" of a person by a point in hyperspace

# UET-Hackathon-2022

## Preparing Data:
- Use [Word2Vec model](https://rare-technologies.com/word2vec-tutorial/) to make the model understand the meaning of aspects like **address**, **job/role**.
- Clean the data:
    * Fill the **Null** values of "worker's address" columns by "NA"
    * Fill the **Null** values of "job/role" columns by "NA"
    * Fill the **Null** values of "office's address" columns by the address of the office with the same *id_office*
    * Represent the "work experience" of a person by a point in hyperspace

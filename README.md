# Book Recommendation System using Jaccard Similarity

This Python code implements a simple recommendation system that utilizes the Jaccard similarity metric to find the best match for a given set of text documents. The code processes a collection of text files, calculates Jaccard similarity between them, and then displays the best matching documents in a user-friendly GUI using the Tkinter library.

## Table of Contents

- [Introduction](#introduction)
- [How it Works](#how-it-works)
- [Requirements](#requirements)
- [Usage](#usage)
- [Results](#results)
- [Run it](#How-to-run-it)

## Introduction

The recommendation system in this code is designed to find the best matching documents among a collection of text files. It is particularly useful for tasks such as recommending similar books, articles, or any other textual content based on their content.

The Jaccard similarity is used to measure the similarity between two sets by comparing their intersection and union. In this code, it is employed to determine the similarity between the word sets of different documents.

## How it Works

1. **Data Preparation**: The system begins by loading a collection of text documents (e.g., books) from a specified directory. It reads the content of each document and preprocesses it, including removing stop words and non-alphabetic characters.

2. **Jaccard Similarity Calculation**: The code then calculates the Jaccard similarity between all pairs of documents. It keeps track of the best matching document for each document based on the Jaccard similarity scores.
3. <img src="https://github.com/GurpreetSingh97/Book_recommendation_system/blob/main/screenshots/algo.png" alt="alt text" width="400" height="whatever">

4. **GUI Display**: The results are displayed in a user-friendly GUI created using the Tkinter library. The GUI shows a list of documents and their best matching documents based on Jaccard similarity.

## Requirements

- Python 3.x
- Tkinter library (usually included in Python installations)
- Text files to process (e.g., books)

## Usage

1. Ensure you have the required dependencies installed.

2. Organize your text documents in a directory, or use the default directory provided in the code (./books).

3. Create a text file named "StopWords.txt" containing common stop words, one word per line. These words will be filtered out during processing.

4. Run the code.

5. The GUI window will display the best matching documents for each document in the collection based on Jaccard similarity.

## Results

The GUI will display a table with two columns:

- **Book Name**: The name of the document for which a match is being sought.
- **Best Match**: The name of the best-matching document based on Jaccard similarity.

<img src="https://github.com/GurpreetSingh97/Book_recommendation_system/blob/main/screenshots/output.png" alt="alt text" width="400" height="whatever">  

You can use this information to recommend similar documents to users or for any other relevant application.


## How to run it
1. Download the [Book_recommendation_system](https://github.com/GurpreetSingh97/Book_recommendation_system) repository.  
2.  Compile and run the [main.py](https://github.com/GurpreetSingh97/Book_recommendation_system) file.  
3.  Choose the folder where all the files are located which needs to compared for recommendation. ([Book](https://github.com/GurpreetSingh97/Book_recommendation_system/tree/main/books) folder has some file for demo run.)

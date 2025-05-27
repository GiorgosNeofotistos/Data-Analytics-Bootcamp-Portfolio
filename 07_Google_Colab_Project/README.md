Amazon Reviews Analysis with NLP
Project Overview
This project involves analyzing Amazon reviews using Natural Language Processing (NLP) and various data visualization techniques. The main goal is to extract insights from customer feedback, including sentiment analysis, named entity recognition (NER), and generating visualizations like bar charts and word clouds.

The project includes several tasks:

Data Cleaning: Removing missing values and preprocessing text.

Sentiment Analysis: Classifying reviews as positive, negative, or neutral using TextBlob.

Named Entity Recognition (NER): Extracting organization names from the review texts using SpaCy.

Data Visualization: Generating visual representations of the data, such as bar charts for sentiment distribution and word clouds for popular terms.

This project is based on learning resources and solutions from Workearly, where I applied concepts from those resources and customized them to deepen my understanding of NLP techniques and their application to real-world data.

Dataset
The dataset used in this project is a collection of Amazon product reviews. It contains the following columns:

reviewText: The text of the customer review.

overall: The overall rating of the product (1–5).

reviewerName: Name of the reviewer.

asin: Product identifier.

summary: A brief summary of the review.

helpfulVotes: The number of helpful votes the review received.

Tasks and Code Walkthrough
Loading and Exploring the Data

Loaded the dataset from a CSV file and performed basic exploration, including checking for missing values.

Sentiment Analysis

Applied TextBlob to classify reviews as positive, negative, or neutral based on sentiment polarity.

Named Entity Recognition (NER)

Used SpaCy to extract organization names mentioned in the reviews.

Data Visualization

Created bar charts to visualize the distribution of sentiment, the most mentioned organizations, and the count of ratings.

Generated a Word Cloud to visualize the most frequent words in the reviews.

Example Code
python
import pandas as pd
import matplotlib.pyplot as plt
import spacy
from textblob import TextBlob
import nltk
nltk.download('punkt')
nltk.download('wordnet')
import re
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from wordcloud import WordCloud

# Dataset Loading and Initial Exploration
df = pd.read_csv('/content/drive/MyDrive/1-amazon_reviews.csv')
df.head()

# Sentiment Analysis
def classify_sentiment(sentiment):
    if sentiment > 0:
        return 'positive'
    elif sentiment < 0:
        return 'negative'
    else:
        return 'neutral'

# Visualizations
plt.bar(rating_counts.index, rating_counts.values, color='skyblue')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.title('Count of Ratings')
plt.show()
Customization and Extensions
**While the core concepts and some code snippets for the project were derived from Workearly’s resources, I have customized the analysis and visualizations based on my understanding of NLP and data processing.** I’ve also extended the project by focusing on specific aspects, such as:

Analyzing sentiment specifically for organizations mentioned in the reviews.

Generating custom visualizations like the Word Cloud to further explore the content of reviews.

Installation
To run this project on your local machine, please follow these steps:

Clone the repository or download the project files.

Install the necessary libraries using pip:

bash
pip install pandas matplotlib spacy textblob nltk wordcloud
Load the Amazon reviews dataset (1-amazon_reviews.csv) into the project.

Run the code in your preferred Python environment (such as Jupyter Notebook or Google Colab).

License
This project is licensed under the MIT License - see the LICENSE file for details.

Disclaimer:
**This project was based on learning resources and solutions from Workearly. I have customized and extended the ideas to deepen my understanding of the concepts. The main goal was to apply NLP techniques and data analysis to a real-world dataset, showcasing my skills in data cleaning, analysis, and visualization.**

# Abstract
The goal of this project was to create a friend recommender based on similarity of reviews provided on Yelp. Using (Yelp's open dataset)[https://www.yelp.ca/dataset], I was able to access almost 7 million reviews and a dataset of almost 2 million annoynomized users. Using topic modeling I was able to create a recommender for reviews of restaurants.

# Design
This project was focused on the use of Natural Language Processing. While there could have been other metrics that may have generated more scientifically sound analysis a greater emphasis is put on the story told through a Yelp user's review. This project serves as a proof of concept that could be built on for future direction in development for Yelp or other companies that may be interested in connecting people with similar ideas.

# Data
The Yelp data set contained 5 different collections of data, however, I will be primarily focused on 2 pieces provided by Yelp. The review dataset contains 6990280 rows with 9 features, while the business dataset contains 150346 rows with 14 features. The combination of these 2 datasets would require more computational power than what I have available to me. After filtering down only restaurants in Philadelphia I have a dataset of 168354 rows with 15 features. Each row represents 1 review for a business and the primary features that were of interest were the reviews \(text\), the user_id, and the business_id. The dataset was filtered to restaurants as I felt that would be the most relevant category in which reviews would be left. Philadelphia was the city that had the most restaurant reviews.

# Algorithms
## Vectorizing
PorterStemmer was used alongside both CountVectorizer and TfidfVectorizer to start analyzing reviews.
## Dimensionality Reduction
NMF was used to both model topics and begin dimensionality reduction. NMF was was choosen for it's interpretability. 
## Clustering
An attempt at clustering with DBSCAN was made however the dataset proved too large to use DBSCAN on. Given additional time I would have liked to apply BIRCH algorithms to reduce the dataset size and try clustering again.
## Recommender
A recommender was built leveraging NMF Dot Product math principals to analyze the similarity of reviews.

# Tools
- Numpy and Pandas for data manipulation
- Scikit-learn for mathematical analysis
- NLTK for language processing

# Communication
A visual presentation was made to present my findings.
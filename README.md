# Movie-Recommendation-System
This repository contains a Movie Recommendation System built using data from Netflix, Amazon, and HBO. The project utilizes clustering techniques to recommend movies and TV series based on user preferences. Two implementations of the system are provided: one using Streamlit for a simple and interactive web application, and another using Flask API with an HTML front end. <br/>
<br/>

## Introduction
The Movie Recommendation System uses three datasets sourced from Kaggle, focusing on Netflix, Amazon, and HBO movies and TV series. The system leverages the DBSCAN clustering algorithm to group similar movies and provide recommendations based on user input. <br/>
<br/>

## Features
* Clustering with DBSCAN: Grouping of movies and TV series based on features to create clusters for recommendation.
* Streamlit Implementation: A user-friendly web interface for easy interaction with the recommendation system.
* Flask API Implementation: A robust backend system with a custom HTML front end for serving recommendations. <br/>
<br/>

## Datasets
The following datasets were used to build the recommendation system: <br/>
* Netflix Movies and TV Series Dataset - Contains details about movies and TV shows available on Netflix.
* Amazon Prime Movies and TV Series Dataset - Includes data on movies and TV series available on Amazon Prime.
* HBO Movies and TV Series Dataset - Consists of information about movies and TV series available on HBO. <br/>

All datasets were sourced from Kaggle and combined to create a comprehensive data source. <br/>
<br/>

## Clustering Technique
The DBSCAN (Density-Based Spatial Clustering of Applications with Noise) algorithm was used to cluster the movies and TV series. This clustering allows the system to identify similar content and make more accurate recommendations. <br/>
<br/>

## Implementations
**Streamlit** <br/>
The Streamlit implementation provides an interactive interface where users can input their preferences and receive movie or TV series recommendations. This implementation is ideal for quick and easy access to the recommendation system. <br/>

**Flask API** <br/>
The Flask API implementation offers a more scalable solution with a custom HTML front end. Users interact with the system through the front end, while the backend processes requests and provides recommendations. This version is suitable for integration into larger web applications or services. <br/>
<br/>

## Setup and Installation
To run the Movie Recommendation System locally, follow these steps: <br/>
1. Clone the repository:
   ```bash
   git clone https://github.com/Shah114/movie-recommendation-system.git
   cd movie-recommendation-system
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit application:
   ```bash
   streamlit run app_streamlit.py
   ```
4. Run the Flask API application:
   ```bash
   python app_flask.py
   ```
<br/>

## Usage
* Streamlit: Open the Streamlit app in your browser, input your movie preferences, and get recommendations instantly.
* Flask API: Access the Flask app through the provided HTML front end, where you can enter your preferences and receive tailored recommendations. <br/>
<br/>

## Future Enhancements
* Improved Recommendation Algorithm: Experiment with other clustering and recommendation algorithms for better accuracy.
* Additional Datasets: Incorporate more streaming services to enhance the system's range of recommendations.
* User Authentication: Implement user login and profile management for personalized recommendations. <br/>
<br/>

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue.

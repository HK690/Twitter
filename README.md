# 🐦 Twitter Sentiment Analysis using Python & VADER

A Python-based sentiment analysis project that analyzes tweets using the **VADER (Valence Aware Dictionary and sEntiment Reasoner)** sentiment analysis model from NLTK. The project cleans raw tweets, performs sentiment scoring, classifies tweets into Positive, Neutral, and Negative categories, and visualizes sentiment trends over time using Plotly.

---

## 📌 Project Overview

Social media platforms like Twitter generate millions of opinions every day. This project demonstrates how Natural Language Processing (NLP) can be used to analyze public sentiment from tweets.

The workflow includes:

- Loading Twitter data from a CSV file
- Cleaning tweet text
- Removing usernames, URLs, hashtags, and non-English words
- Performing sentiment analysis using VADER
- Customizing the VADER lexicon with domain-specific words
- Categorizing tweets as Positive, Neutral, or Negative
- Visualizing sentiment trends over time

---

## 🚀 Features

- 🧹 Tweet text preprocessing
- 🔗 Removes:
  - User mentions (@username)
  - URLs
  - Hashtags
  - Non-English words
- 😊 Sentiment analysis using VADER
- 📖 Custom sentiment dictionary for improved accuracy
- 📊 Positive vs Negative tweet visualization using Plotly
- 📅 Daily sentiment trend analysis

---

## 📂 Dataset

The project expects a CSV file named:

```
data_science-tweet.csv
```

Required columns:

| Column | Description |
|----------|-------------|
| tweet | Tweet text |
| date | Date of tweet |
| id | Tweet ID |

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- NLTK
- Plotly
- Regular Expressions (re)

---

## 📦 Installation

Clone the repository

```bash
git clone https://github.com/HK690/twitter-sentiment-analysis.git
```

Move into the project folder

```bash
cd twitter-sentiment-analysis
```

Install dependencies

```bash
pip install pandas numpy nltk plotly
```

---

## ▶️ Running the Project

Simply run

```bash
python twitter_sentiment_analysis.py
```

The script will automatically download the required NLTK resources:

- vader_lexicon
- words

---

## 📊 Workflow

```
Load Dataset
      │
      ▼
Clean Tweets
      │
      ▼
Remove URLs & Usernames
      │
      ▼
Filter English Words
      │
      ▼
Apply VADER Sentiment Analysis
      │
      ▼
Custom Lexicon Update
      │
      ▼
Calculate Compound Score
      │
      ▼
Classify Sentiment
      │
      ▼
Group by Date
      │
      ▼
Plot Sentiment Trends
```

---

## 📈 Sentiment Classification

The VADER compound score is converted into sentiment labels using the following logic:

| Compound Score | Sentiment |
|----------------|-----------|
| > 0 | Positive |
| = 0 | Neutral |
| < 0 | Negative |

---

## 📖 Custom Sentiment Dictionary

The project extends VADER's default lexicon with domain-specific words such as:

```python
{
    "manipulate": -1,
    "manipulative": -1,
    "pedophile": -1,
    "cancel": -1,
    "cancelled": -1,
    "teamjames": 1,
    "teamjamescharles": 1,
    "liar": -1
}
```

This improves sentiment accuracy for tweets related to specific online discussions.

---

## 📊 Output

The project generates an interactive Plotly graph showing:

- 📈 Positive Tweets over time
- 📉 Negative Tweets over time

This helps visualize changes in public sentiment across different dates.

---

## 📁 Project Structure

```
Twitter-Sentiment-Analysis/
│
├── data_science-tweet.csv
├── twitter_sentiment_analysis.py
├── README.md
└── requirements.txt
```

---

## 📚 Libraries Used

```text
pandas
numpy
nltk
plotly
re
os
```

---

## 💡 Future Improvements

- Support for real-time Twitter API data
- Machine Learning-based sentiment models
- Word Cloud visualization
- Emotion Detection
- Interactive dashboard using Streamlit
- Export analysis reports to CSV or Excel
- Multi-language sentiment analysis

---

## 🎯 Learning Outcomes

This project demonstrates:

- Data Cleaning
- Natural Language Processing (NLP)
- Sentiment Analysis
- Regular Expressions
- Text Preprocessing
- Data Visualization
- Python Programming
- Plotly Interactive Charts

---

## 📜 License

This project is intended for educational and learning purposes.

---

## 👤 Author

**Harshal Kapse**

If you found this project useful, feel free to ⭐ the repository.

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import pickle
import re
import streamlit as st

# def evaluate_model():
#     # Load the model from disk
#     filename = f'model_{accuracy}.sav'
#     loaded_model = pickle.load(open(filename, 'rb'))

#     # Load the test data
#     df = pd.read_csv("tweetsdata.csv", encoding="latin-1", header)

def pre_process_visualise(df):
    print("Preprocessing dataframe..")
    print(df.head())
    print("Shape:", df.shape)

    # Count the number of tweets in each sentiment category
    sentiment_counts = df["target"].value_counts()
    print("Sentiment Counts:")
    print(sentiment_counts)

    # Visualize the sentiment distribution
    plt.figure(figsize=(8, 6))
    sns.countplot(x=["Negative", "Positive"], data=df)
    plt.title("Sentiment Distribution")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    # plt.show()
    # st.pyplot()


final_model_name = "model.mdl"

def train_model(df):
    # Split the data into training and testing sets
    global final_model_name
    print("Beginning training")
    X = df["text"]
    y = df["target"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    # Vectorize the tweets using TF-IDF
    vectorizer = TfidfVectorizer(max_features=5000)
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    # Train a logistic regression model
    model = LogisticRegression(max_iter=500, verbose=1)
    model.fit(X_train_vec, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test_vec)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy*100}%")

    filename = f'model_{accuracy}.sav'
    pickle.dump(model, open(filename, 'wb'))
    pickle.dump(model, open(final_model_name, 'wb'))
    print("Training done. Model saved.")


def evaluate_model(model_name, df):
    print("Beginning evaluation")
    X = df["text"]
    y = df["target"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    with open("model.mdl", "rb") as file:
        model = pickle.load(file)
        print("model loaded")

        print("Vectorizing tweets")
        vectorizer = TfidfVectorizer(max_features=5000)
        X_train_vec = vectorizer.fit_transform(X_train)
        X_test_vec = vectorizer.transform(X_test)
        print("Predicting sentiments")
        y_pred = model.predict(X_test_vec)

        accuracy = accuracy_score(y_test, y_pred)
        print("Model Accuracy:", accuracy)

        # Calculate precision, recall, and F1-score
        precision = precision_score(y_test, y_pred, pos_label=4)
        recall = recall_score(y_test, y_pred, pos_label=4)
        f1 = f1_score(y_test, y_pred, pos_label=4)

        print("Precision:", precision)
        print("Recall:", recall)
        print("F1-score:", f1)

    # # Plot confusion matrix
    # cm = confusion_matrix(y_test, y_pred)
    # plt.figure(figsize=(8, 6))
    # sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    # plt.title("Confusion Matrix")
    # plt.xlabel("Predicted")
    # plt.ylabel("Actual")
    # plt.show()


if __name__ == "__main__":
    df = pd.read_csv("tweets_data.csv", encoding="latin-1", header=None)
    df.columns = ["target", "ids", "date", "flag", "user", "text"]

    pre_process_visualise(df)
    # train_model(df)
    evaluate_model(final_model_name, df)

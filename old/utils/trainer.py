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

# Global variables
df = None
vectorizer = None
X_train = None
X_test = None
y_train = None
y_test = None
X_train_vec = None

initialized = False

def initialize():
    global df, vectorizer, X_train, X_test, y_train, y_test, X_train_vec, initialized
    print("initialized = ", initialized)

    if initialized:
        return

    df = pd.read_csv("./utils/tweets_data.csv", encoding="latin-1", header=None)
    df.columns = ["target", "ids", "date", "flag", "user", "text"]

    vectorizer = TfidfVectorizer(max_features=5000)

    # Vectorize the tweets using TF-IDF
    X = df["text"]
    y = df["target"]

    print("Vectorizing tweets")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    X_train_vec = vectorizer.fit_transform(X_train)

    print("Done vectorizing")
    initialized = True


def train_test_vectorizer_split(dataframe=None, custom_x_test=None):
    global df, vectorizer, X_train, X_test, y_train, y_test, X_train_vec

    initialize()

    if custom_x_test:
        X_test = custom_x_test
    X_test_vec = vectorizer.transform(X_test)

    print("Returning")
    return X_train_vec, X_test_vec, X_train, X_test, y_train, y_test


def pre_process_visualise(df):
    print("Preprocessing dataframe..")
    print(df.head())
    print("Shape:", df.shape)

    sentiment_counts = df["target"].value_counts()
    print("Sentiment Counts:")
    print(sentiment_counts)

    plt.figure(figsize=(8, 6))
    sns.countplot(x=["Negative", "Positive"], data=df)
    plt.title("Sentiment Distribution")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")
    # plt.show()
    # st.pyplot()


final_model_name = "model.mdl"


def train_model(df):
    print("Beginning training")

    X_train_vec, X_test_vec, X_train, X_test, y_train, y_test = train_test_vectorizer_split(
        df)

    # do cleaning for X_train and X_test

    print("Predicting sentiments")
    model = LogisticRegression(max_iter=500, verbose=1)
    model.fit(X_train_vec, y_train)

    y_pred = model.predict(X_test_vec)

    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy*100}%")

    filename = f'model_{accuracy}.sav'
    # pickle.dump(model, open(filename, 'wb'))
    print(final_model_name)
    pickle.dump(model, open(final_model_name, 'wb'))
    print("Training done. Model saved.")


def evaluate_model(model_name, df):
    print("Beginning evaluation")
    X_train_vec, X_test_vec, X_train, X_test, y_train, y_test = train_test_vectorizer_split(
        df)

    with open("model.mdl", "rb") as file:
        model = pickle.load(file)
        print("model loaded")

        print("Predicting sentiments")
        y_pred = model.predict(X_test_vec)

        accuracy = accuracy_score(y_test, y_pred)
        print("Model Accuracy:", accuracy)

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
    train_model(df)
    evaluate_model(final_model_name, df)

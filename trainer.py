from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

import pickle
import re


def pre_process_visualise(df=df):
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
    plt.show()


def train_model(df=df):
    # Split the data into training and testing sets
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
    print("Model Accuracy:", accuracy)

    filename = f'model_{accuracy}.sav'
    pickle.dump(model, open(filename, 'wb'))
    print("Training done. Model saved.")


if __name__ == "__main__":
    df = pd.read_csv("tweetsdata.csv", encoding="latin-1", header=None)
    df.columns = ["target", "ids", "date", "flag", "user", "text"]

    pre_process_visualise(df)
    train_model(df)

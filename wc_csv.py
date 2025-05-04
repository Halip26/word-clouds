from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
import os


def generate_wordcloud(csv_path):
    """
    Generates a word cloud from a CSV file containing a 'CONTENT' column.
    """
    # Check if the file exists
    if not os.path.exists(csv_path):
        print(f"Error: File '{csv_path}' not found.")
        return

    try:
        # Read the CSV file
        df = pd.read_csv(csv_path, encoding="latin-1")
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        return

    # Ensure the 'CONTENT' column exists
    if "CONTENT" not in df.columns:
        print("Error: 'CONTENT' column not found in the CSV file.")
        return

    # Initialize variables
    comment_words = ""
    stopwords = set(STOPWORDS)

    # Process the 'CONTENT' column
    for val in df["CONTENT"].dropna():  # Drop NaN values to avoid errors
        tokens = [token.lower() for token in str(val).split()]
        comment_words += " ".join(tokens) + " "

    # Generate the word cloud
    wordcloud = WordCloud(
        width=1366,
        height=768,
        background_color="white",
        stopwords=stopwords,
        min_font_size=10,
    ).generate(comment_words)

    # Plot the WordCloud image
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()


if __name__ == "__main__":
    # Path to the CSV file
    csv_path = r"csv/words.csv"
    generate_wordcloud(csv_path)

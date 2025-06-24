from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os


def generate_wordcloud(file_path):
    """
    Generates and displays a word cloud from a text file.
    """
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return

    try:
        # Open and read the text file
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
    except Exception as e:
        print(f"Error reading the file: {e}")
        return

    # Generate the word cloud
    wordcloud = WordCloud(
        width=1366, height=673, background_color="white", min_font_size=10
    ).generate(text)

    # Display the word cloud
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()


if __name__ == "__main__":
    # Path to the text file
    file_path = str(input("\nEnter your file path here: "))
    generate_wordcloud(file_path)

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# buka text file
with open("bullshit.txt", "r") as f:
    text = f.read()

# generate the word Cloud
wordcloud = WordCloud(
    width=1366, height=673, background_color="white", min_font_size=10
).generate(text)

# Menampilkan the wordcloud
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

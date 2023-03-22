import time
import webbrowser
import random

common_words = ["technology", "nature", "science", "history", "music", "art",
    "education", "business", "health", "sports", "travel", "food",
    "politics", "environment", "culture", "entertainment", "animals",
    "economy", "lifestyle", "language"]
keywords = []
for _ in range(30):
    word_1 = random.choice(common_words)
    word_2 = random.choice(common_words)

    while word_1 == word_2:
        word_2 = random.choice(common_words)

    keyword = f"{word_1} {word_2}"
    keywords.append(keyword)

print(keywords)

def open_browser_and_search(keyword):
    query = f"https://www.bing.com/search?q={keyword}"
    webbrowser.open(query)
    print(f"Opened browser with keyword: {keyword}")
for keyword in keywords:
    open_browser_and_search(keyword)
    time.sleep(10)
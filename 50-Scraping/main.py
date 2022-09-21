# module import
import collections
from pprint import pprint
import requests
from bs4 import BeautifulSoup

id_artist = int(input("Enter the id of the artist to scrape: "))
# test avec Patrick Bruel : 29743


def is_valid(word):
    return "[" not in word and "]" not in word


def extract_lyrics(url):
    print(f"Fetching lyrics {url}...")
    r = requests.get(url)
    if r.status_code != 200:
        print("Impossible to fetch the page!!!")
        return []


    soup = BeautifulSoup(r.content, 'html.parser')
    all_words = []
    for tag in soup.find_all("div", class_="Lyrics__Container-sc-1ynbvzw-6 YYrds"):
        for sentence in tag.stripped_strings:
            sentence_words = [word.strip(",").strip(".").strip("c'").strip("l'").strip("d'").strip(".").lower() for word in sentence.split() if is_valid(word)]
            all_words.extend(sentence_words)
    return all_words


def get_all_urls():
    page_number = 1
    links = []
    while True:
        r = requests.get(f"https://genius.com/api/artists/{id_artist}/songs?page={page_number}&sort=popularity")
        if r.status_code == 200:
            print(f"Fetching page {page_number}")
            response = r.json().get("response", {})
            next_page = response.get("next_page")

            songs = response.get("songs")
            links.extend([song.get("url") for song in songs])
            page_number += 1

            if not next_page:
                print("No more pages to fetch")
                break
    return links


def get_all_words():
    urls = get_all_urls()
    words = []
    for url in urls:
        lyrics = extract_lyrics(url=url)
        words.extend(lyrics)

    # with open("data-patrick-bruel.json", "w") as f:
    #     json.dump(words, f, indent=4)

    # with open("data.json", "r") as f:
    #     words = json.load(f)

    # print(len(words))
    # pprint(words)

    counter = collections.Counter([w for w in words if len(w) > 5])
    most_common_words = counter.most_common(10)
    pprint(most_common_words)


get_all_words()


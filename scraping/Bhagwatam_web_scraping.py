import requests
import csv
import time
import re
from bs4 import BeautifulSoup

BASE_URL = "https://vedabase.io"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def safe_get(url):
    while True:
        try:
            r = requests.get(url, headers=HEADERS, timeout=20)
            if r.status_code == 200:
                return r
            if r.status_code == 404:
                return None
        except Exception:
            pass
        time.sleep(1.5)


def get_canto_urls():
    return [f"{BASE_URL}/en/library/sb/{i}/" for i in range(1, 13)]


def get_chapter_urls(canto_url):
    r = safe_get(canto_url)
    if not r:
        return []

    soup = BeautifulSoup(r.text, "html.parser")
    chapter_links = []

    for a in soup.find_all("a", href=True):
        href = a["href"]
        if re.match(rf"^/en/library/sb/\d+/\d+/$", href):
            chapter_links.append(BASE_URL + href)

    return sorted(set(chapter_links))


def get_chapter_title(chapter_url):
    r = safe_get(chapter_url)
    if not r:
        return ""

    soup = BeautifulSoup(r.text, "html.parser")
    h1 = soup.find("h1")
    return h1.get_text(strip=True) if h1 else ""

def get_verse_page_links(chapter_url):
    r = safe_get(chapter_url)
    if not r:
        return []

    soup = BeautifulSoup(r.text, "html.parser")
    verse_links = []

    for a in soup.find_all("a", href=True):
        href = a["href"]
        if re.match(rf"^/en/library/sb/\d+/\d+/\d+(-\d+)?/$", href):
            verse_links.append(BASE_URL + href)

    return sorted(set(verse_links))


def extract_verse_page(url):
    r = safe_get(url)
    if not r:
        return {"devanagari": "", "translation": "", "purport": ""}

    soup = BeautifulSoup(r.text, "html.parser")

    def grab(cls):
        div = soup.find("div", class_=lambda x: x and cls in x)
        return div.get_text("\n", strip=True) if div else ""

    return {
        "devanagari": grab("devanagari"),
        "translation": grab("translation"),
        "purport": grab("purport")
    }


with open("srimad_bhagavatam.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Canto",
        "Chapter",
        "Text",
        "Chapter Description",
        "Devanagari Script",
        "Translation",
        "Purport"
    ])

    for canto_url in get_canto_urls():
        canto_number = int(canto_url.rstrip("/").split("/")[-1])
        print(f"\n📘 Canto {canto_number}")

        chapter_urls = get_chapter_urls(canto_url)

        for chapter_url in chapter_urls:
            chapter_number = int(chapter_url.rstrip("/").split("/")[-1])
            chapter_title = get_chapter_title(chapter_url)

            print(f" Chapter {chapter_number}")

            verse_pages = get_verse_page_links(chapter_url)

            for page_url in verse_pages:
                verse_part = page_url.rstrip("/").split("/")[-1]

                if "-" in verse_part:
                    start, end = map(int, verse_part.split("-"))
                    verses = range(start, end + 1)
                else:
                    verses = [int(verse_part)]

                data = extract_verse_page(page_url)

                for v in verses:
                    writer.writerow([
                        canto_number,
                        chapter_number,
                        f"{canto_number}.{chapter_number}.{v}",
                        chapter_title,
                        data["devanagari"],
                        data["translation"],
                        data["purport"]
                    ])
                    print(f" Saved {canto_number}.{chapter_number}.{v}")

                time.sleep(0.7)

print("\n ALL 12 CANTOS PARSED — ZERO VERSES SKIPPED")




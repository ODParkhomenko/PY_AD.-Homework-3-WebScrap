import requests
import bs4

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
habr_url = "https://habr.com/ru/all/"
http_headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}
response = requests.get(habr_url, headers=http_headers)
response_text = response.text
soup = bs4.BeautifulSoup(response_text, features="html.parser")
all_articles = soup.find_all("article")

for article in all_articles:
    datetime_published = article.find("time").get("title")
    pars_keywords = article.find_all(class_="tm-article-snippet")
    pars_keywords = " ".join([pars_keyword.text.strip() for pars_keyword in pars_keywords])
    link = article.find(class_="tm-article-snippet__title-link").get("href")
    for search_word in KEYWORDS:
        if search_word in pars_keywords:
            print(f"Дата - {datetime_published}; Заголовок - {search_word}; Ссылка - https://habr.com{link}")
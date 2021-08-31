from dotenv import load_dotenv
from urllib.parse import urlparse
import argparse
import requests
import os


def get_netloc_with_path(user_url):
    netloc = urlparse(user_url).netloc
    path = urlparse(user_url).path
    updated_user_url = f"{netloc}{path}"
    return updated_user_url


def is_bitlink(headers, user_url):
    bitlink_description_url = "https://api-ssl.bitly.com/v4/bitlinks/{bitlink}"
    response = requests.get(
        bitlink_description_url.format(bitlink=user_url),
        headers=headers,
    )
    return response.ok


def shorten_link(headers, user_url):
    shorten_url = "https://api-ssl.bitly.com/v4/shorten"
    payload = {
        "long_url": user_url
    }
    response = requests.post(shorten_url, json=payload, headers=headers)
    response.raise_for_status()
    answer = response.json()
    return answer["link"]


def count_clicks(bitlink, headers):
    sum_clicks_url = "https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary"
    response = requests.get(
        sum_clicks_url.format(bitlink=bitlink),
        headers=headers,
    )
    response.raise_for_status()
    answer = response.json()
    return answer["total_clicks"]


if __name__ == "__main__":
    load_dotenv()
    parser = argparse.ArgumentParser(
        description="Программа выводит сокращенные ссылки и количество кликов по ним."
    )
    parser.add_argument("link", help="Ссылка или битлинк")
    user_url = parser.parse_args().link
    token = os.getenv("BITLY_TOKEN")
    authorization = {
        "Authorization": "Bearer {}".format(token)
    }
    netloc_with_path = get_netloc_with_path(user_url)

    if is_bitlink(authorization, netloc_with_path):
        try:
            print(count_clicks(netloc_with_path, authorization))
        except:
            print("Ошибка при подсчете кликов")
    else:
        try:
            print(shorten_link(authorization, user_url))
        except:
            print("Ошибка при сокращении ссылки")

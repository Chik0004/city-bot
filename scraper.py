import requests
import streamlit as st
from bs4 import BeautifulSoup

BASE_URL = "https://www.normanok.gov"

@st.cache_data(ttl=3600)
def get_city_news():
    try:
        response = requests.get(BASE_URL)
        soup = BeautifulSoup(response.text, "html.parser")

        news_list = []

        # Extract links + titles
        for link in soup.find_all("a", href=True):
            text = link.text.strip()
            href = link["href"]

            # Filter meaningful content
            if text and len(text) > 20 and "news" in href.lower():
                full_link = BASE_URL + href if href.startswith("/") else href

                news_list.append({
                    "title": text,
                    "link": full_link
                })

        # Limit results
        return news_list[:5] if news_list else [{"title": "No news found", "link": ""}]

    except Exception as e:
        return [{"title": f"Error: {e}", "link": ""}]
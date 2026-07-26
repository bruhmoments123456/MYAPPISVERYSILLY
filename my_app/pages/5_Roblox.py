import streamlit as st
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

st.set_page_config(page_title="Roblox Search", page_icon="🔍")

st.title("🔍 Roblox Search")

search = st.text_input("Nhập tên game")

if st.button("Tìm kiếm"):

    if search.strip() == "":
        st.warning("Hãy nhập từ khóa.")
        st.stop()

    url = f"https://www.roblox.com/discover/?Keyword={quote(search)}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(url, headers=headers)

    if r.status_code != 200:
        st.error(f"Lỗi {r.status_code}")
        st.stop()

    soup = BeautifulSoup(r.text, "html.parser")

    cards = soup.find_all("a")

    found = False

    for card in cards:

        href = card.get("href")

        if href and "/games/" in href:

            name = card.get("title")

            if name:

                found = True

                st.subheader(name)
                st.write("https://www.roblox.com" + href)
                st.divider()

    if not found:
        st.warning("Không tìm thấy kết quả.")
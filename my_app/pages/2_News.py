import streamlit as st
import feedparser

@st.cache_data
def load_news():
    return feedparser.parse("https://vnexpress.net/rss/tin-moi-nhat.rss")

@st.cache_data
def load_news_gold():
    return feedparser.parse("https://vietnamnet.vn/rss/kinh-doanh.rss")


tab1, tab2 = st.tabs(["News", "Gold Prices"])
with tab1:
    st.header("Latest News on VnExpress")
    feed = load_news()
    for entry in feed.entries[:10]:
        st.subheader(entry.title)
        st.write(entry.published)
        st.write(entry.link)    
with tab2:
    st.header("Latest Gold Prices from Vietnamnet")
    feet = load_news_gold()
    gold_news = [entry for entry in feet.entries if "vàng" in entry.title.lower() or "giá vàng" in entry.summary.lower()]
    if gold_news:
        for entry in gold_news[:5]:
            st.subheader(entry.title)
            st.write(entry.published)
            st.write(entry.link)
    else:
        st.info("No news found about gold prices.")
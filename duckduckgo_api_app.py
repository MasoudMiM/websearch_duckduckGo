import streamlit as st
from duckduckgo_search import DDGS
import plotly.express as px


regions = ['xa-ar [Arabia]', 'xa-en [Arabia (en)]', 'ar-es [Argentina]', 
               'au-en [Australia]', 'at-de [Austria]', 'be-fr [Belgium (fr)]',
               'be-nl [Belgium (nl)]', 'br-pt [Brazil]', 'bg-bg [Bulgaria]', 'ca-en [Canada]', 
               'ca-fr [Canada (fr)]', 'ct-ca [Catalan]', 'cl-es [Chile]', 
               'cn-zh [China]', 'co-es [Colombia]', 'hr-hr [Croatia]', 
               'cz-cs [Czech Republic]', 'dk-da [Denmark]', 
               'ee-et [Estonia]', 'fi-fi [Finland]', 'fr-fr [France]', 
               'de-de [Germany]', 'gr-el [Greece]', 'hk-tzh [Hong Kong]', 
               'hu-hu [Hungary]', 'in-en [India]', 'id-id [Indonesia]', 
               'id-en [Indonesia (en)]', 'ie-en [Ireland]', 'il-he [Israel]'
               'it-it [Italy]', 'jp-jp [Japan]', 'kr-kr [Korea]', 
               'lv-lv [Latvia]', 'lt-lt [Lithuania]', 'xl-es [Latin America]',
               'my-ms [Malaysia]', 'my-en [Malaysia (en)]', 'mx-es [Mexico]', 
               'nl-nl [Netherlands]', 'nz-en [New Zealand]', 'no-no [Norway]', 
               'pe-es [Peru]', 'ph-en [Philippines]', 'ph-tl [Philippines (tl)]',
               'pl-pl [Poland]', 'pt-pt [Portugal]', 'ro-ro [Romania]',
               'ru-ru [Russia]', 'sg-en [Singapore]', 'sk-sk [Slovak Republic]',
               'sl-sl [Slovenia]', 'za-en [South Africa]', 'es-es [Spain]',
               'se-sv [Sweden]', 'ch-de [Switzerland (de)]', 'ch-fr [Switzerland (fr)]',
               'ch-it [Switzerland (it)]', 'tw-tzh [Taiwan]', 'th-th [Thailand]',
               'tr-tr [Turkey]', 'ua-uk [Ukraine]', 'uk-en [United Kingdom]',
               'us-en [United States]', 'ue-es [United States (es)]', 've-es [Venezuela]',
               'vn-vi [Vietnam]', 'wt-wt [No region]']

languages = [
    "af-Afrikaans",
    "ar-Arabic",
    "bn-Bengali",
    "bs-Bosnian",
    "ca-Catalan",
    "cs-Czech",
    "da-Danish",
    "de-German",
    "el-Greek",
    "en-English",
    "es-Spanish",
    "et-Estonian",
    "fa-Persian",
    "fi-Finnish",
    "fr-French",
    "gu-Gujarati",
    "he-Hebrew",
    "hi-Hindi",
    "hr-Croatian",
    "hu-Hungarian",
    "id-Indonesian",
    "it-Italian",
    "ja-Japanese",
    "jw-Javanese",
    "kn-Kannada",
    "ko-Korean",
    "la-Latin",
    "lv-Latvian",
    "mg-Malagasy",
    "ml-Malayalam",
    "mn-Mongolian",
    "mr-Marathi",
    "ms-Malay",
    "mt-Maltese",
    "ne-Nepali",
    "nl-Dutch",
    "no-Norwegian",
    "pl-Polish",
    "pt-Portuguese",
    "ro-Romanian",
    "ru-Russian",
    "si-Sinhala",
    "sk-Slovak",
    "sl-Slovenian",
    "sn-Shona",
    "so-Somali",
    "sq-Albanian",
    "sr-Serbian",
    "sv-Swedish",
    "sw-Swahili",
    "ta-Tamil",
    "te-Telugu",
    "th-Thai",
    "tr-Turkish",
    "uk-Ukrainian",
    "ur-Urdu",
    "vi-Vietnamese",
    "xh-Xhosa",
    "yi-Yiddish",
    "yo-Yoruba",
    "zu-Zulu"
]

default_option = 'wt-wt [No region]'
default_index = regions.index(default_option)

def main():
    st.title("DuckDuckGo Search Interface")

    # Sidebar content
    st.sidebar.title("DuckDuckGo API Options")
    # Sidebar for search type selection
    search_type = st.sidebar.selectbox(
        "Select Type",
        ["AI Chat", "Text", "Images", "Videos", "News", "Maps", "Translate"]
    )
    # Main content area
    if search_type == "AI Chat":
        st.sidebar.markdown(
            """See an example input [here](https://github.com/MasoudMiM/duckduckgo_search/tree/main?tab=readme-ov-file#1-chat---ai-chat).  
            [DuckDuckGo AI Chat](https://duckduckgo.com/duckduckgo-help-pages/aichat/) is a free beta feature that allows you to have anonymous conversations 
            with 3rd-party AI chat models. It currently supports Anthropic’s Claude 3 Haiku, 
            Mistral AI’s Mixtral 8x7B, OpenAI’s GPT-4o mini, and Meta’s Llama 3.1 70B (built with Llama). 
            Each model relies on unique algorithms and data sets and will respond to your prompts differently. 
            You can use DuckDuckGo AI Chat to get answers to questions, compose an email, summarize text, or 
            just have an interesting conversation.
            """
            )
    if search_type == "Text":
        st.sidebar.markdown(
            """See an example input [here](https://github.com/MasoudMiM/duckduckgo_search/tree/main?tab=readme-ov-file#2-text---text-search-by-duckduckgocom).
            """
        )
    elif search_type == "Images":
        st.sidebar.markdown(
            """See an example input [here](https://github.com/MasoudMiM/duckduckgo_search/tree/main?tab=readme-ov-file#4-images---image-search-by-duckduckgocom).
            """
        )
    elif search_type == "Videos":
        st.sidebar.markdown(
            """See an example input [here](https://github.com/MasoudMiM/duckduckgo_search/tree/main?tab=readme-ov-file#5-videos---video-search-by-duckduckgocom).
            """
        )
    elif search_type == "News":
        st.sidebar.markdown(
            """See an example input [here](https://github.com/MasoudMiM/duckduckgo_search/tree/main?tab=readme-ov-file#6-news---news-search-by-duckduckgocom).
            """
        )
    elif search_type == "Maps":
        st.sidebar.markdown(
            """See an example input [here](https://github.com/MasoudMiM/duckduckgo_search/tree/main?tab=readme-ov-file#7-maps---map-search-by-duckduckgocom).
            """
        )
    elif search_type == "Translate":
        st.sidebar.markdown(
            """See an example input [here](https://github.com/MasoudMiM/duckduckgo_search/tree/main?tab=readme-ov-file#8-translate---translation-by-duckduckgocom).  
            According to [DuckDuckGo](https://duckduckgo.com/duckduckgo-help-pages/results/translation/), "For our translation feature, we've partnered with Microsoft but we still proxy your queries through our servers before passing them to search result and Instant Answer providers, so they stay completely anonymous."
            """
        )

    # Main content area
    if search_type == "AI Chat":
        ai_chat()
    if search_type == "Text":
        text_search()
    elif search_type == "Images":
        image_search()
    elif search_type == "Videos":
        video_search()
    elif search_type == "News":
        news_search()
    elif search_type == "Maps":
        maps_search()
    elif search_type == "Translate":
        translate()

def ai_chat():
    st.header("AI Chat")
    keywords = st.text_input("The initial message or question to send to the AI")
    model = st.selectbox("Select model", ["gpt-4o-mini", "claude-3-haiku", "llama-3-70b", "mixtral-8x7b"])
    timeout = st.number_input("Timeout", min_value=1, value=30)

    if st.button("Chat"):
        with DDGS() as ddgs:
            results = ddgs.chat(keywords, model=model, timeout=timeout)
            st.write(results)


def text_search():
    st.header("Text Search")
    keywords = st.text_input("Enter keywords")
    region = st.selectbox("Select region", options=regions, index=default_index)
    safesearch = st.select_slider("SafeSearch", options=["off", "moderate", "on"])
    timelimit = st.selectbox("Time limit", [None, "d", "w", "m", "y"])
    max_results = st.number_input("Max results", min_value=1, value=10)

    if st.button("Search"):
        with DDGS() as ddgs:
            results = ddgs.text(keywords, region=region.split("[")[0], safesearch=safesearch, 
                                timelimit=timelimit, max_results=max_results)
            for result in results:
                st.write(f"**{result['title']}**")
                st.write(result['body'])
                st.write(result['href'])
                st.write("---")

def image_search():
    st.header("Image Search")
    keywords = st.text_input("Enter keywords")
    region = st.selectbox("Select region", options=regions, index=default_index)
    safesearch = st.select_slider("SafeSearch", options=["off", "moderate", "on"])
    timelimit = st.selectbox("Time limit", [None, "Day", "Week", "Month", "Year"])
    size = st.selectbox("Image size", [None, "Small", "Medium", "Large", "Wallpaper"])
    color = st.selectbox("Image color", [None, "color", "Monochrome", "Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Pink", "Brown", "Black", "Gray", "Teal", "White"])
    type_image = st.selectbox("Image type", [None, "photo", "clipart", "gif", "transparent", "line"])
    layout = st.selectbox("Image layout", [None, "Square", "Tall", "Wide"])
    license_image = st.selectbox("Image license", [None, "any", "Public", "Share", "ShareCommercially", "Modify", "ModifyCommercially"])
    max_results = st.number_input("Max results", min_value=1, value=10)
    if st.button("Search"):
        with DDGS() as ddgs:
            results = ddgs.images(keywords, region=region.split("[")[0], safesearch=safesearch, 
                                timelimit=timelimit, size=size, color=color, type_image=type_image, 
                                layout=layout, license_image=license_image, max_results=max_results)
            for result in results:
                st.image(result['image'], caption=result['title'], use_column_width=True)
                st.write("---")

def video_search():
    st.header("Video Search")
    keywords = st.text_input("Enter keywords")
    region = st.selectbox("Select region", options=regions, index=default_index)
    safesearch = st.select_slider("SafeSearch", options=["off", "moderate", "on"])
    timelimit = st.selectbox("Time limit", [None, "Day", "Week", "Month"])
    resolution = st.selectbox("Video resolution", [None, "high", "standart"])
    duration = st.selectbox("Video duration", [None, "short", "medium", "long"])
    license_videos = st.selectbox("Video license", [None, "creativeCommon", "youtube"])
    max_results = st.number_input("Max results", min_value=1, value=10)
    if st.button("Search"):
        with DDGS() as ddgs:
            results = ddgs.videos(keywords, region=region.split("[")[0], safesearch=safesearch, 
                                timelimit=timelimit, resolution=resolution, duration=duration, 
                                license_videos=license_videos, max_results=max_results)
            for result in results:
                st.video(result['embed_url'])
                st.write("---")

def news_search():
    st.header("News Search")
    keywords = st.text_input("Enter keywords")
    region = st.selectbox("Select region", options=regions, index=default_index)
    safesearch = st.select_slider("SafeSearch", options=["off", "moderate", "on"])
    timelimit = st.selectbox("Time limit", [None, "d", "w", "m"])
    max_results = st.number_input("Max results", min_value=1, value=10)
    if st.button("Search"):
        with DDGS() as ddgs:
            results = ddgs.news(keywords, region=region.split("[")[0], safesearch=safesearch, 
                                timelimit=timelimit, max_results=max_results)
            for result in results:
                st.write(f"{result['title']} - {result['date']}")
                st.write(result['body'])
                st.write(result['url'])
                st.write(result['source'])
                st.write("---")

def maps_search():
    st.header("Maps Search")
    keywords = st.text_input("Enter keywords")
    place = st.text_input("Place")
    max_results = st.number_input("Max results", min_value=1, value=10)
    if st.button("Search"):
        with DDGS() as ddgs:
            results = ddgs.maps(keywords, place=place, max_results=max_results )
            for result in results:
                st.write(f"**{result['title']}**")
                st.write(result['address'])
                st.write(result['url'])
                lat = result['latitude']
                lon = result['longitude']
                # use plotly to create a map with the point shown on the map
                data = {
                    'lat': [lat],
                    'long': [lon],
                    'address': result['address']
                }
                fig = px.scatter_mapbox(
                    data, 
                    lat='lat', 
                    lon='long', 
                    hover_name='address', 
                    size = [5],
                    color_discrete_sequence=['red'],
                    zoom=12, 
                    height=600)
                fig.update_layout(mapbox_style="open-street-map")
                st.plotly_chart(fig) 
                st.write("---")

def translate():
    st.header("Translate")
    text = st.text_area("Enter text to translate")
    from_lang = st.text_input("From language (leave blank for auto-detect)")
    to_lang = st.selectbox("To language", options=languages)

    if st.button("Translate"):
        with DDGS() as ddgs:
            results = ddgs.translate(text, from_=from_lang or None, to=to_lang.split("-")[0])
            for result in results:
                st.write(f"Original: {result['original']}")
                st.write(f"Translated: {result['translated']}")
                st.write(f"Detected Language: {result['detected_language']}")

if __name__ == "__main__":
    main()
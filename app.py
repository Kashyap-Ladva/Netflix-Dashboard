import streamlit as st
from src.data_processing import preprocess
from src.plots import plot_top_genres, plot_binge_hours, plot_genre_heatmap

st.set_page_config(layout="wide", page_title="OTT Watch Dashboard")

@st.cache_data
def get_data(path="data/sample_watch_history.csv"):
    return preprocess(path)

df = get_data()

st.sidebar.header("Filters")
all_genres = sorted({g for gl in df["genre_list"] for g in gl})
genre = st.sidebar.selectbox("Genre", options=["All"] + all_genres)
years = sorted(df["watch_year"].dropna().unique().astype(int).tolist())
year = st.sidebar.selectbox("Year", options=["All"] + years)
countries = sorted(df["country"].fillna("Unknown").unique().tolist())
country = st.sidebar.selectbox("Country", options=["All"] + countries)

filtered = df.copy()
if genre != "All":
    filtered = filtered[filtered["genre_list"].apply(lambda gl: genre in gl)]
if year != "All":
    filtered = filtered[filtered["watch_year"] == int(year)]
if country != "All":
    filtered = filtered[filtered["country"] == country]

st.title("Netflix / OTT Watch Pattern Dashboard")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Watch Minutes", int(filtered["duration_minutes"].sum()))
col2.metric("Unique Titles", filtered["title"].nunique())
col3.metric("Active Days", filtered["watch_date_only"].nunique())
col4.metric("Avg Minutes / Session", round(filtered["duration_minutes"].mean() or 0, 1))

with st.expander("Top Genres"):
    fig = plot_top_genres(filtered)
    st.pyplot(fig)

with st.expander("Binge Hours Pattern"):
    fig = plot_binge_hours(filtered)
    st.pyplot(fig)

with st.expander("Genre x Hour Heatmap"):
    fig = plot_genre_heatmap(filtered)
    st.pyplot(fig)

with st.expander("Top Shows by Country (table)"):
    grouped = filtered.groupby(["country", "title"]).agg(total_minutes=("duration_minutes","sum"), sessions=("title","count")).reset_index()
    top_shows = grouped.sort_values("total_minutes", ascending=False).groupby("country").head(10)
    st.dataframe(top_shows)

st.caption("Built with Python, Pandas, Seaborn, Matplotlib & Streamlit")

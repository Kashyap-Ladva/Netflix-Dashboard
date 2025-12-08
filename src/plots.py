import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_style("whitegrid")

def plot_top_genres(df, top_n=10):
    rows = []
    for _, r in df.iterrows():
        for g in r.get("genre_list", []):
            rows.append((g, r.get("duration_minutes", 0)))

    gdf = pd.DataFrame(rows, columns=["genre", "duration"])
    agg = gdf.groupby("genre").agg(total_minutes=("duration","sum")).sort_values("total_minutes", ascending=False).head(top_n)
    fig, ax = plt.subplots(figsize=(8,5))

    sns.barplot(x=agg["total_minutes"].values, y=agg.index, ax=ax)
    ax.set_xlabel("Total Minutes Watched")
    ax.set_ylabel("Genre")
    ax.set_title("Top Genres by Watch Minutes")
    return fig

def plot_binge_hours(df):
    fig, ax = plt.subplots(figsize=(10,4))
    order = ["Morning (6-12)", "Afternoon (12-18)", "Evening (18-22)", "Night (22-6)"]
    counts = df.groupby("day_night")["duration_minutes"].sum().reindex(order).fillna(0)
    
    sns.barplot(x=counts.index, y=counts.values, ax=ax)
    ax.set_ylabel("Total Minutes")
    ax.set_title("Binge Hours Pattern (Day vs Night)")
    return fig

def plot_genre_heatmap(df):
    rows = []
    for _, r in df.iterrows():
        for g in r.get("genre_list", []):
            rows.append({"genre": g, "hour": r.get("watch_hour", 0), "duration": r.get("duration_minutes", 0)})
   
    gdf = pd.DataFrame(rows)
    pivot = gdf.pivot_table(index="genre", columns="hour", values="duration", aggfunc="sum", fill_value=0)
    pivot = pivot.loc[pivot.sum(axis=1).sort_values(ascending=False).head(12).index]
    fig, ax = plt.subplots(figsize=(12,6))
   
    sns.heatmap(pivot, ax=ax)
    ax.set_title("Genre x Hour Heatmap (total minutes)")
    return fig

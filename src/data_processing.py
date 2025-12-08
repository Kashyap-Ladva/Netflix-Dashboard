import pandas as pd
import numpy as np

def load_data(path: str):
    df = pd.read_csv(path)
    return df

def parse_datetime_columns(df, start_col="watch_start", end_col="watch_end"):
    if start_col in df.columns:
        df[start_col] = pd.to_datetime(df[start_col], errors='coerce')
    elif "watch_date" in df.columns:
        df[start_col] = pd.to_datetime(df["watch_date"], errors='coerce')
    if end_col and end_col in df.columns:
        df[end_col] = pd.to_datetime(df[end_col], errors='coerce')
    return df

def explode_genres(df, genre_col="genres", sep=r"[|,]"):
    df[genre_col] = df[genre_col].fillna("")
    df["genre_list"] = df[genre_col].str.split(sep, regex=True).apply(lambda arr: [g.strip() for g in arr if g and g.strip()])
    return df

def add_time_features(df, start_col="watch_start"):
    df["watch_hour"] = df[start_col].dt.hour
    df["watch_date_only"] = df[start_col].dt.date
    df["watch_year"] = df[start_col].dt.year
    df["day_night"] = df["watch_hour"].apply(lambda h: "Night (22-6)" if (h >= 22 or h < 6) else ("Evening (18-22)" if h>=18 else ("Afternoon (12-18)" if h>=12 else "Morning (6-12)")))
    return df

def preprocess(path):
    df = load_data(path)
    df = parse_datetime_columns(df)
    df = explode_genres(df)
    df = add_time_features(df)
    if "duration_minutes" in df.columns:
        df["duration_minutes"] = pd.to_numeric(df["duration_minutes"], errors='coerce').fillna(0)
    else:
        df["duration_minutes"] = np.nan
    return df

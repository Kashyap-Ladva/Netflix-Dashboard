#  Netflix / OTT Watch Pattern Dashboard

An interactive analytics dashboard that visualizes OTT streaming behavior — built with Python and Streamlit.

 **Live Demo:** [Click to Open App](https://netflix-dashboard-egrze9f9evsfym52evdcw7.streamlit.app/)

---

##  Overview

Upload your Netflix watch history and instantly explore your streaming patterns through interactive charts and filters.

**What it analyzes:**
- Top genres by watch time
- Binge hours pattern (day vs night viewing)
- Genre × Hour heatmap
- Top shows by country

**Filters available:** Genre → Year → Country

---

##  Tech Stack

| Tool | Usage |
|------|-------|
| Python | Core logic |
| Pandas | Data processing |
| Matplotlib & Seaborn | Visualizations |
| Streamlit | Dashboard UI + deployment |

---

##  Quick Start
```bash
# 1. Clone the repo
git clone https://github.com/Kashyap-Ladva/Netflix-Dashboard.git
cd Netflix-Dashboard

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
```

---

##  Dataset

Add your CSV to `data/watch_history.csv`  
See `data/sample_watch_history.csv` for the required schema.

> You can export your Netflix watch history from: **Netflix Account → Security & Privacy → Download your personal information**

---

##  Demo

![Dashboard Screenshot](assets/screenshot1.png)

---

##  Key Insights (Sample Data)

-  **Drama** is the most-watched genre
-  **Peak binge hours** fall between 10 PM – 1 AM
-  Viewing activity clusters around **weekends**
-  Content consumption varies significantly **by country**

---

##  Author

**Kashyap Ladva**  
CE Student @ GEC Gandhinagar | Data Science & ML  
[GitHub](https://github.com/Kashyap-Ladva)

**Kashyap Ladva**  
CE Student @ GEC Gandhinagar | Data Science & ML  
[GitHub](https://github.com/Kashyap-Ladva)

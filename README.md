# 🎬 Netflix IMDb Data – Data Engineering Project

This is a beginner-level data engineering project where I perform **data loading**, **cleaning**, and **visualization** using Python and a Netflix-style dataset with IMDb ratings.

## 📁 Dataset

The dataset (`netflix_data.csv`) contains metadata for Movies and TV Shows, including:

- Title
- Type (Movie/Show)
- Release Year
- Age Certification
- Runtime
- IMDb Score
- IMDb Votes

## 🔧 Tools Used

- Python
- pandas
- matplotlib
- seaborn

## 🧹 Data Cleaning Process

- Removed duplicate rows
- Dropped rows with missing critical fields (`type`, `release_year`, `imdb_score`, `runtime`)
- Filled missing `age_certification` with `"Unknown"`
- Filtered out rows with runtime ≤ 0
- Converted data types to numeric where needed

## 📊 Visualizations Included

- Count of Movies vs TV Shows
- Content Released Per Year
- IMDb Score Distribution
- Runtime Distribution by Type
- IMDb Votes vs Score (linear scale)
- Age Certification Distribution

## 🏁 How to Run This Project

1. **Clone this repo**
2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python analysis.py

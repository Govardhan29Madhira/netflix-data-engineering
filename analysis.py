
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV
df = pd.read_csv("netflix_data.csv")

# Data Cleaning Section
# 1. Inspect the data
print("Initial shape:", df.shape)
print(df.info())
print("\nMissing values per column:\n", df.isnull().sum())

# 2. Drop duplicates if any
df.drop_duplicates(inplace=True)

# 3. Handle missing values
# Drop rows with missing critical values
df.dropna(subset=['type', 'release_year', 'imdb_score', 'runtime'], inplace=True)

# Fill missing 'age_certification' with 'Unknown'
df['age_certification'] = df['age_certification'].fillna('Unknown')

# Convert datatypes explicitly
df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')
df['imdb_score'] = pd.to_numeric(df['imdb_score'], errors='coerce')
df['imdb_votes'] = pd.to_numeric(df['imdb_votes'], errors='coerce')

# Optional: remove rows with unrealistic runtime (e.g., 0 or negative)
df = df[df['runtime'] > 0]

# Final check
print("Cleaned shape:", df.shape)

# Visualizations
# 1. Count of Movies vs TV Shows
sns.countplot(data=df, x='type')
plt.title("Count of Movies vs TV Shows")
plt.show()

# 2. Content per Year
df_year = df['release_year'].value_counts().sort_index()
df_year.plot(kind='bar', figsize=(12, 5), title='Content Released Per Year')
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.show()

# 3. IMDb Score Distribution
sns.histplot(df['imdb_score'].dropna(), bins=20, kde=True)
plt.title("IMDb Score Distribution")
plt.xlabel("IMDb Score")
plt.ylabel("Number of Titles")
plt.show()

# 4. Runtime Boxplot
sns.boxplot(x='type', y='runtime', data=df)
plt.title("Runtime Distribution by Type")
plt.show()

# 5. IMDb Votes vs Score
sns.scatterplot(data=df, x='imdb_votes', y='imdb_score', hue='type')
plt.title("IMDb Votes vs Score")
plt.xscale('log')
plt.xlabel("IMDb Votes (log scale)")
plt.ylabel("IMDb Score")
plt.show()

# 6. Age Certification Distribution
sns.countplot(data=df, x='age_certification', order=df['age_certification'].value_counts().index)
plt.title("Age Certification Distribution")
plt.xticks(rotation=45)
plt.show()
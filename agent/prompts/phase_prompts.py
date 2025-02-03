eda_prompt = """
# 1. Data Collection & Initial Inspection

1.1 Import the dataset (CSV, SQL, APIs, etc.).
1.2 Check dataset structure:
- Number of rows and columns.
- Data types (numeric, categorical, datetime).
- Initial summary using df.head(), df.info(), df.describe().


# 2. Data Cleaning & Preprocessing
2.1 Handle missing data:
- Identify missing values (df.isnull().sum()).
- Decide on strategies: imputation (mean/median/mode), deletion, or advanced methods (e.g., KNN imputation).
- Remove duplicates (df.drop_duplicates()).

2.2 Detect and treat outliers:
- Statistical methods (Z-score, IQR).
- Fix data type mismatches (e.g., converting strings to datetime).
- Validate data consistency (e.g., categorical labels, numeric ranges).

# 3. Descriptive Statistics
3.1 Numeric variables: 
- Central tendency: mean, median.
- Spread: std dev, variance, IQR, range.

3.2 Categorical variables:
- Frequency counts (value_counts()).

Tools and libraries:
Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn.
"""
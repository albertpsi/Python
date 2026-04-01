# Data Analysis Quick Revision

Based on:

- `13.1-numpy.ipynb`
- `13.2-Pandas.ipynb`
- `13.3-DataAnalysis & Manipulation.ipynb`
- `13.4-Reading Data from Different Sources.ipynb`
- `13.5-Matplotlib.ipynb`
- `13.6-Seaborn.ipynb`

## 1. NumPy Basics

### Core idea

- NumPy is the foundation for numerical computing in Python.
- Its main object is `ndarray`, which supports fast, vectorized operations.
- It is the right choice when you need efficient math, reshaping, slicing, and array-based workflows.

### `numpy.array()` vs `array.array()`

- `array.array()` is from the Python standard library and is mainly a lightweight 1D typed container.
- `numpy.array()` creates an `ndarray` and supports 1D, 2D, and higher-dimensional arrays.
- `array.array()` is useful for compact storage.
- `numpy.array()` is better for numerical computing and data analysis.
- NumPy supports rich `dtype` choices such as `int32`, `float64`, and `bool`.
- Element-wise math works naturally with NumPy arrays.

### Array creation

- `np.array([...])`
- `np.arange(start, stop, step)`
- `np.ones((rows, cols))`
- `np.zeros((rows, cols))`
- `np.eye(n)`

### Shape and reshaping

- `arr.shape` shows the size of the array along each axis.
- `arr.ndim` gives the number of dimensions.
- `arr.reshape(r, c)` changes the layout when the total element count matches.
- A 1D array and a 2D array with one column are not the same thing.

### Indexing and slicing

- `arr[0]`
- `arr[1:4]`
- `matrix[0, 1]`
- `matrix[:, 2]`
- `matrix[1:3, 1:3]`

### Vectorization and ufuncs

- NumPy performs element-wise operations without explicit Python loops.
- Common functions in the notebooks include:
  - `np.sqrt(arr)`
  - `np.exp(arr)`
  - `np.sin(arr)`
  - `np.cos(arr)`
  - `np.tan(arr)`
  - `np.log(arr)`

### Statistics and logical filtering

- `np.mean(data)`
- `np.median(data)`
- `np.std(data)`
- `np.var(data)`
- Boolean masking filters values based on a condition.
- Common patterns:
  - `(data >= 5) & (data <= 8)`
  - `(data < 3) | (data > 7)`

### Why it matters

- Vectorized operations are shorter, faster, and easier to read than manual loops.
- NumPy is the base layer for most data science work in Python.

---

## 2. Pandas Series and DataFrame

### Core idea

- Pandas is the main library for tabular data manipulation and analysis.
- `Series` is one-dimensional.
- `DataFrame` is two-dimensional and can hold mixed data types.

### Common creation patterns

- Create a `Series` from a list, array, or dictionary.
- Create a `DataFrame` from a list of dictionaries or a dictionary of lists.
- Load tabular data with `pd.read_csv(...)`.

### Common inspection methods

- `head()`
- `tail()`
- `describe()`
- `axes`
- `type(...)`
- `DataFrame.shape`
- `DataFrame.columns`

### Quick revision points

- A `Series` is like a labeled column.
- A `DataFrame` is like a spreadsheet or SQL table.
- Pandas is used heavily for cleaning, transforming, and summarizing data.

---

## 3. Data Manipulation and Analysis with Pandas

### Core idea

- This notebook focuses on cleaning and transforming data before analysis.
- The example data starts from `data.csv` and then explores the DataFrame step by step.

### Data inspection

- `df.head()`
- `df.tail()`
- `df.describe()`
- `df.dtypes`
- `df.isnull().sum()`

### Missing value handling

- `df.fillna(0)` fills missing values with a fixed value.
- `df['sales_filled_mean'] = df['Sales'].fillna(df['Sales'].mean())` fills missing sales with the column mean.
- `isnull()` helps identify missing entries before cleaning.

### Column and type transformations

- `df.rename(columns={'Date': 'SalesDate'}, inplace=True)`
- `astype(...)` converts a column to a new data type.
- Example:
  - `df['New_Sales_value'] = df['sales_filled_mean'].astype(int)`

### Grouping and aggregation

- `df.groupby('Product')['Value'].mean()`
- `df.groupby(['Product', 'Region'])['Value'].sum()`
- `df.groupby(['Product', 'Region'])['Value'].mean()`
- `df.groupby('Region').agg({'Value': ['mean', 'sum', 'count']})`

### Merging and joining

- `pd.merge(df1, df2, on='Key', how='inner')`
- `pd.merge(df1, df2, on='Key', how='outer')`
- `pd.merge(df1, df2, on='Key', how='left')`
- `pd.merge(df1, df2, on='Key', how='right')`

### Interview note

- `groupby()` is for aggregating within one table.
- `merge()` is for combining related tables.
- `fillna()` is for repairing missing data.
- `astype()` is for controlling data types before analysis.

---

## 4. Reading Data From Different Sources

### Core idea

- Pandas can load data from files, URLs, HTML tables, JSON strings, and in-memory buffers.
- It can also write data back out in several formats.

### Reading data

- `pd.read_csv('file.csv')`
- `pd.read_csv(url)`
- `pd.read_csv(url, header=None)`
- `pd.read_excel('data.xlsx')`
- `pd.read_json(...)`
- `pd.read_pickle('data.pkl')`
- `pd.read_html(url)`
- `pd.read_html(url, match='Country', header=0)[0]`

### In-memory parsing

- `StringIO` lets you read JSON text from a string.
- This is useful for small examples and API-style payloads.

### Writing data

- `to_csv(...)`
- `to_json(...)`
- `to_pickle(...)`

### Important details from the notebook

- `pd.read_html()` returns a list of DataFrames, not a single DataFrame.
- The notebook shows a Wikipedia example and notes that some sites may require a custom `User-Agent`.
- The source-loading examples also use `titanic.csv`, `data.xlsx`, `data.pkl`, and remote CSV URLs.

---

## 5. Data Visualization With Matplotlib

### Core idea

- Matplotlib is the base plotting library in Python.
- It is flexible and works well when you need full control over charts.

### Common plot types

- Line plot
- Bar plot
- Histogram
- Scatter plot
- Pie chart
- Multiple plots with `subplot()`

### Common controls

- `plt.figure(...)`
- `plt.plot(...)`
- `plt.bar(...)`
- `plt.hist(...)`
- `plt.scatter(...)`
- `plt.pie(...)`
- `plt.subplot(...)`
- `plt.title(...)`
- `plt.xlabel(...)`
- `plt.ylabel(...)`
- `plt.grid(...)`
- `plt.tight_layout()`
- `plt.show()`

### Sales examples from the notebook

- The notebook loads `sales_matplotlib_data.csv`.
- It groups sales by product and plots total sales with a bar chart.
- It converts the `Date` column with `pd.to_datetime(...)`.
- It sorts the data by date and plots a sales trend line over time.

### Revision note

- Matplotlib is best when you want detailed control over layout and formatting.
- It is often the foundation under higher-level plotting libraries.

---

## 6. Data Visualization With Seaborn

### Core idea

- Seaborn is built on top of Matplotlib.
- It provides a higher-level interface for statistical graphics and cleaner default styling.

### Datasets and setup

- The notebook uses `sns.load_dataset('tips')`.
- It also uses `sales_data.csv` for a business-style bar chart.

### Plot types covered

- `sns.scatterplot(...)`
- `sns.lineplot(...)`
- `sns.barplot(...)`
- `sns.boxplot(...)`
- `sns.violinplot(...)`
- `sns.histplot(..., kde=True)`
- `sns.kdeplot(...)`
- `sns.pairplot(...)`
- `sns.heatmap(...)`

### Correlation and summary visuals

- `sns.load_dataset('tips')[['total_bill', 'tip', 'size']].corr()`
- `sns.heatmap(..., annot=True, cmap='coolwarm')`

### Sales example from the notebook

- The notebook plots `Product Category` against `Total Revenue` with `sns.barplot(...)`.
- `plt.figure(figsize=(10, 6))` is used to control chart size.

### Revision note

- Seaborn is ideal for quick statistical plots with polished defaults.
- It is especially handy for relationships, distributions, categorical comparisons, and correlation heatmaps.

---

## Frequently Asked Interview Questions

1. **Why use NumPy instead of plain Python lists for numerical work?**

- NumPy is faster, supports vectorized operations, and handles multi-dimensional arrays well.

2. **What do `shape` and `ndim` tell you?**

- `shape` gives the size along each axis.
- `ndim` gives the number of axes.

3. **What is vectorization?**

- Performing operations on whole arrays at once instead of looping element by element in Python.

4. **What is the use of `reshape()`?**

- It changes the arrangement of data without changing the underlying values.

5. **What is boolean masking?**

- Filtering array elements using a condition that evaluates to `True` or `False`.

6. **What is the difference between `Series` and `DataFrame`?**

- A `Series` is one-dimensional.
- A `DataFrame` is a two-dimensional table.

7. **When would you use `groupby()` vs `merge()`?**

- Use `groupby()` to aggregate within one DataFrame.
- Use `merge()` to combine related DataFrames.

8. **What does `pd.read_html()` return?**

- It returns a list of DataFrames, one per HTML table found.

9. **When should you use Matplotlib vs Seaborn?**

- Use Matplotlib for low-level control.
- Use Seaborn for faster, more polished statistical plots.

---

## Last-Minute Revision Checklist

- Memorize NumPy array-creation functions.
- Revise `shape`, `ndim`, and `reshape()`.
- Practice indexing, slicing, and boolean masking on 2D arrays.
- Remember vectorized operations and common ufuncs like `sqrt`, `exp`, `sin`, `cos`, `tan`, and `log`.
- Revise `Series` vs `DataFrame` and the common Pandas inspection methods.
- Be comfortable with `fillna()`, `astype()`, `groupby()`, `agg()`, and `merge()`.
- Remember how to read and write CSV, Excel, JSON, pickle, and HTML data.
- Practice the main Matplotlib chart types and labeling functions.
- Know the Seaborn plots used in the notebooks, especially bar, box, violin, pair, histogram, KDE, and heatmap.

# Brainwave_Matrix_Intern - Sales Data Analysis

This repository contains a Python script (`Analysis.py`) and a sales dataset (`sales_data.csv`) designed for exploratory data analysis (EDA). The project aims to analyze sales data, uncover trends, and generate insights that can be used to make informed business decisions.  This README will guide you through setting up and running the project within PyCharm.

## Project Overview

The `Analysis.py` script performs the following key tasks:

1. **Data Loading:** Reads sales data from `sales_data.csv` into a Pandas DataFrame.
2. **Exploratory Data Analysis (EDA):**
    * Displays the first few rows of the data using `df.head()`.
    * Provides information about data types and missing values using `df.info()`.
    * Calculates descriptive statistics using `df.describe()`.
    * Checks for missing values using `df.isnull().sum()`.
3. **Data Preprocessing:**
    * Converts the 'Date' column to datetime objects using `pd.to_datetime()` for proper time-series analysis.
    * *(Add any other preprocessing steps here, like handling missing values if you have them)*
4. **Data Visualization:**
    * Generates visualizations to explore trends and relationships:
        * Sales trends over time (line plot using `seaborn.lineplot`).
        * Best-selling products (bar plot using `seaborn.barplot`).
        * Revenue by store (bar plot using `seaborn.barplot`).
        * Distribution of unit price (histogram using `seaborn.histplot`).
        * *(Add other visualizations you create here)*
5. **Insights:** The script prints key insights observed from the data analysis.
         - Product X is the best-selling product overall.
         - Store A generates the highest revenue.
         - There might be a seasonal trend in sales (further investigation needed).
         - The unit price distribution shows that most products fall within a certain range.

## Dataset

The `sales_data.csv` file contains the following columns:

* **Date:** The date of the sale (YYYY-MM-DD format).
* **Store:** The store where the sale took place (e.g., Store A, Store B, Store C).
* **Product:** The product sold (e.g., Product X, Product Y, Product Z).
* **Quantity:** The number of units sold.
* **UnitPrice:** The price per unit.

## How to Run the Project in PyCharm

1. **Clone the Repository:**
   * In PyCharm, go to *VCS > Get from Version Control...*
   * Enter the repository URL: `https://github.com/harshansai30/Brainwave_Matrix_Intern.git` 
   * Choose the directory where you want to clone the project.

2. **Open the Project:**
   * In PyCharm, go to *File > Open...* and select the directory where you cloned the repository.

3. **Set up a Virtual Environment (Highly Recommended):**
   * In PyCharm, go to *File > Settings* (or *PyCharm > Preferences* on macOS).
   * Select *Project: Brainwave_Matrix_Intern > Project Interpreter*.
   * Click the gear icon and select *Add...*
   * Choose *New environment*.
   * Select *venv* as the environment type.
   * Choose a base interpreter (your system's Python).
   * Click *OK* to create the virtual environment.

4. **Install Required Packages:**
   * Open the PyCharm Terminal (*View > Tool Windows > Terminal*).
   * Activate your virtual environment (if it's not already):
     * On Windows: `venv\Scripts\activate`
     * On macOS/Linux: `source venv/bin/activate`
   * Install the necessary libraries:
     ```bash
     pip install pandas matplotlib seaborn
     ```

5. **Place `sales_data.csv` in the Correct Location:**

   * **Crucially, ensure that `sales_data.csv` is in the same directory as `Analysis.py`.**  This is the most common reason for the `FileNotFoundError`.  You can drag and drop the `sales_data.csv` file within the PyCharm project view to ensure it's in the correct location.

6. **Run the Script:**
   * Open `Analysis.py` in the editor.
   * Right-click in the editor window and select *Run 'Analysis'*.  (PyCharm will likely create a run configuration for you automatically).

## Troubleshooting the `FileNotFoundError`

The error `FileNotFoundError: [Errno 2] No such file or directory: 'sales_data.csv'` usually means that Python can't find the CSV file.  Here are the most important things to check:

1. **File Location:** *Absolutely make sure `sales_data.csv` is in the same directory as `Analysis.py`.*  Use the PyCharm project view to verify this.  If it's not, drag and drop it to the correct location.
2. **Typos:** Double-check for any typos in the filename `sales_data.csv` in your code and the actual filename.  Case matters!
3. **Working Directory (Less Common in PyCharm):** While less common in PyCharm, you can check the working directory in your run configuration (Run > Edit Configurations...).  However, if you've placed the file correctly, this shouldn't be an issue.

## Project Structure

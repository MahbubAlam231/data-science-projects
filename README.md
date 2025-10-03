# Data Analysis with car data

## Overview

This script performs automated **data cleaning and preprocessing** for the `auto_raw.csv` dataset, which contains automobile attributes. It applies various data preparation techniques to handle missing values, transform variables, and generate useful features for analysis or modeling.

## Features

* **Load Data**: Reads raw automobile dataset (`auto_raw.csv`) into a Pandas DataFrame.
* **Missing Data Handling**:

  * Replaces `?` with `NaN`.
  * Imputes numeric columns (`normalized_losses`, `bore`, `stroke`, `horsepower`, `peak_rpm`) with mean values.
  * Imputes categorical column (`num_of_doors`) with the most frequent value.
  * Drops rows where `price` is missing.
* **Data Type Conversion**: Converts numerical columns to `float` or `int` for consistency.
* **Feature Engineering**:

  * Standardization: Converts fuel consumption from mpg to L/100km.
  * Normalization: Scales `length`, `width`, and `height`.
  * Binning: Groups horsepower into `Low`, `Medium`, and `High`.
* **Visualization**:

  * Generates histograms and bar charts for horsepower distribution.
  * Saves plots as `.jpg` files (`horsepower_hist.jpg`, `horsepower_bins.jpg`, `horsepower_bins_from_hist.jpg`).
* **Indicator Variables**:

  * Creates dummy variables for `fuel_type` and `aspiration`.
* **Output**:

  * Optionally saves the cleaned dataset as `clean_auto.csv`.

## Requirements

* Python 3.x
* Libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`

Install dependencies (if needed):

```bash
pip install pandas numpy matplotlib seaborn
```

## Usage

Run the script directly:

```bash
python data_cleaning_auto.py
```

This will:

1. Clean and preprocess the dataset.
2. Save visualizations as image files.
3. Print sample outputs to the console.
4. (Optional) Export cleaned dataset as `clean_auto.csv` (uncomment the relevant line).

---

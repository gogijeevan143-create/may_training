# Titanic Data Preprocessing Assignment

This project completes **Test 03 - Data Preprocessing Assignment (No Model Training)**.

## Dataset Choice

I selected a Titanic-style passenger survival dataset because it is one of the best datasets for preprocessing practice. It has:

- A clear target variable: `survived`
- Numeric columns: `age`, `fare`, `sibsp`, `parch`
- Categorical columns: `sex`, `embarked`, `deck`
- Missing values
- Duplicate records
- Outliers
- Skewed fare values
- Redundant identifier/text columns

## Files

- `data/raw/titanic_raw.csv` - original raw dataset
- `preprocess_titanic.py` - preprocessing code only
- `outputs/cleaned_titanic_preprocessed.csv` - cleaned dataset ready for modeling
- `outputs/preprocessing_report.md` - explanation of every preprocessing step
- `requirements.txt` - Python packages used

## Preprocessing Steps Covered

1. Understanding the dataset shape, columns, and target variable
2. Checking and handling missing values
3. Removing duplicate records
4. Detecting and handling outliers
5. Handling incorrect data types
6. Handling categorical variables
7. Feature scaling
8. Removing irrelevant or redundant features
9. Handling skewness

## Run

```bash
python3 preprocess_titanic.py
```

The cleaned CSV and report will be generated inside the `outputs` folder.

## Note

No machine learning model is trained in this assignment.

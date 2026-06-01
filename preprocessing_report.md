# Titanic Data Preprocessing Report

## 1. Dataset Understanding
- Original shape: `60` rows and `12` columns.
- Target variable: `survived`.
- Dataset type: passenger survival records with numeric and categorical features.

### Original Columns
`passenger_id`, `survived`, `pclass`, `name`, `sex`, `age`, `sibsp`, `parch`, `ticket`, `fare`, `cabin`, `embarked`

## 2. Missing Values
Missing values before cleaning:
- `age`: 14
- `cabin`: 44

Handling method:
- `age`: filled with median age grouped by `sex` and `pclass`.
- `fare`: filled with median fare grouped by `pclass`.
- `embarked`: filled with mode.
- `cabin`: filled as `Unknown` so a deck feature can be extracted.

## 3. Duplicate Records
- Duplicate passenger records removed: `1`.
- Shape after duplicate removal: `59` rows and `12` columns.

## 4. Incorrect Data Types
- Converted `survived`, `pclass`, `sibsp`, and `parch` to integer.
- Converted `age` and `fare` to numeric values.

## 5. Feature Engineering and Redundant Features
- Created `family_size` from `sibsp` and `parch`.
- Created `is_alone` from `family_size`.
- Extracted `deck` from `cabin`.
- Removed identifiers and high-cardinality text fields: `passenger_id`, `name`, `ticket`, `cabin`.

## 6. Outliers
- `age`: capped 1 outliers to IQR bounds (-7.50, 60.50).
- `fare`: capped 5 outliers to IQR bounds (-40.83, 89.51).
- `family_size`: capped 4 outliers to IQR bounds (-2.00, 6.00).

## 7. Skewness
- `fare` skewness before log transform: `1.198`.
- `fare_log` skewness after `log1p`: `0.332`.

## 8. Categorical Encoding
- `sex`: binary label encoding because it has two categories.
- `embarked` and `deck`: one-hot encoding because they are nominal categories.
- `pclass`: kept as an ordinal numeric feature because 1st, 2nd, and 3rd class have natural order.

## 9. Feature Scaling
- Applied `StandardScaler` to all feature columns.
- The target column `survived` was not scaled.

## Final Output
- Cleaned dataset shape: `59` rows and `19` columns.
- Output file: `cleaned_titanic_preprocessed.csv`.
- No machine learning model was trained.

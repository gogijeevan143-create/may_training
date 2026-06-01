from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


BASE_DIR = Path(__file__).resolve().parent
RAW_PATH = BASE_DIR / "data" / "raw" / "titanic_raw.csv"
OUTPUT_DIR = BASE_DIR / "outputs"
CLEANED_PATH = OUTPUT_DIR / "cleaned_titanic_preprocessed.csv"
REPORT_PATH = OUTPUT_DIR / "preprocessing_report.md"


def cap_outliers_iqr(series: pd.Series) -> tuple[pd.Series, float, float, int]:
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    outlier_count = int(((series < lower) | (series > upper)).sum())
    return series.clip(lower, upper), float(lower), float(upper), outlier_count


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    raw_df = pd.read_csv(RAW_PATH)
    df = raw_df.copy()
    report: list[str] = []

    report.append("# Titanic Data Preprocessing Report")
    report.append("")
    report.append("## 1. Dataset Understanding")
    report.append(f"- Original shape: `{df.shape[0]}` rows and `{df.shape[1]}` columns.")
    report.append("- Target variable: `survived`.")
    report.append("- Dataset type: passenger survival records with numeric and categorical features.")
    report.append("")
    report.append("### Original Columns")
    report.append(", ".join(f"`{column}`" for column in df.columns))
    report.append("")

    report.append("## 2. Missing Values")
    missing_before = df.isna().sum()
    report.append("Missing values before cleaning:")
    for column, count in missing_before[missing_before > 0].items():
        report.append(f"- `{column}`: {int(count)}")
    report.append("")

    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df["fare"] = pd.to_numeric(df["fare"], errors="coerce")
    df["embarked"] = df["embarked"].fillna(df["embarked"].mode()[0])
    df["age"] = df.groupby(["sex", "pclass"])["age"].transform(lambda col: col.fillna(col.median()))
    df["fare"] = df.groupby("pclass")["fare"].transform(lambda col: col.fillna(col.median()))
    df["cabin"] = df["cabin"].fillna("Unknown")

    report.append("Handling method:")
    report.append("- `age`: filled with median age grouped by `sex` and `pclass`.")
    report.append("- `fare`: filled with median fare grouped by `pclass`.")
    report.append("- `embarked`: filled with mode.")
    report.append("- `cabin`: filled as `Unknown` so a deck feature can be extracted.")
    report.append("")

    report.append("## 3. Duplicate Records")
    duplicate_count = int(df.duplicated(subset=df.columns.drop("passenger_id")).sum())
    df = df.drop_duplicates(subset=df.columns.drop("passenger_id")).reset_index(drop=True)
    report.append(f"- Duplicate passenger records removed: `{duplicate_count}`.")
    report.append(f"- Shape after duplicate removal: `{df.shape[0]}` rows and `{df.shape[1]}` columns.")
    report.append("")

    report.append("## 4. Incorrect Data Types")
    df["survived"] = df["survived"].astype(int)
    df["pclass"] = df["pclass"].astype(int)
    df["sibsp"] = df["sibsp"].astype(int)
    df["parch"] = df["parch"].astype(int)
    report.append("- Converted `survived`, `pclass`, `sibsp`, and `parch` to integer.")
    report.append("- Converted `age` and `fare` to numeric values.")
    report.append("")

    report.append("## 5. Feature Engineering and Redundant Features")
    df["family_size"] = df["sibsp"] + df["parch"] + 1
    df["is_alone"] = (df["family_size"] == 1).astype(int)
    df["deck"] = df["cabin"].str[0].replace("U", "Unknown")
    report.append("- Created `family_size` from `sibsp` and `parch`.")
    report.append("- Created `is_alone` from `family_size`.")
    report.append("- Extracted `deck` from `cabin`.")
    report.append("- Removed identifiers and high-cardinality text fields: `passenger_id`, `name`, `ticket`, `cabin`.")
    report.append("")
    df = df.drop(columns=["passenger_id", "name", "ticket", "cabin"])

    report.append("## 6. Outliers")
    outlier_lines = []
    for column in ["age", "fare", "family_size"]:
        df[column], lower, upper, count = cap_outliers_iqr(df[column])
        outlier_lines.append(f"- `{column}`: capped {count} outliers to IQR bounds ({lower:.2f}, {upper:.2f}).")
    report.extend(outlier_lines)
    report.append("")

    report.append("## 7. Skewness")
    skew_before = float(df["fare"].skew())
    df["fare_log"] = np.log1p(df["fare"])
    df = df.drop(columns=["fare"])
    skew_after = float(df["fare_log"].skew())
    report.append(f"- `fare` skewness before log transform: `{skew_before:.3f}`.")
    report.append(f"- `fare_log` skewness after `log1p`: `{skew_after:.3f}`.")
    report.append("")

    report.append("## 8. Categorical Encoding")
    df["sex"] = df["sex"].map({"male": 0, "female": 1}).astype(int)
    df = pd.get_dummies(df, columns=["embarked", "deck"], drop_first=False, dtype=int)
    report.append("- `sex`: binary label encoding because it has two categories.")
    report.append("- `embarked` and `deck`: one-hot encoding because they are nominal categories.")
    report.append("- `pclass`: kept as an ordinal numeric feature because 1st, 2nd, and 3rd class have natural order.")
    report.append("")

    report.append("## 9. Feature Scaling")
    target = df["survived"]
    features = df.drop(columns=["survived"])
    scaler = StandardScaler()
    scaled_features = pd.DataFrame(
        scaler.fit_transform(features),
        columns=features.columns,
        index=features.index,
    )
    cleaned_df = pd.concat([target, scaled_features], axis=1)
    report.append("- Applied `StandardScaler` to all feature columns.")
    report.append("- The target column `survived` was not scaled.")
    report.append("")

    report.append("## Final Output")
    report.append(f"- Cleaned dataset shape: `{cleaned_df.shape[0]}` rows and `{cleaned_df.shape[1]}` columns.")
    report.append(f"- Output file: `{CLEANED_PATH.name}`.")
    report.append("- No machine learning model was trained.")
    report.append("")

    cleaned_df.to_csv(CLEANED_PATH, index=False)
    REPORT_PATH.write_text("\n".join(report), encoding="utf-8")

    print(f"Raw dataset: {RAW_PATH}")
    print(f"Cleaned dataset saved to: {CLEANED_PATH}")
    print(f"Report saved to: {REPORT_PATH}")
    print(f"Final shape: {cleaned_df.shape}")


if __name__ == "__main__":
    main()

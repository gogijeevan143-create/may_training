# Model Evaluation Report

This report is created after data cleaning and preprocessing.

## Dataset Split
- Training rows: `44`
- Testing rows: `15`
- Target variable: `survived`

## Algorithms Applied
1. Logistic Regression
2. K-Nearest Neighbors
3. Random Forest

## Logistic Regression

- Accuracy: `0.867`
- Precision: `0.778`
- Recall: `1.000`
- F1 Score: `0.875`

### Confusion Matrix
| Actual / Predicted | Predicted 0 | Predicted 1 |
|---|---:|---:|
| Actual 0 | 6 | 2 |
| Actual 1 | 0 | 7 |

### Classification Report
```text
              precision    recall  f1-score   support

           0       1.00      0.75      0.86         8
           1       0.78      1.00      0.88         7

    accuracy                           0.87        15
   macro avg       0.89      0.88      0.87        15
weighted avg       0.90      0.87      0.87        15

```

## K-Nearest Neighbors

- Accuracy: `0.800`
- Precision: `0.833`
- Recall: `0.714`
- F1 Score: `0.769`

### Confusion Matrix
| Actual / Predicted | Predicted 0 | Predicted 1 |
|---|---:|---:|
| Actual 0 | 7 | 1 |
| Actual 1 | 2 | 5 |

### Classification Report
```text
              precision    recall  f1-score   support

           0       0.78      0.88      0.82         8
           1       0.83      0.71      0.77         7

    accuracy                           0.80        15
   macro avg       0.81      0.79      0.80        15
weighted avg       0.80      0.80      0.80        15

```

## Random Forest

- Accuracy: `0.867`
- Precision: `0.778`
- Recall: `1.000`
- F1 Score: `0.875`

### Confusion Matrix
| Actual / Predicted | Predicted 0 | Predicted 1 |
|---|---:|---:|
| Actual 0 | 6 | 2 |
| Actual 1 | 0 | 7 |

### Classification Report
```text
              precision    recall  f1-score   support

           0       1.00      0.75      0.86         8
           1       0.78      1.00      0.88         7

    accuracy                           0.87        15
   macro avg       0.89      0.88      0.87        15
weighted avg       0.90      0.87      0.87        15

```

## Summary Comparison

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---:|---:|---:|---:|
| Logistic Regression | 0.867 | 0.778 | 1.000 | 0.875 |
| K-Nearest Neighbors | 0.800 | 0.833 | 0.714 | 0.769 |
| Random Forest | 0.867 | 0.778 | 1.000 | 0.875 |

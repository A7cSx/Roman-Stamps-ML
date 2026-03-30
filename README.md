# 🏺 Predicting Roman Amphora Stamp Types Using Machine Learning

> Can we predict what type of ancient Roman amphora stamp was found at a location — just by knowing its geographic coordinates?  
> This project uses real archaeological data to answer that question.

---

## 💡 Motivation

Roman amphora stamps are small clay marks pressed onto ancient storage jars (amphorae) that carried goods like olive oil, wine, and fish sauce across the Roman Empire. Each stamp type is linked to a specific production region.

The **CEIPAC dataset** contains over 24,000 recorded stamp finds across Roman provinces. By applying machine learning to this data, we can explore whether **geography alone** can predict the stamp type — and by extension, reveal ancient trade patterns.

---

## ❓ Questions of Interest

1. Which Roman provinces have the most recorded stamp finds?
2. What are the most common amphora stamp types in the dataset?
3. Can geographic coordinates (latitude & longitude) predict the stamp type?
4. Which coordinate — latitude or longitude — is more predictive?

---

## 📚 Libraries Used

| Library | Purpose |
|---|---|
| `pandas` | Data loading and manipulation |
| `numpy` | Numerical operations |
| `matplotlib` / `seaborn` | Data visualization |
| `scikit-learn` | Machine learning models and evaluation |

---

## 📁 File Structure

```
Stamp-ML-Project/
│
├── stamps.csv               # Raw dataset (24,092 records)
├── stamp_analysis.ipynb     # Full analysis notebook (CRISP-DM)
├── main.py                  # Python script version
├── README.md                # Project documentation
└── images/
    ├── top_provinces.png
    ├── lat_long_distribution.png
    ├── confusion_matrix.png
    └── feature_importance.png
```

---

## 📊 Dataset Overview

- **Rows:** 24,092 stamp records
- **Columns:** 9 (location, type, province, site, code)
- **Source:** CEIPAC — Centre for the Study of Roman Amphoras
- **Coverage:** Roman provinces across Europe, North Africa, and the Middle East

| Column | Description |
|---|---|
| `lat` / `long` | Geographic coordinates of find site |
| `type` | Amphora stamp type (target variable) |
| `name` | Roman province name |
| `site` | Archaeological site name |
| `code` | Stamp code |

---

## 🔍 Key Findings

### Top Provinces by Stamp Count
| Province | Stamps Found |
|---|---|
| Italia | 6,832 |
| Narbonensis | 3,498 |
| Tarraconensis | 2,526 |
| Germania Superior | 2,365 |
| Britannia | 1,980 |

### Model Performance
| Model | Accuracy |
|---|---|
| **Random Forest** | **69.6%** |
| Logistic Regression | 62.5% |
| Cross-Validation (RF, 5-fold) | **71.8%** |

### Feature Importance
| Feature | Importance |
|---|---|
| Longitude | 51.7% |
| Latitude | 48.3% |

> Both coordinates contribute nearly equally, confirming that stamp type distribution is genuinely spatial — not just north-south or east-west.

---

## ✅ Summary

- Random Forest outperforms Logistic Regression by ~7 percentage points
- **Dressel 20** (olive oil from Baetica, modern Spain) is the dominant stamp type with 10,238 records
- **Brindisian amphora** achieved the highest per-class accuracy (97%) due to its geographically concentrated distribution in southern Italy
- Geographic coordinates alone can predict stamp type with ~70% accuracy — a strong signal that Roman trade routes created distinct spatial patterns in the archaeological record

---

## 🚀 How to Run

```bash
# Install dependencies
pip install pandas numpy matplotlib seaborn scikit-learn

# Run the script
python main.py

# Or open the notebook
jupyter notebook stamp_analysis.ipynb
```

---

## 👤 Author

Abdulrahman  
Data Science Nanodegree — Udacity  

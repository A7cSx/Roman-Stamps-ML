import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder

# =========================================
# OUTPUT FOLDER SETUP
# =========================================
IMAGES_DIR = "images"
os.makedirs(IMAGES_DIR, exist_ok=True)

# =========================================
# 1. DATA LOADING (CRISP-DM: Data Understanding)
# =========================================
df = pd.read_csv('stamps.csv')

print("Dataset Shape:", df.shape)
print(df.head())
print(df.info())

# =========================================
# 2. EXPLORATORY DATA ANALYSIS (EDA)
# =========================================

# Top provinces
plt.figure(figsize=(10, 5))
df['name'].value_counts().head(10).plot(kind='bar', color='steelblue')
plt.title('Top 10 Provinces by Stamp Count')
plt.xlabel('Province')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(os.path.join(IMAGES_DIR, 'top_provinces.png'), dpi=150)
plt.close()
print("Saved: top_provinces.png")

# Latitude & Longitude distribution
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
sns.histplot(df['lat'], kde=True, color='steelblue')
plt.title('Latitude Distribution')

plt.subplot(1, 2, 2)
sns.histplot(df['long'], kde=True, color='darkorange')
plt.title('Longitude Distribution')
plt.tight_layout()
plt.savefig(os.path.join(IMAGES_DIR, 'lat_long_distribution.png'), dpi=150)
plt.close()
print("Saved: lat_long_distribution.png")

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# =========================================
# 3. DATA CLEANING (CRISP-DM: Data Preparation)
# =========================================
df_clean = df.copy()

# Fix swapped coordinates
df_clean.rename(columns={'lat': 'longitude', 'long': 'latitude'}, inplace=True)

# Drop missing values
df_clean.dropna(subset=['name', 'type'], inplace=True)

# Drop unnecessary columns
df_clean.drop(columns=['X', 'Y', 'id'], inplace=True)

# Remove rare classes (keep types with >= 100 records)
type_counts = df_clean['type'].value_counts()
valid_types = type_counts[type_counts >= 100].index
df_clean = df_clean[df_clean['type'].isin(valid_types)]

print("Cleaned Dataset Shape:", df_clean.shape)

# =========================================
# 4. FEATURE SELECTION
# =========================================
X = df_clean[['latitude', 'longitude']]

le = LabelEncoder()
y = le.fit_transform(df_clean['type'])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# =========================================
# 5. MODELING
# =========================================
rf = RandomForestClassifier(n_estimators=200, class_weight='balanced', random_state=42)
rf.fit(X_train, y_train)

lr = LogisticRegression(max_iter=2000)
lr.fit(X_train, y_train)

# =========================================
# 6. EVALUATION
# =========================================
def evaluate_model(model, X_test, y_test, name):
    y_pred = model.predict(X_test)
    print(f"\n==== {name} ====")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred, target_names=le.classes_))

evaluate_model(rf, X_test, y_test, "Random Forest")
evaluate_model(lr, X_test, y_test, "Logistic Regression")

# Confusion Matrix
plt.figure(figsize=(10, 8))
sns.heatmap(confusion_matrix(y_test, rf.predict(X_test)),
            annot=True,
            fmt='d',
            xticklabels=le.classes_,
            yticklabels=le.classes_,
            cmap='Blues')
plt.title('Random Forest Confusion Matrix')
plt.tight_layout()
plt.savefig(os.path.join(IMAGES_DIR, 'confusion_matrix.png'), dpi=150)
plt.close()
print("Saved: confusion_matrix.png")

# =========================================
# 7. FEATURE IMPORTANCE
# =========================================
importances = rf.feature_importances_
feature_names = X.columns

plt.figure(figsize=(6, 4))
plt.bar(feature_names, importances, color=['steelblue', 'darkorange'])
plt.title("Feature Importance")
plt.ylabel("Importance Score")
plt.tight_layout()
plt.savefig(os.path.join(IMAGES_DIR, 'feature_importance.png'), dpi=150)
plt.close()
print("Saved: feature_importance.png")

# =========================================
# 8. CROSS VALIDATION
# =========================================
cv_scores = cross_val_score(rf, X, y, cv=5)
print("\nCross Validation Scores:", cv_scores)
print("Average CV Score:", cv_scores.mean())

# =========================================
# 9. SCENARIO PREDICTION
# =========================================
def predict_scenario(lat, lon):
    input_data = pd.DataFrame([[lat, lon]], columns=['latitude', 'longitude'])
    pred = rf.predict(input_data)
    return le.inverse_transform(pred)[0]

result = predict_scenario(45.0, 5.0)
print("\nPrediction for location (45,5):", result)

print("\n✅ All charts saved to the 'images/' folder.")
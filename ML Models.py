

# ML Models for Food Matching


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

# ----------------- Sample Data Creation -----------------
donation_types = ['Fruits', 'Vegetables', 'Canned Goods', 'Bread', 'Dairy', 'Cooked Meals']
perishability_map = {'Fruits': 3, 'Vegetables': 3, 'Canned Goods': 1, 'Bread': 2, 'Dairy': 3, 'Cooked Meals': 4}

ml_data = pd.DataFrame({
    'Donation_Type': np.random.choice(donation_types, 300),
    'Quantity_kg': np.random.randint(1, 30, 300),
    'Distance_km': np.random.normal(10, 3, 300).clip(1, 25),
    'Match_Success': np.random.choice([0, 1], 300, p=[0.2, 0.8])
})

ml_data['Perishability'] = ml_data['Donation_Type'].map(perishability_map)

# ----------------- Logistic Regression -----------------
print("----- Logistic Regression -----")
X = ml_data[['Donation_Type', 'Quantity_kg', 'Distance_km']]
y = ml_data['Match_Success']

preprocessor = ColumnTransformer([
    ('cat', OneHotEncoder(), ['Donation_Type']),
    ('num', StandardScaler(), ['Quantity_kg', 'Distance_km'])
])

pipeline = Pipeline([
    ('prep', preprocessor),
    ('clf', LogisticRegression())
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
pipeline.fit(X_train, y_train)
lr_preds = pipeline.predict(X_test)
print(classification_report(y_test, lr_preds))

# ----------------- Random Forest Classifier -----------------
print("----- Random Forest Classifier -----")
X_rf = ml_data[['Donation_Type', 'Quantity_kg', 'Distance_km', 'Perishability']]
rf_preprocessor = ColumnTransformer([
    ('cat', OneHotEncoder(), ['Donation_Type']),
    ('num', StandardScaler(), ['Quantity_kg', 'Distance_km', 'Perishability'])
])

rf_pipeline = Pipeline([
    ('prep', rf_preprocessor),
    ('clf', RandomForestClassifier(n_estimators=100, random_state=42))
])

X_train_rf, X_test_rf, y_train_rf, y_test_rf = train_test_split(X_rf, y, test_size=0.2, random_state=42)
rf_pipeline.fit(X_train_rf, y_train_rf)
rf_preds = rf_pipeline.predict(X_test_rf)
print(classification_report(y_test_rf, rf_preds))

# ----------------- KMeans Clustering -----------------
print("----- KMeans Clustering -----")
donor_data = pd.DataFrame({
    'Donor_Lat': np.random.uniform(32.7, 33.2, 300),
    'Donor_Lon': np.random.uniform(-117.3, -116.9, 300),
    'Quantity_kg': np.random.randint(1, 50, 300)
})

X_clust = StandardScaler().fit_transform(donor_data)
kmeans = KMeans(n_clusters=3, random_state=42)
donor_data['Cluster'] = kmeans.fit_predict(X_clust)

print(donor_data['Cluster'].value_counts())

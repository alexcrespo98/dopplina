import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Path to your features CSV
FEATURES_CSV = os.path.join("preprocessed_data", "doppler_features.csv")
MODEL_PATH = "doppler_classifier.pkl"

def main():
    # Check for file existence
    if not os.path.exists(FEATURES_CSV):
        print(f"bro... I'm expecting a file at {FEATURES_CSV}, but I don't see it.")
        return

    # Load all data
    df = pd.read_csv(FEATURES_CSV)

    expected_cols = ['file', 'label', 'peak_freq', 'avg_amp', 'std_amp']
    missing_cols = [col for col in expected_cols if col not in df.columns]
    if missing_cols:
        print(f"bro... I'm expecting columns {expected_cols}, but you're missing {missing_cols} in your features file.")
        return

    # Features and labels
    X = df[['peak_freq', 'avg_amp', 'std_amp']]
    y = df['label']

    # Check shape
    if X.shape[0] < 2 or y.shape[0] < 2:
        print(f"bro... I'm expecting at least 2 rows to train, but you're giving me {X.shape[0]}.")
        return

    # Check for more than one class
    if len(set(y)) < 2:
        print(f"bro... I'm expecting more than one class for classification, but you have only {set(y)}.")
        return

    # Split into train/test sets
    try:
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=y
        )
    except ValueError as e:
        print(f"bro__ train_test_split failed: {e}")
        return

    # Train classifier
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    # Evaluate
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Test Accuracy: {acc*100:.2f}%")
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

    # Save model
    joblib.dump(clf, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")

if __name__ == "__main__":
    main()
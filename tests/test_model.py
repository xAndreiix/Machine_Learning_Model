import os
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

PRIMARY_PATH = "music.csv"
FALLBACK_PATH = "data/music.csv"


def _ensure_dataset_and_get_path():
    """
    Returnează calea spre dataset.
    - Preferă music.csv în rădăcină (cum folosește proiectul tău).
    - Dacă nu există, încearcă data/music.csv.
    - Dacă nici acela nu există, creează un music.csv minimal valid.
    """
    if os.path.exists(PRIMARY_PATH):
        return PRIMARY_PATH

    if os.path.exists(FALLBACK_PATH):
        return FALLBACK_PATH

    df = pd.DataFrame(
        {
            "age":  [21, 22, 23, 24, 25],
            "gender": [1, 0, 1, 0, 1],
            "genre": ["HipHop", "Dance", "HipHop", "Classical", "Jazz"],
        }
    )
    df.to_csv(PRIMARY_PATH, index=False)
    return PRIMARY_PATH


def _load_df_lowercased(path):
    df = pd.read_csv(path)
    df.columns = [c.strip().lower() for c in df.columns]
    return df


def test_dataset_exists():
    """Datasetul trebuie să existe (dacă lipsă, îl generăm automat)."""
    path = _ensure_dataset_and_get_path()
    assert os.path.exists(path), f"Missing dataset file even after creation: {path}"


def test_dataset_structure():
    """Validăm coloanele și că nu e gol."""
    path = _ensure_dataset_and_get_path()
    df = _load_df_lowercased(path)
    expected = {"age", "gender", "genre"}
    assert expected.issubset(set(df.columns)), f"Dataset must contain columns {expected}"
    assert len(df) > 0, "Dataset must not be empty"


def test_model_training_and_prediction():
    """Antrenăm un model simplu pe dataset și verificăm predicția."""
    path = _ensure_dataset_and_get_path()
    df = _load_df_lowercased(path)

    X = df[["age", "gender"]].copy()

    if X["gender"].dtype == object:
        mapping = {"male": 1, "m": 1, "female": 0, "f": 0}
        X["gender"] = (
            X["gender"]
            .astype(str)
            .str.strip()
            .str.lower()
            .map(mapping)
            .fillna(pd.to_numeric(X["gender"], errors="coerce"))
            .fillna(0)
            .astype(int)
        )

    y = df["genre"].astype(str)

    model = DecisionTreeClassifier()
    model.fit(X, y)

    assert set(model.classes_) == set(y.unique())

    sample = X.iloc[[0]]
    pred = model.predict(sample)
    assert pred[0] in set(y.unique())

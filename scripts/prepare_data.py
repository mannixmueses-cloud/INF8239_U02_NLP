from pathlib import Path

import pandas as pd

RAW = Path("data/raw/SMSSpamCollection")
CSV = Path("data/raw/dataset.csv")
OUT = Path("data/processed/dataset_dedup.csv")

df = pd.read_csv(RAW, sep="\t", header=None, names=["label", "text"], quoting=3)
df.to_csv(CSV, index=False)

dedup = df.drop_duplicates(subset="text", keep="first")
OUT.parent.mkdir(parents=True, exist_ok=True)
dedup.to_csv(OUT, index=False)

print(f"Filas originales: {len(df)}")
print(f"Filas sin duplicados: {len(dedup)} (eliminadas: {len(df) - len(dedup)})")
print(dedup["label"].value_counts(normalize=True))
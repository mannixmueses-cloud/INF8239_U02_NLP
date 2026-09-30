from pathlib import Path

import pandas as pd

SRC = Path("reports/error_analysis.csv")
OUT = Path("reports/error_analysis_categorizado.csv")

# Propuesta inicial, revisada por el estudiante. Mismo orden que SRC (filas 0 a 24).
CATEGORIAS = [
    "lexico_spam_en_mensaje_legitimo",   # 0
    "texto_insuficiente",                # 1
    "spam_promocional_o_concurso",       # 2
    "texto_insuficiente",                # 3
    "spam_contenido_adulto",             # 4
    "spam_que_imita_mensaje_legitimo",   # 5
    "spam_que_imita_mensaje_legitimo",   # 6
    "spam_promocional_o_concurso",       # 7
    "texto_insuficiente",                # 8
    "mensaje_masivo_legitimo",           # 9
    "etiqueta_discutible",               # 10
    "texto_insuficiente",                # 11
    "lexico_spam_en_mensaje_legitimo",   # 12
    "spam_contenido_adulto",             # 13
    "lexico_spam_en_mensaje_legitimo",   # 14
    "lexico_spam_en_mensaje_legitimo",   # 15
    "spam_contenido_adulto",             # 16
    "spam_contenido_adulto",             # 17
    "spam_que_imita_mensaje_legitimo",   # 18
    "spam_que_imita_mensaje_legitimo",   # 19
    "mensaje_masivo_legitimo",           # 20
    "texto_insuficiente",                # 21
    "etiqueta_discutible",               # 22
    "lexico_spam_en_mensaje_legitimo",   # 23
    "mensaje_masivo_legitimo",           # 24
]

df = pd.read_csv(SRC)
if len(df) != len(CATEGORIAS):
    raise SystemExit(f"El CSV tiene {len(df)} filas y hay {len(CATEGORIAS)} categorias.")

df["category"] = CATEGORIAS
df["error"] = df["real"] + "->" + df["predicted"]
df["text"] = df["text"].str.replace(r"\d{5,}", "[numero omitido]", regex=True)
df.to_csv(OUT, index=False)
print(pd.crosstab(df["category"], df["error"], margins=True))
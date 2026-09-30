# INF-8239 · Unidad 02 · Proyecto NLP

Autor académico: Edwin Ramón José Nolasco

Proyecto base para LAB04–LAB06. No sustituya la comprensión por ejecución mecánica.

## Inicio rápido

```bash
uv python install 3.12
uv sync
uv run pytest -q
uv run python scripts/audit_data.py
```

Copie `.env.example` como `.env` y configure el dataset aprobado.

## Dataset

Complete `docs/DATASET_CARD.md`, el diccionario, la licencia y el procedimiento de obtención.
El archivo `data/sample/demo_text.csv` solamente comprueba la arquitectura.

## Entrenamiento

```bash
uv run python scripts/train_text.py
uv run streamlit run app/streamlit_app.py
```

## Interpretación

Toda conclusión debe separar observación, evidencia, interpretación y decisión.

## Corpus utilizado

Este proyecto usa **SMS Spam Collection** (UCI Machine Learning Repository) para clasificar mensajes SMS en inglés como `ham` (legítimo) o `spam`.

- Fuente: https://archive.ics.uci.edu/dataset/228/sms+spam+collection
- DOI: https://doi.org/10.24432/C5CC84
- Licencia: CC BY 4.0 (uso permitido con atribución)
- Cita: Almeida, T. & Hidalgo, J. (2011). SMS Spam Collection [Dataset]. UCI Machine Learning Repository.
- Ficha completa, diccionario y auditoría: `docs/DATASET_CARD.md` y `reports/auditoria_lab04.txt`

Los datos **no se incluyen en el repositorio** (`data/raw/` está excluido con `.gitignore`). Hay que obtenerlos así.

### Cómo obtener el dataset (Windows, PowerShell)

Desde la carpeta del proyecto:

```powershell
Invoke-WebRequest -Uri "https://archive.ics.uci.edu/static/public/228/sms+spam+collection.zip" -OutFile "data\raw\sms.zip"
Expand-Archive -Path "data\raw\sms.zip" -DestinationPath "data\raw"
Remove-Item data\raw\sms.zip
```

En macOS o Linux:

```bash
curl -L -o data/raw/sms.zip "https://archive.ics.uci.edu/static/public/228/sms+spam+collection.zip"
unzip data/raw/sms.zip -d data/raw && rm data/raw/sms.zip
```

Esto deja el archivo original `data/raw/SMSSpamCollection` (una línea por mensaje: clase, tabulador, texto). No se edita.

### Convertir a CSV

El proyecto espera un CSV con columnas `label` y `text`:

```bash
uv run python -c "import pandas as pd; df=pd.read_csv('data/raw/SMSSpamCollection', sep='\t', header=None, names=['label','text'], quoting=3); df.to_csv('data/raw/dataset.csv', index=False); print(df.shape)"
```

Debe imprimir `(5574, 2)`. Si aparece un error de codificación, agregar `encoding='latin-1'` dentro de `read_csv`.

### Configurar y verificar

1. Copiar `.env.example` como `.env` y dejar:
```
   DATA_SOURCE=local
   DATASET_PATH=data/raw/dataset.csv
   TEXT_COLUMN=text
   TARGET_COLUMN=label
```
2. Ejecutar la descarga/verificación, la auditoría y el contrato de datos:
```bash
   uv run python scripts/download_data.py
   uv run python scripts/audit_data.py
   uv run pytest tests/test_data_contract.py -q
```
3. Comparar los hashes SHA-256 con los registrados en `docs/DATASET_CARD.md`:
   - Original `SMSSpamCollection`: `7D039A24A6083ED9EF0F806EBAD56BBB976E3AEB8DE05669173BFDC4996C239D`
   - Convertido `dataset.csv`: `c9ca2be9b60921499e30de05a0350c9bee1ba7cfc98bc03d1547819938a022d0`

   En PowerShell: `Get-FileHash data\raw\SMSSpamCollection -Algorithm SHA256`

### Advertencias

- Algunos mensajes contienen números de teléfono: no publicar ejemplos con números reales.
- El corpus está desbalanceado (13.4 % spam) y tiene 403 copias duplicadas: eliminar duplicados antes de dividir en entrenamiento y prueba.
- `accuracy` sola puede engañar; evaluar con precisión, recall y F1 de la clase `spam`.

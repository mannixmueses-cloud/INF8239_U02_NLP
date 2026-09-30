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


## Reproducir el experimento (LAB04 + LAB05)

1. Obtener el corpus como se explica en "Corpus utilizado" (deja `data/raw/SMSSpamCollection`).
2. Preparar los datos: `uv run python scripts/prepare_data.py`. Crea `data/raw/dataset.csv` y `data/processed/dataset_dedup.csv`, este último sin textos duplicados (5171 filas).
3. En `.env` usar `DATASET_PATH=data/processed/dataset_dedup.csv`. Esta ruta reemplaza a la del apartado anterior.
4. Auditar: `uv run python scripts/audit_data.py` (debe mostrar 0 duplicados).
5. Entrenar y evaluar: `uv run python scripts/train_text.py` (baseline, Complement Naive Bayes y regresión logística, con partición estratificada y semilla 42).
6. Categorizar los errores: `uv run python scripts/categorize_errors.py`. Requiere el paso 5 y guarda `reports/error_analysis_categorizado.csv` con los números de teléfono enmascarados.
7. Pruebas: `uv run pytest -q`.

### Resultados

| Modelo | F1 macro | Recall de spam |
|---|---|---|
| Baseline (DummyClassifier) | 0.466 | 0.00 |
| Complement Naive Bayes | 0.926 | 0.80 |
| Regresión logística | 0.956 | 0.93 |

Limitaciones: un solo corte de entrenamiento y prueba, sin intervalos de confianza; puede haber mensajes casi duplicados entre ambos conjuntos; el corpus solo cubre SMS en inglés de las fuentes indicadas en `docs/DATASET_CARD.md`.

### Conclusión LAB05
En el desarrollo del laboratorio U02.LAB05 se implementó un proceso reproducible de clasificación de texto utilizando el corpus SMS Spam Collection, con el propósito de diferenciar mensajes legítimos (ham) de mensajes no deseados (spam). El trabajo permitió integrar las etapas de preparación y auditoría de los datos, representación mediante TF-IDF, entrenamiento de modelos, evaluación mediante métricas por clase, análisis de errores, almacenamiento del modelo y construcción de una aplicación local para realizar predicciones. Este enfoque permitió comprobar de manera práctica que un problema de Procesamiento de Lenguaje Natural no debe evaluarse únicamente a partir de una métrica global, sino considerando también el comportamiento del modelo frente a cada clase y los tipos de errores producidos.
Como línea base se utilizó un clasificador de referencia, posteriormente comparado con Complement Naive Bayes y Regresión Logística. Los resultados mostraron que la Regresión Logística obtuvo el mejor desempeño general, alcanzando un F1 macro aproximado de 0.956, superior al obtenido por Naive Bayes, con aproximadamente 0.926, y al baseline, que alcanzó alrededor de 0.466. Este resultado evidencia que la combinación de TF-IDF con un modelo lineal constituye una solución adecuada para este corpus, al ofrecer un buen equilibrio entre rendimiento, interpretabilidad, simplicidad computacional y capacidad de reutilización.
Sin embargo, la evaluación también confirmó que un buen valor de F1 macro no elimina completamente los errores. La clase spam representa un desafío especialmente importante, ya que los falsos negativos pueden provocar que determinados mensajes no deseados sean clasificados como legítimos. En un contexto real, este tipo de error puede permitir que contenidos publicitarios, engañosos o no solicitados lleguen al usuario. Por esta razón, se realizó un análisis específico de los casos mal clasificados, superando el mínimo solicitado de veinte observaciones y organizando los errores en categorías interpretables. Este análisis permitió reconocer que factores como textos breves, expresiones ambiguas, vocabulario poco frecuente y similitudes lingüísticas entre mensajes pueden afectar la decisión del clasificador.
La aplicación desarrollada en Streamlit permitió comprobar que el modelo guardado puede reutilizarse fuera del proceso de entrenamiento. Durante la validación local, la aplicación recibió textos nuevos y generó correctamente una clase predicha, mostrando además una advertencia para recordar que la salida debe interpretarse dentro del dominio y de las limitaciones del dataset. Esto es relevante porque una predicción automática no debe presentarse como una verdad absoluta, sino como el resultado de un modelo condicionado por los ejemplos y características disponibles durante su entrenamiento.
Entre las principales limitaciones se encuentran el dominio específico del corpus, su idioma, el contexto temporal de los mensajes y la posibilidad de encontrar expresiones diferentes en datos futuros. Por ello, antes de utilizar el sistema en un entorno real sería necesario validarlo con datos recientes, revisar periódicamente los errores, comprobar posibles cambios en el lenguaje y evaluar nuevamente las métricas por clase. En conclusión, el laboratorio permitió construir un pipeline reproducible y funcional, demostrando que el análisis responsable de los resultados es tan importante como el entrenamiento del modelo.

## Experimento de parámetros Word2Vec - LAB06

Para analizar el efecto del tamaño de la ventana contextual en los embeddings,
se realizaron dos ejecuciones controladas sobre el mismo corpus SMS Spam
Collection, modificando únicamente el parámetro `window` del modelo Word2Vec.

### Experimento A: window = 5

- Palabra evaluada: `free`
- Tamaño del vocabulario: 8713
- Cobertura: 1.0
- Vecinos observados: `nokia`, `messages`, `unlimited`, `reply`, `24hrs`,
  `87131`, `phd`, `svc`, `bluetooth` y `barkleys`.

### Experimento B: window = 2

- Palabra evaluada: `free`
- Tamaño del vocabulario: 8713
- Cobertura: 1.0
- Vecinos observados: `backdoor`, `chik`, `calls`, `1st`, `08000776320`,
  `auction`, `camera`, `inclusive`, `date` y `poly`.

### Interpretación

La modificación del tamaño de la ventana no alteró el tamaño del vocabulario
ni la cobertura del corpus, que permanecieron en 8713 términos y 1.0,
respectivamente. Sin embargo, produjo cambios claros en las palabras
consideradas próximas a `free`.

Con `window=5`, Word2Vec utiliza un contexto más amplio y captura relaciones
de coocurrencia a mayor distancia dentro de los mensajes. Con `window=2`,
el modelo se concentra en términos situados más cerca de la palabra objetivo,
por lo que las relaciones aprendidas cambian.

Este resultado demuestra que la similitud obtenida por un embedding depende
de la configuración del modelo y del contexto disponible en el corpus. Por
tanto, una similitud alta no debe interpretarse automáticamente como
sinonimia ni como equivalencia semántica universal.

Para la configuración final del proyecto se mantuvo `window=5`, dejando
documentado el experimento alternativo con `window=2`.

## Cierre interpretativo LAB06

### Resultado de embeddings
El modelo Word2Vec entrenado sobre el corpus SMS Spam Collection generó un
vocabulario de 8,713 términos y permitió analizar relaciones de proximidad
contextual entre palabras. Para la palabra `free`, la configuración final
con `window=5` produjo vecinos como `nokia`, `messages`, `unlimited`,
`reply`, `24hrs`, `87131`, `phd`, `svc`, `bluetooth` y `barkleys`.
Estos resultados reflejan patrones de coocurrencia propios del corpus y no
deben interpretarse como relaciones semánticas universales.

### Evidencia de cobertura
La cobertura obtenida fue de 1.0, lo que indica que los tokens considerados
durante la evaluación estuvieron representados en el vocabulario aprendido
por el modelo. Además, el experimento comparativo entre `window=5` y
`window=2` mantuvo el mismo vocabulario y cobertura, aunque modificó las
palabras consideradas más cercanas a `free`. Esto evidencia que los
parámetros del modelo afectan la estructura de similitud aprendida.

### Resultado estructural de la red
Para el análisis de redes se utilizó la red de demostración del club de
karate de Zachary, tal como establece la práctica. El procesamiento generó
los archivos `centralities.csv`, `network.png` y
`social_network.graphml`, permitiendo representar los nodos, las aristas,
las comunidades y distintas medidas de centralidad. La red constituye una
demostración reproducible de análisis estructural y no representa
directamente las relaciones existentes en el corpus de mensajes SMS.

### Dos métricas comparadas
Se consideraron especialmente la centralidad de grado y la centralidad de
intermediación. La centralidad de grado permite identificar nodos con una
mayor proporción de conexiones directas, mientras que la intermediación
permite reconocer nodos que aparecen con frecuencia en los caminos mínimos
entre diferentes partes de la red. Estas métricas describen propiedades
estructurales distintas y, por tanto, un nodo puede presentar un valor alto
en una de ellas sin necesariamente ocupar la misma posición en la otra.

### Interpretación permitida
Es válido afirmar que determinados nodos poseen más conexiones directas,
actúan como puentes estructurales o se encuentran en posiciones relevantes
según una métrica específica. También es posible describir las comunidades
detectadas como agrupaciones producidas por el algoritmo sobre la red
analizada.

### Interpretación que NO puede sostenerse
No puede concluirse que un nodo sea la “persona más influyente” únicamente
porque presente mayor centralidad. Tampoco puede interpretarse una comunidad
detectada como una identidad social definitiva ni asumir que la similitud
entre embeddings representa amistad, intención o equivalencia semántica.
Las conclusiones deben limitarse a las propiedades observadas en los datos
y a las métricas utilizadas.

### Siguiente experimento
Como siguiente paso sería conveniente evaluar los embeddings con otras
palabras frecuentes del corpus y comparar nuevas configuraciones de
`window` o `min_count`. También podría analizarse una red real y
debidamente anonimizada, documentando claramente qué representan los nodos,
las aristas, el periodo de observación, la dirección de las relaciones y
las consideraciones de privacidad y consentimiento.
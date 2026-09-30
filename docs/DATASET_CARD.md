# DATASET\_CARD: SMS Spam Collection

## 1\. Procedencia

* Nombre: SMS Spam Collection
* Fuente original: https://archive.ics.uci.edu/dataset/228/sms+spam+collection
* DOI: https://doi.org/10.24432/C5CC84
* Responsables: Almeida, T. y Hidalgo, J. (2011). UCI Machine Learning Repository.
* Fecha de descarga: 29 de septiembre de 2026
* Licencia: CC BY 4.0 (permite descargar, analizar y publicar resultados derivados, con atribución)
* SHA-256 del archivo original (SMSSpamCollection): 7D039A24A6083ED9EF0F806EBAD56BBB976E3AEB8DE05669173BFDC4996C239D
* SHA-256 del archivo convertido (data/raw/dataset.csv): c9ca2be9b60921499e30de05a0350c9bee1ba7cfc98bc03d1547819938a022d0

## 2\. Uso previsto

Clasificar mensajes SMS en inglés como legítimos (ham) o spam, con fines académicos (curso INF-8239, Unidad 02).

## 3\. Diccionario de datos

|Columna|Tipo|Significado|Valores válidos|
|-|-|-|-|
|label|texto|Clase del mensaje (variable objetivo)|ham, spam|
|text|texto|Contenido bruto del mensaje SMS|cualquier texto no vacío|

## 4\. Auditoría (resultado de scripts/audit\_data.py)

* Filas y columnas: 5574 x 2
* Nulos: 0 en text y 0 en label
* Textos duplicados: 403 copias sobrantes (684 filas pertenecen a grupos repetidos: 503 ham y 181 spam); 0 textos con etiqueta contradictoria
* Distribución: ham 86.6 %, spam 13.4 %
* Longitud en caracteres: media 80.5, mediana 62, p90 156, p99 276, máximo 910

## 5\. Ejemplos (anonimizados)

1. ham: "Ok lar... Joking wif u oni..."
2. ham: "U dun say so early hor... U c already then say..."
3. ham: "Nah I don't think he goes to usf, he lives around here though"
4. spam: "Free entry in 2 a wkly comp to win FA Cup final tkts 21st May 2005. \[número omitido]"
5. spam: "Sunshine Quiz Wkly Q! Win a top Sony DVD player if u know which country the Algarve is in? Txt ansr to \[numero omitido]."

## 6\. Transformaciones realizadas

* El original SMSSpamCollection (una línea por mensaje: clase, tabulador, texto) se convirtió con pandas a data/raw/dataset.csv con columnas label y text.
* No se eliminaron duplicados ni se modificó ningún texto. El archivo original no se editó.

## 7\. Sesgos, población no cubierta y usos prohibidos

* Sesgos: los mensajes legítimos provienen en gran parte de un corpus de estudiantes de Singapur y el spam de un foro del Reino Unido; el corpus refleja esos orígenes.
* No cubre: otros idiomas, otros periodos, otras plataformas de mensajería ni spam reciente.
* Riesgo de privacidad: algunos textos contienen números de teléfono. No publicar ejemplos con números reales.
* Usos prohibidos: identificar o contactar a personas a partir de los textos; presentar los resultados como válidos para todo el spam.
* Limitación estadística: el corpus está desbalanceado (13.4 % spam), por lo que accuracy sola puede engañar; usar precisión, recall y F1 de la clase spam.

## 8\. Decisión de aprobación

Aprobado frente a Turkish Spam V01 (826 filas, correos de cuentas personales, menor volumen). Ver docs/dataset\_candidates.csv.

## **9. Cierre interpretativo**

\- Resultado principal: el corpus tiene 5574 mensajes, sin nulos, con 403 copias duplicadas y 13.4 % de spam.

\- Evidencia de calidad y procedencia: hash SHA-256 del original y del CSV convertido, licencia CC BY 4.0, salida de audit\_data.py y 3 pruebas del contrato aprobadas.

\- Riesgo o sesgo identificado: desbalance de clases, origen limitado (Singapur y Reino Unido) y números de teléfono dentro de algunos textos.

\- Decisión de aprobación o rechazo: aprobado; Turkish Spam V01 rechazado por tamaño y riesgo de privacidad.

\- Limitación que debe comunicarse: los resultados aplican a SMS en inglés de estas fuentes y accuracy sola no es una medida confiable.

\- Siguiente verificación: eliminar duplicados antes de dividir los datos en el LAB05 y evaluar con precisión, recall y F1 de spam.


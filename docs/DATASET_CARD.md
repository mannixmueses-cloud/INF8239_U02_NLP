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

\- Resultado principal: revisé el corpus SMS Spam Collection y lo encontré utilizable. Tiene 5574 mensajes en dos columnas (label y text), no tiene datos vacíos y solo el 13.4 % son spam; el resto son mensajes normales. Lo que más me llamó la atención es que hay 403 mensajes repetidos.

\- Evidencia de calidad y procedencia: sé de dónde viene porque guardé el enlace oficial de UCI, el DOI y la licencia CC BY 4.0, que permite usarlo y publicar resultados dando el crédito. Guardé la huella SHA-256 del archivo original y la del CSV convertido, para poder demostrar que no cambió. También corrí la auditoría (audit\_data.py) y las 3 pruebas del contrato de datos, que pasaron.

\- Riesgo o sesgo identificado: los mensajes normales vienen sobre todo de estudiantes de Singapur y el spam de un foro del Reino Unido, así que el corpus no representa a todos los usuarios. Además, algunos mensajes traen números de teléfono, por lo que no debo publicar ejemplos con números reales. Y como hay muchos más mensajes normales que spam, el conjunto está desbalanceado.

\- Decisión de aprobación o rechazo: aprobé SMS Spam Collection porque tiene licencia clara, suficientes mensajes (5574) y una procedencia documentada. Rechacé Turkish Spam V01 porque solo tiene 826 filas y sus correos vienen de cuentas personales, lo que aumenta el riesgo de privacidad.

\- Limitación que debe comunicarse: los resultados solo valen para mensajes SMS en inglés de estas fuentes, no para todo el spam. Además, con tantos mensajes normales, un modelo que dijera siempre "no es spam" acertaría cerca del 87 % sin detectar nada, así que la exactitud (accuracy) sola no es una buena medida.

\- Siguiente verificación: antes de entrenar el modelo en el LAB05, voy a eliminar los mensajes duplicados para que el mismo texto no quede a la vez en entrenamiento y en prueba, porque eso haría que el modelo pareciera mejor de lo que es. También voy a evaluar con precisión, recall y F1 de la clase spam, y no solo con accuracy.


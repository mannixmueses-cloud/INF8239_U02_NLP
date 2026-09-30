\# Declaración de uso de IA · Ejercicio 03



\## Herramienta

Claude (Anthropic), en chat. No se usó ninguna otra herramienta de IA. \[COMPLETAR si usé otra]



\## Para qué la usé

\- Guía paso a paso, sin conocimientos previos, para instalar uv, preparar el proyecto base, usar PowerShell y trabajar con Git y GitHub.

\- Explicación de las salidas de la auditoría, de las métricas y de la matriz de confusión.

\- Propuesta de dos candidatos de corpus (SMS Spam Collection y Turkish Spam V01) y comparación con los criterios del manual.

\- Borradores de: docs/DATASET\_CARD.md, la sección "Corpus utilizado" y la sección "Reproducir el experimento" del README, y docs/conclusion\_lab05.md.

\- Borradores de los scripts scripts/prepare\_data.py y scripts/categorize\_errors.py.

\- Una primera propuesta de categorías para los 25 errores de clasificación.



\## Prompts relevantes

\- "realizar esta práctica paso a paso, detalle a detalle, que no sé nada, debes explicarme lo mejor que se pueda"

\- "busca tus 2 candidatos, compáralos y aprueba, como pide el manual"

\- "dime con palabras como si fuera yo y lo que se entendió" (para el cierre interpretativo del LAB04)

\- "revisa y confirma de que esta bien" (revisión de resultados y de lo publicado en GitHub)



\## Lo que verifiqué yo

\- Ejecuté las pruebas del proyecto (6 passed), las del contrato de datos (3 passed) y tests/test\_text\_model.py (1 passed).

\- Calculé los hashes SHA-256 con Get-FileHash y con el script de auditoría; los comparé con los registrados en la ficha.

\- Comprobé en la página de UCI la licencia, el tamaño y la procedencia de los dos candidatos. \[COMPLETAR: confirmar que abrí los enlaces]

\- Comprobé la matriz de confusión (1117, 13, 12, 151) y calculé recall y precisión de spam a partir de ella.

\- Comprobé que data/raw, .env y los archivos con números de teléfono no están en el repositorio (git ls-files, git grep y Select-String).

\- Revisé en GitHub que el repositorio público muestra los archivos esperados.

\- \[COMPLETAR: si revisé las 25 categorías de error una por una y cuáles cambié]



\## Correcciones que hubo que hacer

\- El enlace de Turkish Spam V01 estaba en el formato antiguo de UCI y falló; se reemplazó por el actual.

\- El quinto ejemplo de spam de la ficha era una frase que no estaba verificada en mi copia del corpus; se reemplazó por un mensaje encontrado con Select-String.

\- La fila de Turkish Spam en dataset\_candidates.csv tenía espacios sobrantes al inicio; se reescribió el archivo.

\- Mi primer repositorio Git quedó creado en mi carpeta de usuario y no en el proyecto; se creó uno nuevo dentro del proyecto y se rehízo el historial.

\- La ficha decía que no se eliminaron duplicados; se corrigió al añadir prepare\_data.py.

\- Un texto que era para el Bloc de notas se ejecutó por error en la terminal (sin efecto sobre los archivos).

\- El reporte de auditoría contenía una ruta personal; se reemplazó antes de publicarlo. \[COMPLETAR: confirmar que lo hice]



\## Lo que no verifiqué o quedó como hipótesis

\- La hipótesis de que el modelo se apoya en palabras sueltas no se comprobó con los coeficientes de la regresión logística.

\- Las categorías de error son una propuesta inicial de la IA \[COMPLETAR: "que revisé" o "que no revisé a fondo"].

\- La comparación entre modelos usa una sola partición, sin intervalos de confianza.

\- \[COMPLETAR: si probé o no la aplicación de Streamlit]


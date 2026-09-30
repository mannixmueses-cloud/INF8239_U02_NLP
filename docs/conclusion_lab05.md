\# Conclusión LAB05 · Clasificación de texto



\*\*Resultado principal.\*\* Con el corpus SMS Spam Collection, después de eliminar 403 textos duplicados (quedaron 5171 mensajes: 87.4 % ham y 12.6 % spam), comparé un baseline y dos clasificadores con la misma partición estratificada (semilla 42) y el vectorizador TF-IDF dentro de cada pipeline. El baseline obtuvo un F1 macro de 0.466: siempre predice "ham", acierta cerca del 87 % y no detecta ningún spam. Complement Naive Bayes obtuvo 0.926 y la regresión logística 0.956.



\*\*Modelo seleccionado y evidencia.\*\* Elegí la regresión logística. En 1293 mensajes de prueba (1130 ham y 163 spam), la matriz de confusión muestra 1117 ham bien clasificados, 13 ham marcados como spam, 12 spam que se escaparon y 151 spam detectados. Eso da un recall de spam de 0.93 y una precisión de spam de 0.92; Naive Bayes tuvo un recall de spam de 0.80. Debo aclarar que la regresión logística usa class\_weight="balanced" y Naive Bayes no, así que parte de la ventaja puede deberse a eso y no solo al tipo de modelo.



\*\*Clase con mayor dificultad.\*\* La clase spam, que es la minoritaria: tiene el menor recall (0.93 frente a 0.99 de ham) y la menor precisión (0.92).



\*\*Tipo de error más frecuente.\*\* Clasifiqué en categorías los 25 errores del conjunto de prueba (con apoyo de una IA para la primera propuesta, que revisé fila por fila). Dos categorías empatan con 5 casos: mensajes legítimos con palabras típicas de spam ("call", "free", "offer") y textos demasiado cortos para decidir. Entre los spam que se escaparon predominan los que imitan un mensaje personal o un aviso (4) y los de contenido para adultos (4). Mi hipótesis, que aún no comprobé, es que el modelo se apoya en palabras sueltas y falla cuando el contexto cambia su sentido.



\*\*Impacto en el contexto.\*\* Los 13 falsos positivos son el 1.2 % de los mensajes legítimos de prueba y los 12 falsos negativos son el 7.4 % del spam. En un filtro real considero más grave perder un mensaje legítimo (entre los errores hay un aviso de seguridad de un banco) que recibir un spam. Por eso no lo usaría para borrar mensajes de forma automática.



\*\*Limitación del dataset.\*\* El corpus contiene SMS en inglés de fuentes concretas (estudiantes de Singapur y un foro del Reino Unido) y de un periodo determinado; no representa otros idiomas ni el spam actual. Además, eliminar textos idénticos no elimina los casi idénticos (por ejemplo, "I'm at work. Please call" y "I'm at home. Please call"), así que puede haber fuga entre entrenamiento y prueba. Usé una sola partición, sin intervalos de confianza, por lo que la diferencia entre 0.926 y 0.956 no es una prueba estadística.



\*\*Decisión antes del despliegue.\*\* No lo desplegaría como filtro automático. Antes haría cuatro verificaciones: repetir el experimento con varias particiones para medir la variación; probar un umbral de decisión que reduzca los falsos positivos o enviar los mensajes dudosos a revisión en lugar de bloquearlos; evaluar con mensajes de otra fuente; y revisar las etiquetas discutibles. La aplicación debe advertir que la etiqueta es una predicción y no una verdad.


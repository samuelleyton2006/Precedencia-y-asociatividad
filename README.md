# TallerPrecedencia-
Este repositorio contiene dos implementaciones de una calculadora con ANTLR4:

- `Original/` → gramática con precedencia y asociatividad **estándar**.  
- `Redisenada/` → gramática con precedencia y asociatividad **modificada**.  

El objetivo es comparar cómo cambian los resultados al modificar la **gramática** del lenguaje.

---

##  Comparación de resultados

| Expresión     | Original | Rediseñada | Diferencia |
|---------------|----------|------------|------------|
| `3 + 4 * 2`   | 11       | 14         | Cambio de precedencia |
| `3 * 4 + 2`   | 14       | 18         | Cambio de precedencia |
| `2 ^ 3 ^ 2`   | 512      | 64         | Cambio de asociatividad |
| `-3 + -5`     | -8       | -8         | Igual |
| `12 / 2`      | 6.0      | 6.0        | Igual |
| `2 * 3`       | 6        | 6          | Igual |
| `(1+2) * 3`   | 9        | 9          | Igual (paréntesis mandan) |
| `4 ^ 2`       | 16       | 64         | Cambio por asociatividad |
| `8 ^ 3`       | 512      | 512        | Igual |
| `5 - 3 - 1`   | 1        | 1          | Igual |

---

##  Conclusiones

1. **La precedencia determina qué operador se evalúa primero.**  
   - En la gramática original, la multiplicación es más fuerte que la suma, como en matemáticas convencionales.  
   - En la gramática rediseñada, la suma/resta se evaluaron antes, alterando los resultados.

2. **La asociatividad determina el orden de evaluación en operadores repetidos.**  
   - Originalmente, la potencia (`^`) se asociaba a la derecha, siguiendo la convención matemática.  
   - En la gramática rediseñada se forzó a la izquierda, lo que cambió drásticamente los resultados.

3. **Los paréntesis siempre tienen mayor prioridad.**  
   - Tanto en la gramática original como en la rediseñada, `( )` permiten forzar el orden de evaluación.

4. **Conclusión principal:**  
   - La gramática no solo define la sintaxis de un lenguaje, sino también su **semántica operativa**.  
   - Un mismo input puede generar resultados diferentes dependiendo de cómo se **defina la precedencia y la asociatividad** en la gramática.  
   - Este ejercicio demuestra la importancia de ser explícitos en el diseño de lenguajes y compiladores.

---

##  Cómo correr el proyecto

1. Instalar dependencias en un entorno virtual:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install antlr4-python3-runtime
   ```
2. Generar los analizadores léxicos/sintácticos:
   ```bash
   cd Original
   antlr4 -Dlanguage=Python3 -visitor Calculadora.g4
   cd ../Redisenada
   antlr4 -Dlanguage=Python3 -visitor CalculadoraAlt.g4
   ```
3. Ejecutar ambas versiones con el mismo archivo de pruebas:
   ```bash
   python3 eval_calculadora.py < pruebas.txt
   python3 eval_calculadora_alt.py < pruebas.txt
   ```

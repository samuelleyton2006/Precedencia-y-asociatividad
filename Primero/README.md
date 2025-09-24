# Calculadora - Gramática Original

Este proyecto implementa una calculadora con **ANTLR4** y **Python** usando la gramática original de operaciones matemáticas.

---

## ¿Cómo funciona?

La gramática implementa las reglas de **precedencia** y **asociatividad** estándar en matemáticas:

1. **Precedencia (prioridad de operadores):**
   - `^` (potencia) → mayor precedencia
   - `*` y `/` → precedencia media
   - `+` y `-` → menor precedencia

   Ejemplo:
3 + 4 * 2
=> 3 + (4 * 2)
=> 11

2. **Asociatividad (orden de aplicación cuando hay empate):**
- `^` → asociativo a la **derecha**  
  ```
  2 ^ 3 ^ 2
  = 2 ^ (3 ^ 2)
  = 2 ^ 9 = 512
  ```
- `+`, `-`, `*`, `/` → asociativos a la **izquierda**  
  ```
  5 - 3 - 1
  = (5 - 3) - 1
  = 1
  ```

---

## Ejecución

1. Generar archivos de ANTLR:
```bash
antlr4 -Dlanguage=Python3 -visitor Calculadora.g4
```
2. Ejecutar
```bash
python eval_calculadora.py < pruebas.txt
```
## Resultados 
<img width="610" height="476" alt="image" src="https://github.com/user-attachments/assets/6bdc8072-7e7e-4495-be56-c6093c836b06" />





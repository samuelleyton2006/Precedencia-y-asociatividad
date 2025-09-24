# Calculadora - Gramática Rediseñada

En esta versión, se modifica la gramática para **alterar la precedencia y la asociatividad** y observar cómo cambia el resultado de las mismas expresiones.

---

## Cambios realizados

1. **Cambio en precedencia:**
   - Ahora `+` y `-` tienen **mayor precedencia** que `*` y `/`.  
   - Esto significa que primero se evalúan sumas/restas antes que multiplicaciones/divisiones.

Ejemplo:

3 + 4 * 2

Original: 3 + (4 * 2) = 11

Rediseñada: (3 + 4) * 2 = 14

---

2. **Cambio en asociatividad del operador `^`:**
- Original: `^` era asociativo a la **derecha**.  
- Rediseñada: `^` es asociativo a la **izquierda**.  


Ejemplo:

2 ^ 3 ^ 2

Original: 2 ^ (3 ^ 2) = 512

Rediseñada: (2 ^ 3) ^ 2 = 64

---

## Ejecución

1. Generar archivos de ANTLR:
```bash
antlr4 -Dlanguage=Python3 -visitor CalculadoraAlt.g4
```
2. Usar el mismo archivo pruebas.txt que en la versión original.
3. Ejecutar
```bash
   python eval_calculadora_alt.py < pruebas.txt

```
## Resultados obtenidos:

<img width="681" height="263" alt="image" src="https://github.com/user-attachments/assets/2a1bd063-8284-4fba-a394-99305b559b8b" />

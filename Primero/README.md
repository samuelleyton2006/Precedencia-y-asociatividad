# Calculadora ANTLR (Gramática Original)

Este proyecto implementa una calculadora con ANTLR4 en Python3 utilizando la gramática **Expr.g4**, la cual respeta la **precedencia y asociatividad estándar** en expresiones aritméticas.

---

## 📌 Precedencia y asociatividad en la versión original
- `^` (potencia): **asociatividad derecha** (right-assoc).
- `*` y `/`: mayor precedencia que `+` y `-`, **asociatividad izquierda** (left-assoc).
- `+` y `-`: menor precedencia, **asociatividad izquierda**.

Ejemplos:
- `1+2*3` → `1+(2*3)=7`
- `10-5-2` → `(10-5)-2=3`
- `2^3^2` → `2^(3^2)=512`

---

## 🚀 cadena de entrada
1. Contenido de prueba y resultado esperado 
   ```bash
   1+2*3     # Original=7
   10-5-2    # Original=3
   4/2+3     # Original=5
   2-3*4     # Original=-10
   2^3^2     # Original=512
   (1+2)*3   # Original=9

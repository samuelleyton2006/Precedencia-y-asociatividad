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

## 🚀 Cómo usar
1. Instalar ANTLR y el runtime para Python:
   ```bash
   pip install antlr4-tools

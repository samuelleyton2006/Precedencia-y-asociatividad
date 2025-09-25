
# Calculadora ANTLR (Gramática Modificada)

Este proyecto implementa una calculadora con ANTLR4 en Python3 utilizando la gramática **ExprModified.g4**, en la cual se cambió la **precedencia y asociatividad** de algunos operadores para observar diferencias.

---

## 📌 Cambios realizados en precedencia y asociatividad
- `^` (potencia): sigue con **asociatividad derecha**.
- `+`: ahora tiene **mayor precedencia** que `*` y `/`.
- `-`: ahora tiene **asociatividad derecha** (right-assoc).

Ejemplos:
- `1+2*3` → `(1+2)*3=9` (cambia respecto al original).
- `10-5-2` → `10-(5-2)=7` (cambia por la nueva asociatividad de `-`).
- `4/2+3` → `4/(2+3)=0.8` (cambia por la precedencia de `+` sobre `/`).

---

## 🚀 Cómo usar
1. Instalar ANTLR y el runtime para Python:
   ```bash
  1+2*3     # Modificado=9
   10-5-2    # Modificado=7
   4/2+3     # Modificado=0.8
   2-3*4     # Modificado=-4
   2^3^2     # Modificado=512
   (1+2)*3   # Modificado=9

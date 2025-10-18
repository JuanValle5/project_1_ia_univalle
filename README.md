# 🐜 Proyecto 1 - Introducción a la Inteligencia Artificial (2025-2)

**Universidad del Valle**  
**Escuela de Ingeniería de Sistemas y Computación**  
**Asignatura:** Introducción a la Inteligencia Artificial  
**Periodo:** 2025-2  

---

## 🧠 Descripción del Proyecto

El proyecto consiste en desarrollar un agente inteligente (una **hormiga**) que debe encontrar un **hongo mágico** dentro de un entorno representado por una matriz.  
Durante su búsqueda, la hormiga puede enfrentarse a **venenos** y obstáculos. El objetivo es que el agente logre llegar al hongo aplicando **técnicas de búsqueda informada**, específicamente:

1. **Beam Search**  
   Una variación de búsqueda informada que limita la cantidad de nodos que se expanden en cada nivel (la “amplitud de la viga” o β).  
   Solo se mantienen los β nodos más prometedores según su función heurística, y los demás se descartan.

2. **Dynamic Weighting Search**  
   Una versión dinámica de *Weighted A\** que ajusta el peso de la heurística en función de la profundidad:  
   \[
   f(n) = g(n) + h(n) + ε \times (1 - \frac{d(n)}{N}) \times h(n)
   \]  
   De esta manera, la búsqueda prioriza moverse rápidamente lejos del inicio y refina su precisión al acercarse al objetivo.

---

## 🧩 Requerimientos del Proyecto

- La **matriz del entorno** debe ser **modificable** en tamaño y posiciones.
- Es **obligatorio** incluir una **interfaz gráfica** que muestre visualmente el movimiento de la hormiga.  
  No se aceptan soluciones únicamente por consola.
- La nota del proyecto es **grupal**, pero la **evaluación es individual** según el dominio demostrado en la sustentación.
- El lenguaje de programación **recomendado** es **Python**, aunque se permite el uso de otros lenguajes.

---

## 🎨 Interfaz Gráfica

La interfaz debe permitir:
- Visualizar el entorno como una cuadrícula.  
- Mostrar gráficamente la hormiga, los venenos y el hongo mágico.  
- Observar en tiempo real el recorrido realizado por la hormiga según el algoritmo seleccionado.

---
```
project_1_ia_univalle/
│
├── src/
│   ├── __init__.py
│   ├── algorithms/
│   │   ├── __init__.py
│   │   ├── beam_search.py
│   │   ├── dynamic_weighting.py
│   │   └── base_search.py
│   │
│   ├── environment/
│   │   ├── __init__.py
│   │   ├── grid.py
│   │   ├── cell.py
│   │   └── entities.py
│   │
│   ├── visualization/
│   │   ├── __init__.py
│   │   ├── game_window.py
│   │   ├── colors.py
│   │   └── animations.py
│   │
│   └── utils/
│       ├── __init__.py
│       ├── heuristics.py
│       └── node.py
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── tests/
│   ├── __init__.py
│   ├── test_beam_search.py
│   ├── test_dynamic_weighting.py
│   └── test_grid.py
│
├── assets/
│   ├── images/
│   │   ├── ant.png (opcional)
│   │   ├── mushroom.png (opcional)
│   │   └── poison.png (opcional)
│   └── fonts/
│       └── arial.ttf (opcional)
│
├── examples/
│   ├── example_1.json
│   ├── example_2.json
│   └── example_3.json
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```
## 🚀 Ejecución

1. Clona el repositorio:  
   ```bash
   git clone https://github.com/<usuario>/project_1_ia_univalle.git
   cd project_1_ia_univalle
   ```
2. Accede al ambiente virtual:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   
3. Instala las dependencias necesarias:  
   ```bash
   pip install -r requirements.txt
   ```

4. Ejecuta el programa:  
   ```bash
   python main.py
   ```
5. (Opcional) Ejecutar pruebas:
   ```bash
   pytest tests/
   ```
   
## 👥 Integrantes

| Nombre Completo                 | Código   | Rol           | Correo Electrónico                         |
|---------------------------------|----------|----------------|-------------------------------------------|
| Juan José Valencia Jimenez      | 2359567  | Líder          | juan.j.valencia@correounivalle.edu.co     |
| Yulieth Tatiana Rengifo Rengifo | 2359748  | Colaboradora   | yulieth.rengifo@correounivalle.edu.co     |
| Pedro José Lopez Quiroz         | 2359423  | Colaborador    | pedro.lopez@correounivalle.edu.co         |

---

## 🧩 Créditos

Este proyecto fue desarrollado como parte de los requerimientos académicos del curso **Introducción a la Inteligencia Artificial** de la **Universidad del Valle**, periodo 2025-2.

# NINE MEN'S MORRYS ESCALADO - PYGAME

Este proyecto fue propuesto para el curso de Inteligencia Artificial del ciclo VII de la carrera de Ingeniería de Sistemas de la Universidad Nacional Mayor de San Marcos.

La finalidad del proyecto era aplicar los conocimientos en inteligencia artificial mediante el lenguaje de programación `Python`.

Se ha decidido implementar el algoritmo Minimax para dotar de "inteligencia" a la máquina. Este enfoque se basa en la capacidad del algoritmo Minimax para tomar decisiones en juegos de estrategia como el nuestro.

Cabe resaltar que este proceso se vio enriquecido gracias al valioso aporte del siguiente paper: [Nine Men's Morris: Evaluation Functions](http://www.dasconference.ro/papers/2008/B7.pdf). Además de apoyarme del siguiente repositorio [nine-mens-morris-python by rajko-z](https://github.com/rajko-z/nine-mens-morris-python)


## Características principales

Este juego es esencialmente similar al Nine Men's Morris original, con una diferencia importante: en esta versión, el molino se forma al alinear de manera consecutiva fichas numeradas del 1 al 3 en línea recta, ya sea en el orden (1, 2, 3) o (3, 2, 1).

## Herramientas utilizadas
- Pygame para realizar la interfaz gráfica.
- Python para la programación del juego.
- Canva para diseñar el juego.

## Requisitos
- Instalar python (+3.12.0)
- Instalar pygame
- Instalar IDE o editor de código

## Intrucciones para su uso
### Desde Terminal
- Clonar el repositorio.
````bash
git clone git@github.com:Fabo2303/nine-mens-morris-python.git
````
- Dirigirse al proyecto en la terminal.
- [Crear el entorno virtual](#crear-entorno-virtual)
- Instalar pygame.
    ````bash
    pip install pygame
    ````
- Ejecutar el proyecto con el siguiente comando.
    ````bash
    py src/main.py
    ````

## Implementación

- [PRONTO]


## Crear entorno virtual
### Creación en Windows
#### Crear el entorno virtual
- Creamos un entorno virtual en la terminal de Windows.
    ```shell
    python -m venv venv
    ```
    Este script de shell generará una carpeta que contendrá los archivos necesarios para el entorno virtual.
#### Activar el entorno virtual
- Luego de crear el entorno virtual tenemos que activarlo.
    ```shell
    venv\Scripts\activate
    ```
    Si se ejecuto correctamente saldrá (venv) al principio de tu línea de comandos.
### Creación en Linux
#### Crear el entorno virtual
- Creamos un entorno virtual en la terminal de Linux.
    ```bash
    python -m venv venv
    ```
    Este script de shell generará una carpeta que contendrá los archivos necesarios para el entorno virtual.
#### Activar el entorno virtual
- Luego de crear el entorno virtual tenemos que activarlo.
    ```bash
    source venv/bin/activate
    ```
    Si se ejecuto correctamente saldrá (venv) al principio de tu línea de comandos.


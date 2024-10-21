# Hardware-Store

Proyecto final del módulo FastAPI del curso "Python+FastAPI"

## Dependencias
- **fastapi:** Dependencia principal del proyecto. Framework de python.
- **uvicorn:** Servidor asincrónico para levantar la aplicación.

## Puesta en marcha
1. Crear un entorno virtual y activarlo
    ```
    `python -m venv env`
             ó
    `python -m venv venv`
   ```
    Si tienes Windows:
    ```
    env\Scripts\activate
    venv\Scripts\activate
    ```
    Si tienes Linux:
    ```
    source env/bin/activate
    source venv/bin/activate
    ```

2. Instalar dependencias del archivo `requirements.txt`

    ```
    pip install -r requirements.txt
    ```

3. Ejecutar con Python el archivo `main.py`
  
    ```
    py | python main.py
    ```
    Si todo está bien, saldrá la siguiente información:
    ```
    INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
    INFO:     Started reloader process [16596] using StatReload
    INFO:     Started server process [10192]
    INFO:     Waiting for application startup.
    INFO:     Application startup complete.
    ```
    Ctrl+Click en __http://127.0.0.1:8000__
    
4. Acceder a la docu interactiva en `/docs` o `/redoc`
    - Agregar `/docs` o `/redoc` después de la URL __http://127.0.0.1:8000__ en el navegador.
    
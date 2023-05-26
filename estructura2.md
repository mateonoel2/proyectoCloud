# Estructura de archivos

```
/proyectoCloud
    /app
            /models
                - model.h5
        - __init__.py
        - routes.py
        - forms.py
        - prediction_service.py
        - utils.py
    /tests
        - test_prediction_service.py
        - test_routes.py
    /migrations
    - .gitignore
    - Dockerfile
    - requirements.txt
    - README.md
    - run.py
    - config.py
    /react
        /templates
            -index.html
            - home.html
            - results.html
        /static
            /css
                - main.css
            /js
                - main.js
            /images
                - logo.png
```

Explicación de la estructura de archivos:

- `app`: Directorio principal de la aplicación Flask.

- `templates`: Archivos HTML de las plantillas Flask.

- `static`: Archivos estáticos como CSS, JavaScript, imágenes y modelos.

- `models`: Modelos de aprendizaje automático en formato .h5 y spark.

- `__init__.py`: Inicializa la aplicación y reúne todas las partes de esta.

- `routes.py`: Definimos las rutas HTTP de la aplicación.

- `forms.py`: Define los formularios de Flask-WTForms.

- `prediction_service.py`: Este es el servicio de predicción que utiliza el modelo de aprendizaje automático para predecir la hora de llegada del autobús.

- `tests`: Este directorio almacena los archivos de pruebas unitarias.

- `migrations`: Este directorio se utiliza para las migraciones de la base de datos.

- `Dockerfile`: Este archivo se utiliza para la crar un Docker image para el despliegue.

- `requirements.txt`: Aquí se enumeran las dependencias de Python que se necesitan para la aplicación.

- `run.py`: Este es el script que se utiliza para iniciar la aplicación.

- `config.py`: Este archivo se utiliza para configurar la aplicación con AWS.
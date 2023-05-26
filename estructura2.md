# Estructura de archivos
```
/proyectoCloud
    /app
        /static
            /models
            - model.h5
        - prediction_service.py

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
        - public
        - src
        - index.html
        - package.json
```

Explicación de la estructura de archivos:

- `app`: Directorio principal de la aplicación Flask.

- `static`: Archivos estáticos como CSS, JavaScript, imágenes y modelos.

- `models`: Modelos de aprendizaje automático en formato .h5 y spark.

- `prediction_service.py`: Este es el servicio de predicción que utiliza el modelo de aprendizaje automático para predecir la hora de llegada del autobús.

- `tests`: Este directorio almacena los archivos de pruebas unitarias.

- `migrations`: Este directorio se utiliza para las migraciones de la base de datos.

- `Dockerfile`: Este archivo se utiliza para la crar un Docker image para el despliegue.

- `requirements.txt`: Aquí se enumeran las dependencias de Python que se necesitan para la aplicación.

- `run.py`: Este es el script que se utiliza para iniciar la aplicación.

- `config.py`: Este archivo se utiliza para configurar la aplicación con AWS.
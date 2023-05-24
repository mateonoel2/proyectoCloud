
```
+---------------------+
|                     |
|     Usuario (UI)    |
|                     |
+----------+----------+
           |
           |
           v
+---------------------+   +--------------------------+
|                     |   |                          |
|    AWS Elastic      |   |         AWS EC2          |
|  Beanstalk (Flask)  |<->| (Machine Learning Model) |
|                     |   |                          |
+----------+----------+   +--------------------------+
           |
           |
           v
+---------------------+
|                     |
|      AWS S3         |
| (static files: css, |
|  js, images, models)|
|                     |
+----------+----------+
           |
           |
           v
+---------------------+
|                     |
|      AWS RDS        |
|  (Database storage) |
|                     |
+---------------------+
```
* Las flechas indican la dirección del flujo de datos y las interacciones entre los componentes.


1. **UI de usuario** 

    La interfaz de usuario con la que los usuarios interactuarán.
    
    El frontend de la aplicación se basará en las plantillas HTML (home.html y results.html) y los archivos CSS y JavaScript almacenados en el bucket de AWS S3. Los usuarios interactuarán con la interfaz web para introducir los datos necesarios para la predicción.

2. **AWS Elastic Beanstalk (Flask)** 
    
    El backend estará basado en Flask y se alojará en AWS Elastic Beanstalk. Este procesará las solicitudes de los usuarios, interactuará con el modelo de machine learning y devolverá los resultados a los usuarios.

    Contará con los siguientes componentes:

    - `routes.py`: Manejará las rutas de la aplicación Flask, es decir, qué acciones deben realizarse cuando se solicita una cierta URL.

    - `forms.py`: Utiliza Flask-WTF para definir los forms que los usuarios necesitan llenar para obtener las predicciones.

    - `prediction_service.py`: Utilizará el modelo de machine learning (model.h5) para hacer las predicciones basándose en los datos introducidos por el usuario.

    - `utils.py`:  Contiene cualquier código de utilidad para apoyar a los otros módulos.

3. **AWS EC2 (Modelo de Aprendizaje Automático)** el servidor donde se ejecuta el modelo de Machine Learning.

4. **AWS S3** es donde se almacenan los archivos estáticos y el modelo de Machine Learning.

5. **AWS RDS** es la base de datos de la aplicación (Puede que exista puede que no). 

    Es posible que también se necesite una base de datos para almacenar la información del usuario, los datos históricos de los autobuses, etc. Se puedes utilizar AWS RDS para este propósito.


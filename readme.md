## Definición de la aplicación
La aplicación será un sistema de predicción de la hora de llegada de los autobuses basado en los modelos guardados en archivos .h5. Proporcionará una plataforma para que los usuarios puedan estimar la hora de llegada de los autobuses, ayudándoles a planificar sus horarios de forma eficaz. Este sistema utilizará algoritmos de aprendizaje automático para procesar y analizar los datos anteriores de horarios de autobuses y otras variables relevantes para predecir la hora con precisión.

## Funcionalidades, características y arquitectura
### Funcionalidades:
1. Entrada del usuario: Los usuarios pueden introducir parámetros como el día de la semana, la parada inicial, la parada final y la hora de salida.
2. Predicción de llegada de autobuses: El sistema predice la hora de llegada del autobús basándose en los parámetros de entrada y los datos anteriores.

### Características:
1. Interfaz fácil de usar: La aplicación proporcionará una interfaz de fácil navegación para que los usuarios introduzcan sus parámetros.
2. Predicciones fiables: Utilizando algoritmos de aprendizaje automático, la aplicación ofrecerá predicciones fiables de la hora de llegada.

### Arquitectura:
La aplicación seguirá una arquitectura de microservicios adecuada para entornos en la nube. Tendrá dos componentes principales: Interfaz de usuario y servicio de predicción.

1. Interfaz de usuario: Manejará las entradas del usuario y mostrará la hora de llegada prevista.
2. Servicio de predicción: Utilizará modelos de ML para predecir los tiempos de llegada de los autobuses.

## Pasos para ejecutar la aplicación

1. **Configuración del entorno local**: Necesitamos Python y las dependencias necesarias instaladas en el entorno de desarrollo local. Se utilizará `pip` para instalar las dependencias requeridas. Se clona el repositorio de GitHub y se navega hasta la carpeta del proyecto.

2. **Configuración de AWS**: Crear una cuenta en AWS si aún no la tienes. Configura tus credenciales de AWS localmente para poder interactuar con los servicios de AWS desde tu entorno de desarrollo.

4. **Configuración de AWS S3**: Crear un bucket en AWS S3 para almacenar los archivos estáticos de la aplicación, como imágenes, CSS y JavaScript. Sube los archivos estáticos al bucket de S3 y configura los permisos adecuados para que puedan ser accedidos públicamente.

5. **Configuración de Flask**: Se necesita tener Flask instalado en el entorno de desarrollo local. Configura la aplicación Flask para que pueda acceder a los servicios de AWS, como S3 y EC2.

6. **Despliegue en AWS Elastic Beanstalk**: Crear una aplicación en AWS Elastic Beanstalk y configura el entorno de ejecución para tu aplicación Flask. Configura las variables de entorno necesarias, como las credenciales de AWS. Despliega tu aplicación en Elastic Beanstalk utilizando un Dockerfile. (El manejo de las instancias de EC2 será manejado automáticamente por Elastic Beanstalk.)

7. **Prueba y validación**: Una vez desplegada la aplicación en Elastic Beanstalk, accede a la URL proporcionada por Elastic Beanstalk para probar tu aplicación en el entorno de producción. EL objetivo es que la aplicación funcione correctamente y se realizaran pruebas para verificar la precisión de las predicciones de llegada de autobuses.

## Aplicando Cloud Computing

Infraestructura como servicio (IaaS): En lugar de tener un servidor físico, se utilizará AWS EC2 para crear máquinas virtuales (instancias) bajo demanda. Esto permitirá escalar fácilmente la aplicación, gestionar un mayor tráfico y tener más control sobre la infraestructura subyacente.

Almacenamiento de objetos: Los proveedores de la nube ofrecen servicios de almacenamiento de objetos escalables y duraderos, utilizaremos AWS S3 para almacenar y servir archivos estáticos (por ejemplo, cargas de usuarios, imágenes, CSS, JavaScript), reduciendo la carga de su servidor Flask y mejorando el rendimiento.

Plataforma como servicio (PaaS): AWS Elastic Beanstalk proporciona un entorno gestionado para desplegar y ejecutar la aplicación Flask. Se encargan de la gestión de la infraestructura, el escalado automático y el equilibrio de carga, lo que le permite centrarse más en el desarrollo de las aplicaciones.

## Ventajas de la computación en nube
### Escalabilidad:
La computación en nube puede gestionar sin esfuerzo el aumento de los datos y las peticiones de los usuarios. Si la base de usuarios crece o el tamaño de los datos aumenta, la computación en nube permite escalar la aplicación para gestionar este crecimiento.

### Almacenamiento y Procesamiento de Datos:
Utilizando bases de datos en la nube y tecnologías de big data, la aplicación puede almacenar, procesar y analizar cantidades masivas de datos sin afectar al rendimiento de la aplicación.

## Repositorio GitHub
El repositorio GitHub de esta aplicación se encuentra en: https://github.com/mateonoel2/proyectoCloud Contiene todo el código, las dependencias y las instrucciones necesarias para ejecutar la aplicación.
# IOT proyecto

Se basa en simular los reportes de temperatura de un dispositivo y de estos mismos dar un reporte para analizar el comportamiento que puede generar un dispositivo

### Instalacion 💻

Antes de empezar el proyecto es necesario que tenga los siguientes programas:
```
Docker  20.10
Python 3.9
```

Para comenzar el proyecto ejecutar los siguientes comandos
``` bash
docker compose  up --build
```
Despues de que los contenedores estan corriendo ejecutar
```
./scripts/init-rabbitmq.sh
```
Y por ultimo se debe correr un script para simular un dispositivo IOT
```
pip install paho-mqtt==1.5.1
python3 pub/pub.py
```
## Construido con

- Flask - python
- RabbitMQ
- Docker

### Se usan las siguientes librerias

- [ ] paho-mqtt
- [ ] Sqlalchemy
- [ ] uvicorn
- [ ] flask
- [ ] matlibplot
- [ ] pandas

---
### sobre el proyecto ⚒
La arquitectura que se usa en el proyecto es la siguiente
![](https://i.imgur.com/DlyHDF9.png)

Se usa el protocolo MQTT por su sencillez, ligereza. Además siempre va a haber comunicación M2M. Para el desarrollo del back-end donde se consumirán todos los datos y se generara el reporte será Flask.

Se usa Flask por su rendimiento, y la fácil creación de los servicios.


### Project structure
Files related to application are in the app or tests directories. Application parts are:

```
app
├── main             - Donde estan los src de la Api Rest
├── pub              - Donde esta el script que simula un dispositivo iot
├── scripts          - Estan la mayoria de configuracion para setear he iniciar la api rest
```

### relaciones a partir de tablas de Postgresql 🧾
El grafico para guardar los datos generados por los sensores es:

![](https://i.imgur.com/NJZ8mKS.png)


### Documentacion del servicio API-REST
Para la documentación se puede ir al siguiente enlace

Si este enlace no se encuentra en funcionamiento puede ejecutar el proyecto y mirar toda la documentación en:

### End-points

GET /statistics
Aca pueden ver en tiempo real los datos generados por el dispositivo
![](https://i.imgur.com/bgLfJjY.png)

POST /api/csv

Genera un csv donde lo guarda local


POST /api/analisis
Genera una imagen que demuestra el reporte final de todo el tiempo que se ah tomado registro al dispositivo
![](https://i.imgur.com/1d635oH.png)


GET /api/reportes
Retorna un JSON donde traera toda la inforamcion final generada por el dispositivo


### Testing
Se utiliza github actions para CI/CD
Proceso...

### Mejoras
- [ ] usar TLS
- [ ] Mejorar la estructura para anadir medidores dinamicos
- [ ] Implementar security para la api
- [ ] Migrarlo a Fast api para asincronia
- [ ] Mejorar el scheama
- [ ] Documentacion con swagger
- [ ] Manejar los errores
- [ ] Crear y manejar variables de entorno
- [ ] Mejorar los scripts
- [ ] Hacer test
- [ ] Borrar dependencias que no se usan

### Autor
Twitter: [Andres reyes](https://twitter.com/andres_vanml)


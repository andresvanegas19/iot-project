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
docker compose up
```

## Construido con

- Flask - python
- RabbitMQ
- Docker

### Se usan las siguientes librerias

- [ ] paho-mqtt
- [ ] Sqlalchemy
- [ ] uvicorn
- [ ] fastapi

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


### Testing
Para el desarrollo de este proyecto se utiliza varios tipos de testing, aparte de esto se tiene CI para la integración del proyecto y que este tenga un buen funcionamiento

### Mejoras
- [ ] usar TLS
- [ ] Mejorar la estructura para anadir medidores dinamicos
- [ ] Implementar security para la api
- [ ] Migrarlo a Fast api para sincronia
- [ ] Mejorar el scheama
- [ ] Documentacion con swagger
- [ ] Manejar los errores


### Autor
Twitter: [Andres reyes](https://twitter.com/andres_vanml)

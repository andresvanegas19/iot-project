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

Ejecutando este comando van a correr 3 contenedores que seran un simulador IOT, un broker que esta en rabbitmq y un API Rest que esta sobre fastApi


## Construido con

- FastApi - python
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

![](https://i.imgur.com/Jq4uxR4.png)

Se usa el protocolo MQTT por su sencillez, ligereza. Además siempre va a haber comunicación M2M. Para el desarrollo del back-end donde se consumirán todos los datos y se generara el reporte será FastAPI.

Se usa FastAPI por su rendimiento, y la fácil creación de los servicios.

### relaciones a partir de tablas de Postgresql 🧾
El grafico para guardar los datos generados por los sensores es:

![](https://i.imgur.com/aKNNFi9.png)


### Documentacion del servicio API-REST
Para la documentación se puede ir al siguiente enlace

Si este enlace no se encuentra en funcionamiento puede ejecutar el proyecto y mirar toda la documentación en:

Para mas documentacion sobre los endpoints dirijete a ->  http://127.0.0.1/redoc

### Testing
Para el desarrollo de este proyecto se utiliza varios tipos de testing, aparte de esto se tiene CI para la integración del proyecto y que este tenga un buen funcionamiento


### Autor

Twitter: [Andres reyes](https://twitter.com/andres_vanml)

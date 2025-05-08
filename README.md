
## FastAPI + PostgreSQL + Redis + NGINX (Dockerized)

 
### Architecture


+-------------+     +-------------+     +-----------+
|  NGINX      | --> |  FastAPI    | --> |  PostgreSQL
|  (Reverse   |     |  Backend    | --> |  Redis     |
|  Proxy)     |     |  API        |     |  Cache     |
+-------------+     +-------------+     +-----------+


### Usage
bash
docker-compose up --build


### Security Scan
To scan your Docker images:
bash
trivy image fastapi_app
# or using Docker Scout
docker scout quickview fastapi_app

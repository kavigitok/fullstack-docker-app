## Production-like Upgrade

This project uses Nginx as a reverse proxy in front of a Gunicorn-powered Flask backend. The backend connects to MySQL over the internal Docker Compose network.

### Request Flow

Browser / curl → Nginx Reverse Proxy → Gunicorn Flask Backend → MySQL Database

### Health Endpoints

- `/health` checks whether the backend application is alive.
- `/ready` checks whether the backend can connect to the MySQL database.
- `/db` validates backend-to-database connectivity.

### Deployment-style Compose

`docker-compose.deploy.yml` runs the backend using the published Docker Hub image instead of building from local source code.

```bash
docker compose -f docker-compose.deploy.yml up -d

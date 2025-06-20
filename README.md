# ERP Main

This repository contains a monolithic Django project that powers a small ERP system.  It includes a collection of apps such as CRM, HRMS, Inventory and more.  Two apps of interest here are **ITOM** (IT Operations Management) and **ITSM** (Incident Management).

The project is configured for **Python&nbsp;3.13** and uses **Django REST Framework**.  Docker is used to provide PostgreSQL, Redis and a Zabbix stack for monitoring.

## Requirements

* Python 3.13
* [uv](https://docs.astral.sh/uv/) for dependency management
* Docker with Compose v2

## Quick Start

Clone the repository and install the dependencies with `uv`:

```bash
git clone https://github.com/saurav-dhait/erp_main.git
cd erp_main
uv sync
```

Create a `.env` file from the provided template and start the containers:

```bash
cp .env.example .env
docker compose up -d
```

Apply migrations and run the development server:

```bash
uv run manage.py migrate
uv run manage.py runserver
```

The API will be available at `http://localhost:8000/`.

### Running Tests

Run Django's test suite with:

```bash
uv run manage.py test
```

### Services

The `docker-compose.yaml` file starts the following containers:

* **db** – PostgreSQL for the Django backend
* **redis** – Redis cache
* **zabbix-db**, **zabbix-server**, **zabbix-web** – Zabbix monitoring stack

Environment variables for these services are defined in `.env.example`.

## ITOM and Zabbix

The `itom` app exposes API endpoints for managing Hosts and Services.  It also contains a minimal Zabbix API client used to create hosts in Zabbix and to fetch summary data for the dashboard.

```
GET  /api/itom/dashboard/           # summary from Zabbix
GET  /api/itom/hosts/               # list hosts
POST /api/itom/hosts/               # create host (also adds to Zabbix)
```

## ITSM Webhook

The `itsm` app provides an endpoint that Zabbix can call whenever a problem is raised.  Each call creates an `Incident` object in the local database.

```
POST /api/itsm/zabbix/
```

All incidents can be managed through the `/api/itsm/incidents/` endpoints.

## Project Layout

```
erp_main/       # Django project root
├── itom/       # IT Operations Management app
├── itsm/       # Incident Management app
├── crm/        # Other business apps...
└── manage.py
```

Migrations for new apps are stored in their respective `migrations/` directories.  Additional configuration is found in `erp_main/erp_main/settings.py`.

## Contributing

1. Create your virtual environment with `uv sync`.
2. Start the services with `docker compose up -d`.
3. Create a new branch for your feature (note: this repo uses a single `work` branch for demonstration).
4. Submit a pull request with clear commit messages.

---

This README is focused on developer setup.  Refer to the source code for further details on how each module works.


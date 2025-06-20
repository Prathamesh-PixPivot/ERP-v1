# ERP MAIN

## Before you begin
You should install uv (by astral) to manage packages and dependencies.

Follow this link https://docs.astral.sh/uv/#installation .


## How to Run

```bash
# Clone the repository
git clone https://github.com/saurav-dhait/erp_main.git

# Install requirements via uv (make sure you are in same directory as pyproject.toml) 
uv sync

# activate the .venv that was created by uv (for windows powershell)
.\.venv\Scripts\Activate.ps1

# Run the docker-compose
docker compose up 

# Change the directory 
cd erp_main

# Migrate
uv run manage.py migrate

# Run the server
uv run manage.py runserver
```
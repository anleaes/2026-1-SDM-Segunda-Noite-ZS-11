# Gestão de Contratos - Backend Django/DRF

Projeto base para a A3 de Sistemas Distribuídos e Mobile.

## Rodar localmente

```bash
conda env create -f environment.yml
conda activate gestao-contratos
copy .env.example .env
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Ajuste o arquivo `.env` com os dados do Oracle OCI antes de rodar migrations.

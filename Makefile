MANAGE = .venv/bin/python product_catalog/manage.py

install:
	python -m venv .venv
	.venv/bin/pip install -r requirements.txt

migrate:
	$(MANAGE) migrate

setup: migrate
	$(MANAGE) seed

up:
	$(MANAGE) runserver

test:
	$(MANAGE) test product

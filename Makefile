MANAGE = .venv/bin/python product_catalog/manage.py

install:
	python -m venv .venv
	.venv/bin/pip install -r requirements.txt

migrate:
	$(MANAGE) migrate

seed:
	$(MANAGE) seed

up:
	$(MANAGE) runserver

test:
	$(MANAGE) test product

manage:
	$(MANAGE) $(cmd)

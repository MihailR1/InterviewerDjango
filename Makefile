ifneq (,$(wildcard .env))
$(info Found .env file.)
include .env
export
endif

export PYTHONPATH := $(shell pwd):$(PYTHONPATH)

style:
	flake8 .
types:
	mypy .
tests:
	pytest --lf --v
isort:
	isort apps config
black:
	black apps config  --skip-magic-trailing-comma
pre-check:
	pre-commit run --all-files
check:
	make -j3 style types tests
format:
	make -j3 isort black

migrations:
	python manage.py makemigrations
migrate:
	python manage.py migrate

shell:
	python manage.py shell_plus --print-sql
reset_db:
	python manage.py reset_db
startapp:
	python manage.py startapp

up:
	docker-compose up
down:
	docker-compose down

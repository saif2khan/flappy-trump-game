default:
	@make run

run:
	python3 main.py

web:
	python3 -m pygbag main.py

web-build:
	python3 -m pip install --user pygbag
	python3 -m pip install --user pygame
	python3 -m pygbag --build main.py

init:
	@pip3 install -U pip; \
	pip3 install -e ".[dev]"; \
	python3 -m pre_commit install || true; \

pre-commit:
	pre-commit install

pre-commit-all:
	pre-commit run --all-files

format:
	black .

lint:
	flake8 --config=../.flake8 --output-file=./coverage/flake8-report --format=default

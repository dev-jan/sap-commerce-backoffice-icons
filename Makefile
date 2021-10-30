init:
	poetry install

check:
	poetry run flake8 . --show-source --exclude venv

.PHONY: init check

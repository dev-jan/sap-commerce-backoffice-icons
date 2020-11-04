init:
	pip install -r requirements.txt

check:
	flake8 --show-source

.PHONY: init check

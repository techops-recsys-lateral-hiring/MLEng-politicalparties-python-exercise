SHELL := /bin/bash
PYTHON := /opt/homebrew/bin/python3 # TODO: add your python path
VENV_DIR := .venv
ACTIVATE_VENV := source $(VENV_DIR)/bin/activate

install: venv

venv: $(VENV_DIR)/bin/activate

$(VENV_DIR)/bin/activate: requirements.txt
	test -d $(VENV_DIR) || $(PYTHON) -m venv $(VENV_DIR)
	$(ACTIVATE_VENV); pip install -Ur requirements.txt
	touch $(VENV_DIR)/bin/activate

test:
	pytest tests

run:
	docker compose -f compose.yml up

clean:
	docker compose -f compose.yml down
	rm -rf $(VENV_DIR)
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
	rm -rf .pytest_cache
	rm -rf data/models/*

.PHONY: all venv clean test install run

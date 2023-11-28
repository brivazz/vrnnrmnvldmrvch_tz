.PHONY: env install-hooks update-hooks remove-hooks pre-commit check start stop

env:
	pip install -r requirements.txt

install-hooks:
	pre-commit install

update-hooks:
	pre-commit autoupdate

remove-hooks:
	pre-commit uninstall

# pre-commit: update-hooks install-hooks
pre-commit: install-hooks
	pre-commit run --show-diff-on-failure --color=always --all-files

check: pre-commit

start:
	docker-compose up --build -d

stop:
	docker-compose down -v

lint:
	flake8 \
		--per-file-ignores="__init__.py:F401" \
		src/python_typing

test:
	poetry run pytest

doc_check:
	pydocstyle src/python_typing

type_check:
	mypy \
		--disallow-any-generics \
		--disallow-untyped-defs \
		--warn-unused-ignores \
		--warn-redundant-casts \
		--warn-unreachable \
		--pretty \
		--soft-error-limit 10 \
		src/python_typing

checks: lint test doc_check type_check

dev_setup:
	poetry install
	poetry shell

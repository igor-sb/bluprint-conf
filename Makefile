UV_RUN := uv run
FOLDERS= bluprint_conf
PROJ= bluprint_conf
NC=\033[0m # No Color

.PHONY: install autolint lint lint-flake8 shell precommit uv-precommit \
		install-dev test report-coverage docs lint-mypy

test:
		${UV_RUN} coverage erase
		${UV_RUN} coverage run --branch -m pytest tests ${PROJ} \
				--junitxml=junit/test-results.xml -v

install: install-dev
		uv sync

lint:
		make autolint
		make lint-flake8
		make lint-mypy

install-dev:
		cp tools/pre-commit .git/hooks
		chmod +x .git/hooks/pre-commit

autolint:
		@${UV_RUN} autopep8 -r -i ${FOLDERS}
		@${UV_RUN} unify -r -i ${FOLDERS}
		@${UV_RUN} isort ${FOLDERS}

lint-flake8:
		@echo "\n${BLUE}Running flake8...${NC}\n"
		@${UV_RUN} flake8 .

lint-mypy:
		@echo "\n${BLUE}Running mypy...${NC}\n"
		${UV_RUN} mypy --show-error-codes ${PROJ}

precommit: uv-precommit lint

uv-precommit:
		${UV_RUN} pre-commit run --all-files

report-coverage:
		${UV_RUN} coverage report
		${UV_RUN} coverage html
		${UV_RUN} coverage xml

docs:
	@echo "\n${BLUE}Preparing Sphinx documentation...${NC}\n"
	@cd docs; make html; make prepare-gh-pages

clean-docs:
	@cd docs; rm -rf build; rm -rf html
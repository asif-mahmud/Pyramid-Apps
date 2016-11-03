#!/bin/bash
# Yet to be implemented
PROJECT_NAME=pethouse
PROJECT_PATH=/home/shimon/Workspace/Git/Pyramid-Apps/pethouse
VENV_PATH=/home/shimon/Workspace/venv


setup:
	cd ${PROJECT_PATH}
	${VENV_PATH}/bin/pip install -e .
	cd ${PROJECT_PATH}/${PROJECT_NAME}/ngsrc && npm install
	cd ${PROJECT_PATH}/${PROJECT_NAME}/ngsrc/semantic && gulp build

tsc:
	cd ${PROJECT_PATH}/${PROJECT_NAME}/ngsrc
	npm run tsc

tscw:
	cd ${PROJECT_PATH}/${PROJECT_NAME}/ngsrc
	npm run tscw

revision:
	@read -p "What did you add? " MSG && \
	cd ${PROJECT_PATH} &&\
	${VENV_PATH}/bin/alembic revision --autogenerate -m "$$MSG"

upgrade:
	cd ${PROJECT_PATH}
	${VENV_PATH}/bin/alembic upgrade head

downgrade:
	cd ${PROJECT_PATH}
	${VENV_PATH}/bin/alembic downgrade -1

run:
	cd ${PROJECT_PATH}
	${VENV_PATH}/bin/pserve development.ini

#python 3.13버전에서 실행
FROM python:3.13

#poetry 설치
RUN pip install -U poetry

#실행하는 폴더를 code로 설정
WORKDIR /code

#poetry.lock과 pyproject.toml 파일을 code폴더 내로 복사
COPY poetry.lock pyproject.toml /code/

#가상환경 설치를 프로젝트 내에서 하지 않음/ --no-rot:  의존성 따지면서 설치/ --no-interaction: 따로 상호작용 question안함
RUN poetry config virtualenvs.create false \
 && poetry install --no-root --no-interaction

#setuptools: setup.py 기반의 라이브러리
#wheel: 바이너리 배포 형식을 다루는 라이브러리
#--upgrade: 설치된 라이브러리가 있을 때, 버전이 낮으면 업그레이드 하겠다
RUN pip install --upgrade setuptools wheel

#app폴더를 code/app으로 복사한 후, app폴더를 작업 폴더로 설정
COPY ./app /code/app
WORKDIR /code/app

#python 환경변수 설정
ENV PYTHONPATH="${PYTHONPATH}:/code"

#poetry run으로 서버 실행
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
FROM python:3
EXPOSE 8000

RUN git clone -b feat/sanic-solo-project https://github.com/dansobolev/NapoleonIT_project.git
RUN ls /NapleontIT_project
RUN pip install --no-cache-dir -r /NapoleonIT_project/requirements.txt
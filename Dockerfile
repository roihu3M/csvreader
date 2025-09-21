FROM python
WORKDIR /usr/src/app
ENV PYTHONUNBUFFERED=1
COPY requirements.txt ./
RUN pip install -r requirements.txt
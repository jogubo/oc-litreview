FROM debian:bullseye-slim AS litreview

WORKDIR /usr/src/app

ADD . ./

RUN apt update && apt upgrade -y && apt install -y python3 python3-pip \
    && pip3 install -r requirements.txt \
    && apt remove -y python3-pip \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 8000

ENTRYPOINT ["python3", "src/manage.py"]

CMD ["runserver", "0.0.0.0:8000"]

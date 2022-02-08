FROM archlinux

WORKDIR /usr/src/app

RUN pacman -Syu --noconfirm python python-pip && pacman -Scc --noconfirm

ADD . ./

RUN pip install -r requirements.txt


EXPOSE 8000

ENTRYPOINT ["python", "src/manage.py"]

CMD ["runserver", "0.0.0.0:8000"]

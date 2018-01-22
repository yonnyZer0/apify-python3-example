FROM python:3
COPY ./* ./
CMD [ "python3", "example.py" ]

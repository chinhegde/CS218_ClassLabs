FROM python
WORKDIR /app
COPY . /app
RUN pip install bottle
CMD ["python3","app.py"]
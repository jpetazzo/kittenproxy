FROM python:alpine
RUN pip install flask pyyaml
COPY app.py .
COPY sample-config.yaml .
ENV KITTEN_CONFIG=sample-config.yaml
CMD exec flask run --host 0.0.0.0
EXPOSE 5000

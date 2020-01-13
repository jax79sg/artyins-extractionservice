FROM openjdk:slim
COPY --from=python:3.6-slim / /
ENV TIKA_SERVER_JAR /tmp/tika-server.jar
RUN apt update && \
    apt install -y git build-essential axel 
RUN git clone https://github.com/jax79sg/artyins-extractionservice
RUN cd artyins-extractionservice && \
    ./setup_prerequisites.sh
EXPOSE 9891
WORKDIR artyins-extractionservice
ENTRYPOINT ["gunicorn","--bind","0.0.0.0:9891","--workers","1","wsgi:app"]


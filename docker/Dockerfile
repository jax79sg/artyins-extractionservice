FROM openjdk:slim
COPY --from=python:3.6-slim / /
ENV TIKA_SERVER_JAR /tmp/tika-server.jar
RUN apt update && \
    apt install -y git build-essential wget 
RUN git clone https://github.com/jax79sg/artyins-extractionservice
RUN cd artyins-extractionservice && \
    ./setup_prerequisites.sh
COPY tika-server.jar /tmp/tika-server.jar
COPY tika-server.jar.md5 /tmp/tika-server.jar.md5
EXPOSE 9891
RUN mkdir /logs && \
    mkdir /shareddata
WORKDIR artyins-extractionservice
ENTRYPOINT ["gunicorn","--bind","0.0.0.0:9891","--workers","10","-c","docker-gunicorn.conf.py","wsgi:app"]


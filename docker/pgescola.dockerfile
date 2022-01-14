FROM postgres:13.1-alpine
LABEL maintainer "Vinicius de Oliveira"
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=root12345
ENV POSTGRES_DB=escola
EXPOSE 5432
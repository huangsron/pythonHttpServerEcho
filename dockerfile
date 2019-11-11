FROM python:3.8.0-alpine3.10


RUN mkdir -p /code

COPY entrypoint.py /code/entrypoint.py

# Define working directory.
WORKDIR /code

# Define default command.
#CMD ["nginx", "-g", "daemon off;"]
#ENTRYPOINT ["/code/entrypoint.py"]
CMD ["/code/entrypoint.py"]

# Expose ports.
EXPOSE 8000

# base image
FROM python:3.12-slim

# setup working directory in container
WORKDIR /inventory_management_system

# copy all files to inventory_management_system directory
COPY . /inventory_management_system/

# command to run on container start
CMD ["python", "inventory_management_system/main.py"]
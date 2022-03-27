FROM python:3.6.9-slim-buster

WORKDIR /root

# Variable necessary for making python print commands while running program. Otherwise it will print all outputs only
# after program execution. And in case of program hanging, it will never print outputs
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .

# Install python libs in a specific folder that will be copied on next docker build stage named base
RUN apt-get update -y \
    && apt-get install -y --no-install-recommends

RUN pip install --no-cache-dir -r requirements.txt

COPY ./* ./

ADD data ./data

# Uses entrypoint.sh as entrypoint providing by default the argument "server.
ENTRYPOINT [ "./entrypoint.sh" ]
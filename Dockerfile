FROM nvidia/cuda:12.1.0-runtime-ubuntu20.04

# install utilities
RUN apt-get update && \
    apt-get install --no-install-recommends -y curl

RUN apt-get install -y python3.8 python3.8-dev python3.8-distutils python3.8-venv python3-pip git

RUN /bin/bash -c alias python=/usr/bin/python3.8
RUN /bin/bash -c echo 'alias python=python3.8' >> ~/.bashrc
RUN echo -e '#!/bin/bash\npython3=/usr/bin/python3.8' > ~/.bashrc && chmod +x ~/.bashrc
RUN python3 -V

# Installing python dependencies
RUN python3 -m pip --no-cache-dir install --upgrade pip && python3 --version && pip3 --version


COPY ./ /onemt/
WORKDIR /onemt/
ENV PYTHONPATH=/onemt
RUN ls -lah /onemt/*
RUN pip3 --timeout=300 --no-cache-dir install -r requirements.txt

RUN chmod +x /onemt/install_server.sh
RUN chmod +x /onemt/start.sh

RUN bash /onemt/install_server.sh

EXPOSE 8084
CMD ["/onemt/start.sh"]

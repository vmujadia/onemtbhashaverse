#!/bin/bash
gunicorn -w ${WORKERS:=2} \
  -b :8084 -t ${TIMEOUT:=300} \
  -k uvicorn.workers.UvicornWorker \
  run_server:app

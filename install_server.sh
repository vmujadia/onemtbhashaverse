#!/bin/bash


pip3 install --upgrade pip==24.0.0

pip3 install -r requirements.txt

git clone https://github.com/pytorch/fairseq
cd fairseq
python3 -m pip install .

cd ..


mkdir models
python3 downloadmodels.py

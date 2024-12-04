# onemtbhashaverse
onemtbhashaverse



### LOCAL INSTALL

bash install_server.sh

### LOCAL START

sh start.sh

### Docker Build

bash docker_build.sh 

### Docker Run

bash docker_run.sh 

### Docker check

docker container ls

### Docker Stop/Delete Container

docker rm -f <container-id>




## API URL 

http://0.0.0.0:8084/onemtapi/v1/translateulca

### Input (ULCA)
```
{
    "input": [
        {
            "source": "नमस्ते"
        }
    ],
    "config": {
        "modelId":101,
        "language": {
            "sourceLanguage": "hin",
            "targetLanguage": "eng"
            }
    }
}
```
### Output (ULCA)
```
{
    "output": [
        {
            "source": "नमस्ते",
            "target": "Hi."
        }
    ],
    "config": {
        "modelId": 101,
        "language": {
            "sourceLanguage": "hin",
            "targetLanguage": "eng"
        }
    }
}
```
# Training Code
- https://ssmt.iiit.ac.in/meitygit/ssmt/mt-model-deploy-dhruva/-/tree/master/training-code

# Corpora
- https://ssmt.iiit.ac.in/meitygit/palash/himangy-corpora


### supported language pairs



## Citation
```
```

# onemtbhashaverse
onemtbhashaverse

# Supports

- Translation Across 36 × 36 Indian Language Pairs
- Discourse Translation
- Domain-Specific Translation
- Machine Translation Evaluation
- Translation Error Identification and Categorization
- Automatic Post-Editing (APE)


# Cite

```
@misc{mujadia2024bhashaversetranslationecosystem,
      title={BhashaVerse : Translation Ecosystem for Indian Subcontinent Languages}, 
      author={Vandan Mujadia and Dipti Misra Sharma},
      year={2024},
      eprint={2412.04351},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2412.04351}, 
}
```

# How to Run

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
- https://huggingface.co/datasets/ltrciiith/bhashik-parallel-corpora-generic 

### supported language pairs
- 36*36




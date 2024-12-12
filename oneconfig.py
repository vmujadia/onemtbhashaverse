import os
import torch

GLOBAL_CONFIG = {
            "USE_CUDE_IF_AVAILABLE": True,
            "ROUND_DIGIT": 6
        }


URL_SPM_MODEL="https://vandanresearch.sgp1.digitaloceanspaces.com/bhashaverse/IL2ILEN_June7_2024.model"
URL_ONEMT_MODEL="https://vandanresearch.sgp1.digitaloceanspaces.com/bhashaverse/onemtv3b.pt"
URL_SDIC="https://vandanresearch.sgp1.digitaloceanspaces.com/bhashaverse/dict.SRC.txt"
URL_TDIC="https://vandanresearch.sgp1.digitaloceanspaces.com/bhashaverse/dict.TGT.txt"

SUBWORD_MODEL_PATH="models/IL2ILEN_June7_2024.model"
TRANSLATION_MODEL_FOLDER="models/"
TRANSLATION_MODEL_PATH="models/onemtv3b.pt"

language_mapping = {
    "asm": "asm_Beng",
    "ben": "ben_Beng",
    "ban": "ben_Beng",
    "brx": "brx_Deva",
    "doi": "doi_Deva",
    "gom": "gom_Deva",
    "guj": "guj_Gujr",
    "hin": "hin_Deva",
    "kan": "kan_Knda",
    "kas_arab": "kas_Arab",
    "kas": "kas_Arab",
    "kas_deva": "kas_Deva",
    "mai": "mai_Deva",
    "mal": "mal_Mlym",
    "mar": "mar_Deva",
    "mni_beng": "mni_Beng",
    "mni": "mni_Beng",
    "mni_mtei": "mni_Mtei",
    "npi": "npi_Deva",
    "ory": "ory_Orya",
    "ori": "ory_Orya",
    "odi": "ory_Orya",
    "pan": "pan_Guru",
    "pun": "pan_Guru",
    "san": "san_Deva",
    "sat": "sat_Olck",
    "snd_arab": "snd_Arab",
    "snd_deva": "snd_Deva",
    "snd": "snd_Arab",
    "tam": "tam_Taml",
    "tel": "tel_Telu",
    "urd_arab": "urd_Arab",
    "urd": "urd_Arab",
    "eng": "eng_Latn"
}

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Environment specific config, or overwrite of GLOBAL_CONFIG
ENV_CONFIG = {
    "development": {
        "DEBUG": True
    },

    "staging": {
        "DEBUG": True
    },

    "production": {
        "DEBUG": False,
        "ROUND_DIGIT": 3
    }
}


def get_config() -> dict:
    """
    Get config based on running environment

    :return: dict of config
    """

    # Determine running environment
    ENV = os.environ['PYTHON_ENV'] if 'PYTHON_ENV' in os.environ else 'development'
    ENV = ENV or 'development'

    # raise error if environment is not expected
    if ENV not in ENV_CONFIG:
        raise EnvironmentError(f'Config for envirnoment {ENV} not found')

    config = GLOBAL_CONFIG.copy()
    config.update(ENV_CONFIG[ENV])

    config['ENV'] = ENV
    config['DEVICE'] = 'cuda' if torch.cuda.is_available() and config['USE_CUDE_IF_AVAILABLE'] else 'cpu'

    return config

# load config for import
CONFIG = get_config()

if __name__ == '__main__':
    # for debugging
    import json
    print(json.dumps(CONFIG, indent=4))

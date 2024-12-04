#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field


class InferenceInput(BaseModel):
    """
    Input values for model inference
    """
    text: str = Field(..., example='hello, my name is onemt.', title='a sentence at a time')
    source_language: str = Field(..., example='eng', title='language of given text, in 3 character language code, i.e eng for English')
    target_language: str = Field(..., example='hin', title='language of text in which translation needs to be happen, in 3 character language code, i.e hin for Hindi')


class InferenceResult(BaseModel):
    """
    Inference result from the model
    """

    data: str = Field(..., example='hello, my name is onemt.', title='a translated sentence')
    languages: str = Field(..., example='eng:hin', title='language pair')
    version: str = Field(..., example='IIITHV0.0.0.3', title='model version')


class InferenceResponse(BaseModel):
    """
    Output response for model inference
    """
    error: bool = Field(..., example=False, title='Whether there is error')
    data: str = Field(..., example='hello, my name is onemt.', title='a translated sentence')
    languages: str = Field(..., example='eng:hin', title='language pair')
    version: str = Field(..., example='IIITHV0.0.0.3', title='model version')


class ErrorResponse(BaseModel):
    """
    Error response for the API
    """
    error: bool = Field(..., example=True, title='Whether there is error')
    message: str = Field(..., example='', title='Error message')
    traceback: str = Field(None, example='', title='Detailed traceback of the error')

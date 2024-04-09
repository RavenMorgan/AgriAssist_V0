import pandas as pd
import requests
from transformers import pipeline
unmasker = pipeline('fill-mask', model='bert-base-cased')
unmasker("The man worked as a [MASK].")
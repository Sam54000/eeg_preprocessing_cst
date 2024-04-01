[![DOI](https://zenodo.org/badge/657341621.svg)](https://zenodo.org/doi/10.5281/zenodo.10383685)

# CST EEG Preprocessing pipeline

This repository hosts the code for preprocessing EEG data during a CST at 
Nathan Kline Institute.

# eeg_cst_preprocessing

[![Build](https://github.com/childmindresearch/eeg_preprocessing_cst/actions/workflows/test.yaml/badge.svg?branch=main)](https://github.com/childmindresearch/eeg_preprocessing_cst/actions/workflows/test.yaml?query=branch%3Amain)
[![codecov](https://codecov.io/gh/childmindresearch/eeg_preprocessing_cst/branch/main/graph/badge.svg?token=22HWWFWPW5)](https://codecov.io/gh/childmindresearch/eeg_preprocessing_cst)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
![stability-stable](https://img.shields.io/badge/stability-stable-green.svg)
[![LGPL--3.0 License](https://img.shields.io/badge/license-LGPL--3.0-blue.svg)](https://github.com/childmindresearch/eeg_preprocessing_cst/blob/main/LICENSE)
[![pages](https://img.shields.io/badge/api-docs-blue)](https://childmindresearch.github.io/eeg_preprocessing_cst)

## Installation

Install this package via :

```sh
pip install eeg_preprocessing_cst
```

Or get the newest development version via:

```sh
pip install git+https://github.com/childmindresearch/eeg_preprocessing_cst
```

## Quick start

The pipeline can be called with the following code:
```Python
from eeg_preprocessing_cst.pipeline import CSTpreprocessing as preprocess
```

Then you just have to create the object and provide the EEG filename and 
the events filename (in .csv format) as follow:
```Python
preprocess = preprocess(EEG_filename, events_filename)
```

Then, to prepare you raw data for processing you run the following code:
```Python
preprocess.set_annotations_to_raw().set_montage()
```

Finally you can run the different cleaning pipelines 
(careful it can take a very long time):
```Python
preprocess.run_prep()
preprocess.run_asr()
```

## Links or References

- [https://www.wikipedia.de](https://www.wikipedia.de)

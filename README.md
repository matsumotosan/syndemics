# Syndemics

## Installation

Create a virtual environment and install the requirements:

```sh
python -m venv .venv
source activate .venv/bin/activate

pip install -r requirements.txt
```

## Running 

### Download PDFs

Download PDFs from [Google Drive folder]("https://drive.google.com/drive/folders/1iXGcp-935YK8L27EFt5YzA_Wx1R9AOzd").

Place PDFs in directory `./SyndemicsResearchArticles`.

### Text extraction

Extract text from PDFs:

```sh
python extract.py
```

Output of parsed texts will be in new directory `./parsed`.

### LDA model

Train an LDA model on extracted text:

```sh
python lda.py
```

## References

# Syndemics

## Installation

Create a virtual environment and install the requirements:

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running 

### Download PDFs

Download PDFs from [Google Drive folder]("https://drive.google.com/drive/folders/1iXGcp-935YK8L27EFt5YzA_Wx1R9AOzd").

Place PDFs in directory `./SyndemicsResearchArticles`.

### Text extraction

Extract text from PDFs:

```sh
python extract_text.py
```

Output of parsed texts will be in new directory `./parsed`.

### LDA model

Train an LDA model on extracted text:

```sh
# Default text dir is `./parsed`
python lda.py

# If using text in non-default directory
python lda.py --text_dir=<text_dir>
```

### HDP model

Train an HDP model on extracted text:

```sh
# Default text dir is `./parsed`
python hdp.py

# If using text in non-default directory
python hdp.py --text_dir=<text_dir>
```

## References

- [PyMuPDF: Text](https://pymupdf.readthedocs.io/en/latest/recipes-text.html#)

import os
from pathlib import Path

import pymupdf
from tqdm import tqdm

URL = "https://drive.google.com/drive/folders/1iXGcp-935YK8L27EFt5YzA_Wx1R9AOzd"

output_dir = "./parsed"
pdf_dir = "./SyndemicsResearchArticles"


def main():
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(pdf_dir, exist_ok=True)

    # Download files from GDrive folder (limited to 50)
    # Either edit source code in virtual environment or download manually
    # Easier to just download manually
    # gdown.download_folder(URL, output=pdf_dir, quiet=False)

    # Extract text for all PDFs
    path_pdf = Path(pdf_dir)
    path_output = Path(output_dir)

    files = [f for f in path_pdf.iterdir() if f.is_file()]

    for f in tqdm(files):
        with pymupdf.open(f) as doc:
            text = chr(12).join([page.get_text() for page in doc])

        basename = f.stem

        # write as a binary file to support non-ASCII characters
        Path(path_output / f"{basename}.txt").write_bytes(text.encode())


if __name__ == "__main__":
    main()

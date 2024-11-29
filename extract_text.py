import os
import pathlib
import gdown
import pymupdf
from tqdm import tqdm


URL = "https://drive.google.com/drive/folders/1iXGcp-935YK8L27EFt5YzA_Wx1R9AOzd"


def main():
    output_dir = "./output"
    pdf_dir = "./SyndemicsResearchArticles"

    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(pdf_dir, exist_ok=True)

    # Download files from GDrive folder (limited to 50)
    # Either edit source code in virtual environment or download manually
    # gdown.download_folder(URL, output=pdf_dir, quiet=False)

    # Extract text for all PDFs
    path_pdf = pathlib.Path(pdf_dir)
    path_output = pathlib.Path(output_dir)

    files = [f for f in path_pdf.iterdir() if f.is_file()]

    for f in tqdm(files):
        with pymupdf.open(f) as doc:
            text = chr(12).join([page.get_text() for page in doc])

        basename = f.stem

        # write as a binary file to support non-ASCII characters
        pathlib.Path(path_output / f"{basename}.txt").write_bytes(text.encode())


if __name__ == "__main__":
    main()

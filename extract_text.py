from pathlib import Path

import pymupdf
from tqdm import tqdm

URL = "https://drive.google.com/drive/folders/1iXGcp-935YK8L27EFt5YzA_Wx1R9AOzd"

output_dir = "./parsed"
pdf_dir = "./SyndemicsResearchArticles"


def main():
    # Download files from GDrive folder (limited to 50)
    # Either edit source code in virtual environment or download manually
    # os.makedirs(pdf_dir, exist_ok=True)
    # gdown.download_folder(URL, output=pdf_dir, quiet=False) # easier to just download manually

    # Extract text for all PDFs
    path_pdf = Path(pdf_dir)
    path_output = Path(output_dir)
    path_output.mkdir(parents=True, exist_ok=True)

    files = [f for f in path_pdf.iterdir() if f.is_file()]

    for f in tqdm(files):
        with pymupdf.open(f) as doc:
            text = chr(12).join([page.get_text() for page in doc])

        # write as a binary file to support non-ASCII characters
        basename = f.stem
        Path(path_output / f"{basename}.txt").write_bytes(text.encode())


if __name__ == "__main__":
    main()

import fitz
from pathlib import Path
from typing import Union


def pdf_need_ocr_check(pdf_filepath: Path) -> bool:
    """Given a PDF filepath, returns a determination if the PDF needs OCR

    Args:
        pdf_filepath (Path): the PDF filepath

    Returns:
        bool: A boolean indication "needs OCR: True/False"
    """

    doc = fitz.open(pdf_filepath)

    text_list = list()
    for page in doc:
        text_list.append(page.get_textpage().extractText())

    text = "".join(text_list).strip()

    if text == "":
        # the PDF needs OCR
        result = True
    else:
        # does not need OCR - the PDF is machine readable
        result = False

    return result

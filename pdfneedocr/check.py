import fitz
from pathlib import Path
from typing import Union


def need_ocr_check(pdf_filepath: Path) -> Union[bool, str]:
    """Given a PDF filepath, returns a determination if the PDF needs OCR

    Args:
        pdf_filepath (Path): the PDF filepath

    Returns:
        Union[bool, str]: Either a boolean indication "needs OCR: True/False" or the exception encountered attempting to read the PDF
    """

    try:
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

    except Exception as e:
        # An exception was encountered attempting to read the PDF
        result = e

    return result

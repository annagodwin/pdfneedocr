# Documentation

`pdfneedocr` answers the question: Does a "PDF Need OCR"? with a `True/False` response.

## Installation

To use **pdfneedocr** first install it using pip:

```
python -m pip install "pdfneedocr @ git+https://github.com/annagodwin/pdfneedocr.git"
```

## Example

**pdfneedocr** simply returns one of three outcomes:

  - `True` if the PDF requires OCR

  - `False` if the PDF is machine readable and doesn't require OCR


```
>>> from pdfneedocr.check import pdf_need_ocr_check
>>> pdf_fpath = 'pdf_that_needs_ocr.pdf'
>>> pdf_need_ocr_check(pdf_fpath)
True

>>> from pdfneedocr.check import pdf_need_ocr_check
>>> pdf_fpath = 'pdf_that_is_machine_readable.pdf'
>>> pdf_need_ocr_check(pdf_fpath)
False
```

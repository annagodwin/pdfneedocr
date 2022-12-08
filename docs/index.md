# Documentation

Quickly determine if your PDF Needs OCR.

## Installation

To use **pdfneedocr** first install it using pip:

```
python -m pip install "pdfneedocr @ git+https://github.com/annagodwin/pdfneedocr.git"
```

## Example

**pdfneedocr** simply returns one of three outcomes:

  - `True` if the PDF requires OCR

  - `False` if the PDF is machine readable and doesn't require OCR

  - and the `exception` result, if an error is encountered attempting to read the PDF

```
>>> from pdfneedocr.check import need_ocr_check
>>> pdf_fpath = 'example.pdf'
>>> need_ocr_check(pdf_fpath)
True
```

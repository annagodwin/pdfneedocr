# pdfneedocr [![](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

`pdfneedocr` answers the question: Does a "PDF Need OCR?" with a `True` or `False` response.

The thought behind this package is to have **a quick method of determining if a PDF needs OCR**. If a PDF does require OCR, it leaves the method of which OCR technology to use up to the user.

Limitations: `pdfneedocr` is currently limited to testing if a PDF is readable from an "extract text" perspective. In other words, if it cannot read *text* (and only text) within a PDF, the PDF needs OCR. Next steps in development include checking if images and other objects are readable in the absence of text to determine if a PDF Needs OCR.

As of December 2022 `pdfneedocr` is under development. All feedback welcome!


## Installation

To use **pdfneedocr** first install it using pip:

```
pip install "pdfneedocr @ git+https://github.com/annagodwin/pdfneedocr.git"
```

## Example

See [examples](https://github.com/annagodwin/pdfneedocr/blob/main/examples) for a [Colab Notebook](https://github.com/annagodwin/pdfneedocr/blob/main/examples/try_out_pdfneedocr.ipynb) to try out `pdfneedocr`.

**pdfneedocr** simply returns one of two outcomes:

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

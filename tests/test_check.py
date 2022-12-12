from pdfneedocr.check import pdf_need_ocr_check


def test_pdf_need_ocr_check_need_ocr_false():

    outcome = pdf_need_ocr_check("tests/data/text_need_ocr_false.pdf")

    assert outcome is False


def test_pdf_need_ocr_check_need_ocr_true():

    outcome = pdf_need_ocr_check("tests/data/text_need_ocr_true.pdf")

    assert outcome is True

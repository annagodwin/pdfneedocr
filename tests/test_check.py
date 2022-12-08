from pdfneedocr.check import need_ocr_check


def test_need_ocr_check_needs_ocr():

    outcome = need_ocr_check("tests/data/82252956_2958.pdf")

    assert outcome is True


def test_need_ocr_check_machine_readable():

    outcome = need_ocr_check("tests/data/82252956_2958_ocr.pdf")

    assert outcome is False

import pathlib
from setuptools import setup, find_packages


base_packages = ["pymupdf>=1.21.0"]

docs_packages = ["mkdocs==1.4.2", "mkdocs-material==8.5.11", "mkdocstrings==0.19.0"]

test_packages = ["flake8>=3.6.0", "pytest>=4.0.2", "black>=19.3b0", "pre-commit>=2.2.0"]

all_packages = base_packages
dev_packages = all_packages + docs_packages + test_packages


setup(
    name="pdfneedocr",
    version="0.1.0",
    author="Anna Godwin",
    packages=find_packages(exclude=["notebooks", "docs"]),
    description="Quickly determine if a PDF Needs OCR",
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    license_files=("LICENSE"),
    url="https://annagodwin.github.io/pdfneedocr/",
    project_urls={
        "Documentation": "https://annagodwin.github.io/pdfneedocr/",
        "Source Code": "https://github.com/annagodwin/pdfneedocr/",
        "Issue Tracker": "https://github.com/annagodwin/pdfneedocr/issues",
    },
    install_requires=base_packages,
    extras_require={
        "all": all_packages,
        "dev": dev_packages,
    },
    classifiers=[
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
)

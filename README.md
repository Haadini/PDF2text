## Persian PDF to Text Converter

This repository contains code that enables the automated conversion of PDF files to text in Colab or Linux environments. The code utilizes OCR (Optical Character Recognition) techniques to extract text from PDF documents.

### Features

- Convert PDF files to text format
- Support for both Colab and Linux environments
- Automated processing of multiple pages
- Utilizes OCR technology for accurate text extraction

### Usage

- Clone
```bash
!git clone https://github.com/Haadini/PDF2text.git
```
- Install requirements for OS and Python
```bash
!python /content/PDF2text/PersianPDF2Text/install.py
```
- Import file
```python
from PDF2text.PersianPDF2Text import spliter, src
```
- Split PDF to 1 page(Optional)
```python
spliter.spliter('/content/drive/MyDrive/123.pdf')
```
- now you have docx and txt file
```python
src.pdf_to_word('/path_PDF_file/part_page_10.pdf', '/destination_path/')
```

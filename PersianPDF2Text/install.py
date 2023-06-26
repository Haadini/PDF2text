import subprocess

def install_packages():

    subprocess.check_call(["pip", "install", "tqdm", "pdf2image", "pytesseract", "Pillow", "python-docx", "PyPDF2"])

def install_system_packages():

    subprocess.check_call(["apt-get", "install", "-y", "poppler-utils", "libpoppler-cpp-dev", "tesseract-ocr", "libtesseract-dev", "tesseract-ocr-fas"])

install_packages()

install_system_packages()



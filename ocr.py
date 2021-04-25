import sys
import os
import pytesseract

async def read_image(file_path, lang='eng'):
    """
    Performs OCR on a single image

    :file_path: str, path to the image file
    :lang: str, language used while conversion (optional, default is English)

    Returns
    :text: str, converted text after OCR is performed on the image
    """
    pytesseract.pytesseract.tesseract_cmd='/app/.apt/usr/bin/tesseract'
    try:
        return pytesseract.image_to_string(file_path, lang=lang)
    except e:
        return "[ERROR] Unable to process file: {e}".format(e)


def read_images_from_dir(dir_path, lang='eng', write_to_file=False):
    """
    Performs OCR on multiple images from a given directory
    
    :dir_path: str, path to the directory
    :lang: str, language used while conversion (optional, default is English)
    :write_to_file: bool, whether to write the results in a file (optional, default is false)

    Returns
    :converted_text: dict, mapping of filename along with text output from each file
    """

    converted_text={}
    for file_ in os.listdir(dir_path):
        if file_.endswith(('png, jpg, jpeg')):
            file_path=os.path.join(dir_path, file_)
            text = read_image(file_path, lang='lang')
            converted_text[file_path] = text

    if write_to_file:
        for file_path, text in converted_text.items():
            filename= os.path.splitext(file_path)[0] + ".txt"
            _write_to_file(filename, text)
    
    return converted_text

def _write_to_file(filename, text):
    """
    Helper function which writes the text to a given file

    :filename: str, filename along with path to store the file
    :text: str, text to be written into the file
    """
    print("[INFO] Writing text to file: {0}".format(filename))
    with open(filename, 'w') as fp:
        fp.write(text)
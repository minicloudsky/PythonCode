from PIL import Image
from pytesseract import pytesseract
data = pytesseract.image_to_string(Image.open('D:\\pycharm\\PythonCode\\commercial_spider\\douban_send_text\\votebar3.png',lang='chi_sim'))
print(data)
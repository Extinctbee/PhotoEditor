from PIL import Image , ImageEnhance , ImageFilter
import os
from ChoiceHandler import editChoice
path = './imgs' # folder for unedited images
pathOut = '/editedImgs' # folder for edited images

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")
    current_img = img
    history = []
    while True:
        edit = editChoice(img,history)
        if edit == "SAVE_AND_EXIT":
            break
        current_img = edit
    clean_name = os.path.splitext(filename)[0]

    current_img.save(f'.{pathOut}/{clean_name}_edited.jpg')
    print(f"Final Version of {clean_name} saved!")


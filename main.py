from PIL import Image , ImageEnhance , ImageFilter
import os
from ChoiceHandler import editChoice
path = './imgs' # folder for unedited images
pathOut = '/editedImgs' # folder for edited images

for filename in os.listdir(path): # goes through every file in the images folder and opens it
    img = Image.open(f"{path}/{filename}")
    current_img = img # puts the image into current image so that it can be tracked

    history = [] # creates list we will use to store versions of the image

    while True: # keeps prompting edits until the user has saved all the edits and is done
        edit = editChoice(img,history) #calls the edit choice and passes the image and it's history

        if edit == "SAVE_AND_EXIT": #stops loop if user chooses to save
            break
        current_img = edit
    clean_name = os.path.splitext(filename)[0]

    current_img.save(f'.{pathOut}/{clean_name}_edited.jpg')  #saves the image to the edited images folder
    print(f"Final Version of {clean_name} saved!")


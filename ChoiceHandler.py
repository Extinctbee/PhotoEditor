from PIL import ImageFilter , ImageEnhance , Image


def editChoice(img):
    edits = {
        "sharpen" : ImageFilter.SHARPEN ,
        "blur"    : ImageFilter.BLUR ,
        "contour" : ImageFilter.CONTOUR ,
        "detail"  : ImageFilter.DETAIL ,
        "smooth"  : ImageFilter.SMOOTH
    }
    while True:
        user_choice = input("Enter an edit (sharpen , blur , contour , detail , smooth) or 'save' to finish :").lower().strip()
        if user_choice == 'save' :
            print("saving and exiting..")
            return img
            break
        selected_filter = edits.get(user_choice)
        if selected_filter:
            img = img.filter(selected_filter)
            print(f"Successfully applied {user_choice}")
        else:
            print("Invalid edit name please try again")
        return img
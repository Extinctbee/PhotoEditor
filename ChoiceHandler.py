from PIL import ImageFilter , ImageEnhance , Image


def editChoice(img,history):
    edits = {
        "sharpen" : ImageFilter.SHARPEN ,
        "blur"    : ImageFilter.BLUR ,
        "contour" : ImageFilter.CONTOUR ,
        "detail"  : ImageFilter.DETAIL ,
        "smooth"  : ImageFilter.SMOOTH

    }
    while True:


        user_choice = input("Enter an edit (sharpen , blur , contour , detail , smooth) or undo :").lower().strip()

        if user_choice == 'undo' :
            if len(history) > 0 :
                history.pop()
                img.show()
                print("Last edit undone !")
            else :
                print("nothing to undo")
        elif user_choice == 'save':
            return "SAVE_AND_EXIT"
        selected_filter = edits.get(user_choice)
        if selected_filter:
            history.append(img.copy())
            img = img.filter(selected_filter)
            print(f"Successfully applied {user_choice}")
            img.show()
        else:
            print("Invalid edit name please try again")
        return img
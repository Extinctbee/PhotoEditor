from PIL import ImageFilter , ImageEnhance , Image


def editChoice(img,history):
    edits = { # creates dictionary that maps users input to actual edit features
        "sharpen" : ImageFilter.SHARPEN ,
        "blur"    : ImageFilter.BLUR ,
        "contour" : ImageFilter.CONTOUR ,
        "detail"  : ImageFilter.DETAIL ,
        "smooth"  : ImageFilter.SMOOTH

    }
    while True: # keeps running prompt for user choice


        user_choice = input("Enter an edit (sharpen , blur , contour , detail , smooth) or undo :").lower().strip()

        if user_choice == 'undo' : #if the user wants to undo and an edit it will be "popped" out of the stack
            # and bring the image back to the previous version
            if len(history) > 0 :
                history.pop()
                img.show()
                print("Last edit undone !")
            else :
                print("nothing to undo")
        elif user_choice == 'save':
            #This input is what ultimately allows the user move on to the next image they want to edit
            #until they are done with all the images
            return "SAVE_AND_EXIT"
        selected_filter = edits.get(user_choice) #gets the user choice and fetches the edit type
        if selected_filter:
            history.append(img.copy()) #adds the current version of the image before the edit and will
            #continue adding the most recent version
            img = img.filter(selected_filter) # this changes the image to the edited version
            print(f"Successfully applied {user_choice}")
            img.show() #shows the edited image
        else:
            print("Invalid edit name please try again")
        return img
from conversion import Conversion
from asci import image

choice = ""
conversion = Conversion()
convert = True
print(image)

while convert:
    def get_started():
        global choice
        choice = input("To turn text into mors type 'Mors'\nTo turn mors into text type 'Text': ")
        choice = choice.lower()

        if choice == "mors" or choice == "text":
            return choice
        else:
            print("Please type 'Mors' or 'Text'")
            get_started()
    get_started()

    if choice == "mors":
        conversion.mors_action()
    else:
        conversion.text_action()

    def keep_converting():
        global convert
        print("-----------------------------------------------------")
        another = input("Do you want to make another conversion? Type 'Yes' or 'No': ")
        another = another.lower()

        if another == "yes":
            convert = True
        elif another == "no":
            print("Quiting...")
            convert = False
        else:
            print("Please type 'Yes' or 'No'")
            keep_converting()
        return convert
    keep_converting()

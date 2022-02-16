from string import GetString
from mors import MorsAlphabet

string = GetString()
mors = MorsAlphabet()


class Conversion:

    def mors_action(self):
        code_list = []
        user_text = string.get_user_text()
        characters = string.split_text(user_text)
        for character in characters:
            code = mors.get_values(character)
            code_list.append(f"{code} ")

        final_text = "".join(code_list)
        print(f"Your mors code is:\n{final_text}")

    def text_action(self):
        code_list = []
        user_text = string.get_user_mors()
        characters = string.split_mors(user_text)
        for character in characters:
            code = mors.get_keys(character)
            code_list.append(code)

        final_text = "".join(code_list)
        print(f"Your text is:\n{final_text}")

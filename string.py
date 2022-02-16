class GetString:

    def __init__(self):
        self.user_text = ""

    def get_user_text(self):
        self.user_text = input("Please enter the text you want to convert to mors code: ")
        return self.user_text

    def get_user_mors(self):
        self.user_text = input("Please enter the mors code you want to convert to text: ")
        return self.user_text

    def split_text(self, user_text):
        character_list = []
        for character in user_text:
            character = character.upper()
            character_list.append(character)
        return character_list

    def split_mors(self, user_text):
        character_list = []
        mors_list = user_text.split(" ")
        for character in mors_list:
            character = character.upper()
            character_list.append(character)
        return character_list

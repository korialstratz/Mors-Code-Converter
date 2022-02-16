class MorsAlphabet:

    def __init__(self):
        self.mors_alphabet = {
            "A": "*-",
            "B": "-***",
            "C": "-*-*",
            "Ç": "-*-*",
            "D": "-**",
            "E": "*",
            "F": "**-*",
            "G": "--*",
            "Ğ": "--*",
            "H": "****",
            "I": "**",
            "i": "**",
            "J": "*---",
            "K": "-*-",
            "L": "*-**",
            "M": "--",
            "N": "-*",
            "O": "---",
            "ö": "---",
            "P": "*--*",
            "Q": "--*-",
            "R": "*-*",
            "S": "***",
            "Ş": "***",
            "T": "-",
            "U": "**-",
            "Ü": "**-",
            "W": "*--",
            "X": "-**-",
            "V": "***-",
            "Y": "-*--",
            "Z": "--**",
            "1": "*----",
            "2": "**---",
            "3": "***--",
            "4": "****-",
            "5": "*****",
            "6": "-****",
            "7": "--***",
            "8": "---**",
            "9": "----*",
            "0": "-----",
            ".": "*-*-*-",
            ",": "--**--",
            ":": "---***",
            "?": "**--**",
            "'": "*----*",
            "(": "-*--*-",
            ")": "-*--*-",
            " ": " ",
        }
        self.character = ""

    def get_keys(self, letter):
        for key, value in self.mors_alphabet.items():
            if value == letter:
                self.character = key
                break
            elif letter == "":
                self.character = " "
                break
            else:
                self.character = letter
        return self.character

    def get_values(self, letter):
        for key, value in self.mors_alphabet.items():
            if key == letter:
                self.character = value
                break
            else:
                self.character = letter
        return self.character

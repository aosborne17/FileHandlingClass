
class Text_homework:
    def __init__(self, text_storage=None):
        self.text_storage = text_storage

    def take_text(self):
        try:
            name = input("Enter your name: ")
            if len(name) == 0:
                raise Exception
        except Exception:
            print("Sorry we don't take empty names")
            self.take_text()
        else:
            print("Thank you for giving your name {}".format(name))
        return name

    def write_and_read_to_file(self):
        try:
            text = input("Please add your text here: ")
            if len(text) == 0:
                raise Exception
        except Exception:
            print("Sorry we don't take empty text...")
            self.write_and_read_to_file()
        else:
            with open("homework.txt", "w+") as file:
                file.write(text)
                file.seek(0)
                self.text_storage = file.read()
            with open("second_homework.txt", "w") as file:
                file.write(self.text_storage)

            print("Your text has been written, check your files!!")

            return self.text_storage

    def read_image_file(self):
        with open('lol.png', 'rb') as picture:
                data = picture.read()
        with open('picture_out.png', 'wb') as f:
            f.write(data)













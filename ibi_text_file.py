
def writetextfilesusingwith(self):
    with open(order_text, "w+") as file, open(writer_text, "w+") as file2:
        try:
            file_input = (input("Enter your file input:"))
            if len(file_input) == 0:
                raise Exception("sorry we dont take empty names")
        except Exception:
            print("you did not enter anything")
            self.writetextfilesusingwith()
        else:
            file.write(file_input)
        file.seek(0)
        file2.write((file.read()))
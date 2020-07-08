class TextFileHandling:

    def __init__(self, file_path, text_storage=None):
        self.file_path = file_path
        self.text_storage = text_storage



    # Now we are going to read in two ways and write in two ways


    """
    Note that methods should only do one thing
    """
    def readTextFile(self):
        # open file
        # read the file
        # close the file

        file=open(self.file_path, 'r')
        # self.text_storage=file.read()
        # self.text_storage = file.read(3)
        self.text_storage = file.readline()
        # self.text_storage = file.readlines()
        file.close()
        return self.text_storage

    def writeTextFile(self):
        file = open("written.txt", 'w')
        file.write("My first Python created file")
        file.close()
        file = open("written.txt", "a+") # now we are using the 'append' arguement, which adds to our file
        file.write("\nI am now adding to my first Python created file")
        self.text_storage = file.read()
        file.close()
        print(file.closed) # Boolean value, whether the file is open or closed
        print(file.mode) # tells us the mode of the file
        print(file.name) # tells us the name of the file
        return self.text_storage


    def readTextFileUsingWith(self):
        """
        Here we are opening the file just to read it,
        automatically closes the file afterwards.
        """

        with open("order.txt", "r") as file:
            self.text_storage = file.read()
            return self.text_storage


    def writeTextFileUsingWith(self):
        with open ("written.txt", "w+") as file:
            file.write("Using writer with functionality")
            print(file.tell())
            file.seek(0)  # reposition the pointer to the beginning
            self.text_storage = file.read()
            return self.text_storage


    def playingWithOSModule(self):
        import os  # if only one function is using the module we can make do a local import

        print(os.getcwd()) # asking python to display the current directory
        # os.remove("written.txt") this would remove a file
        print(os.listdir()) # this tells us all the files inside of the current directory
        os.rename("order.txt", "modified.txt") # we have now given the order txt a new name 'modified.txt'




"""
The OS module in Python provides functions for creating and 
removing a directory (folder), fetching its contents, 
changing and identifying the current directory, etc.
"""


"""
file.tell() -> tells us where the pointer is when reading
file.close() -> will close the file we have opened

self.text_storage=file.read() = this reads the whole text file
self.text_storage = file.readline() -> this reads one line
self.text_storage = file.read(3) -> this reads three characters in the text
"""
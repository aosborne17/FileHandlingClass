

"""
This is one variable that handles the text file, so if there
is a change to the path you only have to change one variable
"""
file_path="modified.txt"

from textFile import TextFileHandling

"""
For the second attribute 'text storage'
as it is set to 'None' we don't need to put it in the
brackets below, only the file_path"""

textfileobject = TextFileHandling(file_path)

# print(textfileobject.readTextFile())
#
# print(textfileobject.writeTextFile())
# print(textfileobject.writeTextFileUsingWith())


# (textfileobject.playingWithOSModule())

print(textfileobject.playingWithException())
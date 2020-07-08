# File Handling

- Reading from and writing to files
- Exception handling
- CSV
- Assignments

One class per file is how we should be coding things


```bash

self.text_storage=file.read(3)
# the first 3 characters would be read in the text file    
important to close the file as it could cause issues
```

## Reading Files

file.close() -> will close the file we have opened
file.tell(n) -> tells us where the pointer is when reading
file.seek(n) -> Tells the pointer to go back to the point specified

self.text_storage=file.read() = this reads the whole text file
self.text_storage = file.readline() -> this reads one line
self.text_storage = file.read(3) -> this reads three characters in the text
self.text_storage = file.readable() -> Returns a boolean, whether the file can be read or not
self.text_storage = file.readlines() -> 


file = open("written.txt", 'a') # now we are using the 'append' arguement, which adds to our file
file = open("written.txt", 'a+') # as well as append, the plus allows us to read the file as well


## OS Module
The OS module in Python provides functions for creating and removing a directory (folder), 
fetching its contents, changing and identifying the current directory, etc.

## Exceptions

try block --> we try to run a certain code

except block --> if there is an exception in the try, we run this block

else --> If there is no exception in the try we run this block

finally --> This block is always run no matter the above outcomes

```python
    def playingWithException(self):
        try:
            file = open(self.file_path, 'r')

        except Exception as e:  # this exception looks for any error
            print(e)
        except FileNotFoundError as e:  # This exception looks for a specific error
            print(e)
            print("File not present")
        else:
            self.text_storage = file.readline()
            file.close()
            print("File was successfully found!")
        finally:
            print("This will run regardless of the above outcomes!")
            return self.text_storage
```
The above code won't work because we have written generalised
exception before the specific exception, so the specific exception
becomes unreachable.

## Raising Exceptions

Here we can create our own exceptions that Python does not have
E.g. We can raise an error if somebody inputs zero characters when asked for their name


## Today's homework

[16:21]

1. Accept from the user some text. Ensure user enters something else raise an exception.
After that write that text to a file and then read from this file to  write to another file simultaneously
2. Reading an image to  writing to another file simultaneously

Homework Completed, [19:00]




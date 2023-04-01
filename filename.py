filename = input("Input the Filename: ")

filename_parts = filename.split(".")

extension = filename_parts[-1]

print("The extension of the file is: '{}'".format(extension))

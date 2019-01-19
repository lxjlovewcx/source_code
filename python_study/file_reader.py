import Pygame
filename = "text_files\圆周率.txt"
with open( filename) as file_object:
   # contents = file_object.read()
   # print(contents.rstrip())
   #print(list(file_object))
   #for line in file_object:
   #    print(line.rstrip())
   lines=file_object.readlines()
   numbers=""
   print(lines)
   for line in lines:
   #    print(line.rstrip())
        numbers += line.strip()
   print(numbers)
   print(len(numbers))


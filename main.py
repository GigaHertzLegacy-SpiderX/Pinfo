
print(""" 

                       __________                                 
                     .'----------`.                              
                     | .--------. |                             
                     | |########| |       __________              
                     | |########| |      /__________\             
            .--------| `--------' |------|    --=-- |-------------.
            |        `----,-.-----'      |o ======  |             | 
            |       ______|_|_______     |__________|             | 
            |      /  %%%%%%%%%%%%  \                             | 
            |     /  %%%%%%%%%%%%%%  \                            | 
            |     ^^^^^^^^^^^^^^^^^^^^   Gigahertz Legacy-SpiderX | 
            +-----------------------------------------------------+
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 

            """)

print("            --------------Extract EXIF data from image-------------")
print("")
print("1. Select image ")
print("2. Exit ")
print("")
user_input = int(input("Enter your choice: "))

if user_input == 1:
    from PIL import Image
    from PIL.ExifTags import TAGS
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename

    print("")
    Tk().withdraw()
    imagename = askopenfilename()
    image = Image.open(imagename)
    exifdata = image._getexif()

    if isinstance(exifdata, dict):
        for tag, value in exifdata.items():
            decoded = TAGS.get(tag, tag)
            print("%s: %s" % (decoded, value))
    else:
        print("No EXIF data found")


elif user_input == 2:
    print("Exiting")
    exit()

else:
    print("Invalid input")
    exit()

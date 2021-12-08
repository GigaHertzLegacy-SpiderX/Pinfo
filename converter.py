print("""

            .--.
            |__| .-------.
            |=.| |.-----.|
            |--| || GLX ||
            |  | |'-----'|
            |__|~')_____('
                    """)
print("")
print("1. Choose a image ")
print("2. Exit")
print("")

user_input =int(input("Enter your Choice: "))

if user_input == 1:
    from PIL import Image
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename

    Tk().withdraw()
    imagename = askopenfilename()
    im1 = Image.open(f"{imagename}")
    im1.save(r'spiderx.jpg')
    print("Done, Saved as spiderx.jpg")


elif user_input == 2:
    print("Exiting...")
    exit()


else:
    print("Invalid Input")
    exit()
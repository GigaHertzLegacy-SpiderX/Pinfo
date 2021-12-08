print("""

             ______________
            ||            ||
            ||            ||
            ||            ||
            ||____________||
            |______________|
             \\#############\\
              \\#############\\
               \      ____   \   
                \_____\__\____\GLX

                            """)

print("")
print("1. Select Image")
print("2. Exit")
print("")

user_input = int(input("Enter your choice: "))
print("")

if user_input == 1:
    import tkinter.filedialog

    import exifread as ef
    from tkinter import Tk
    from tkinter.filedialog import askopenfilename


    # https://stackoverflow.com/questions/19804768/interpreting-gps-info-of-exif-data-from-photo-in-python
    # barrowed from
    # https://gist.github.com/snakeye/fdc372dbf11370fe29eb
    def _convert_to_degress(value):
        """
        Helper function to convert the GPS coordinates stored in the EXIF to degress in float format
        :param value:
        :type value: exifread.utils.Ratio
        :rtype: float
        """
        d = float(value.values[0].num) / float(value.values[0].den)
        m = float(value.values[1].num) / float(value.values[1].den)
        s = float(value.values[2].num) / float(value.values[2].den)

        return d + (m / 60.0) + (s / 3600.0)


    def getGPS(filepath):
        '''
        returns gps data if present other wise returns empty dictionary
        '''
        with open(filepath, 'rb') as f:
            tags = ef.process_file(f)
            latitude = tags.get('GPS GPSLatitude')
            latitude_ref = tags.get('GPS GPSLatitudeRef')
            longitude = tags.get('GPS GPSLongitude')
            longitude_ref = tags.get('GPS GPSLongitudeRef')
            if latitude:
                lat_value = _convert_to_degress(latitude)
                if latitude_ref.values != 'N':
                    lat_value = -lat_value
            else:
                print("")
                return print("No Data Found !")
                print("")


            if longitude:
                lon_value = _convert_to_degress(longitude)
                if longitude_ref.values != 'E':
                    lon_value = -lon_value
            else:
                return {}
            return {'latitude': lat_value, 'longitude': lon_value}
        return {}


    Tk().withdraw()
    file_path = askopenfilename()
    gps = getGPS(file_path)
    print(gps)

elif user_input == 2:
    print("Exiting...")
    exit()

else:
    print("Invalid input")
    exit()

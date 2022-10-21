from PIL import Image
import os

downloadsFolder = "/Users/User23/Downloads/"
picturesFolder = "/Users/User23/Pictures/Roland_Descargas/"


if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(downloadsFolder + filename)
            picture.save(picturesFolder + "c_"+filename, optimize=True, quality=60)
            os.remove(downloadsFolder + filename)
            print(name + ": " + extension)

        if extension in [".exe"]:
            appFolder = "/Users/User23/Documents/APP_descargas/"
            os.rename(downloadsFolder + filename, appFolder + filename)

        if extension in [".mp4"]:
            videoFolder = "/Users/User23/Videos/"
            os.rename(downloadsFolder + filename, videoFolder + filename)

        if extension in [".xlsx"]:
            excelFolder = "/Users/User23/Desktop/nasly/"
            os.rename(downloadsFolder + filename, excelFolder + filename)
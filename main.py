# imports
import cv2

# resizes and concatenates images
# (from https://www.geeksforgeeks.org/concatenate-images-using-opencv-in-python/)
def hconcat_resize(img_list: list, interpolation = cv2.INTER_CUBIC):
    # take minimum hights
    h_min = min(img.shape[0] for img in img_list)

    # image resizing 
    im_list_resize = [cv2.resize(img,
                       (int(img.shape[1] * h_min / img.shape[0]),
                        h_min), interpolation
                                 = interpolation) 
                      for img in img_list]

    # return final image
    return cv2.hconcat(im_list_resize)

# defines the dict for converting chars
conversionDict = {
    "a":"images/A.png",
    "b":"images/B.png",
    "c":"images/C.png",
    "d":"images/D.png",
    "e":"images/E.png",
    "f":"images/F.png",
    "g":"images/G.png",
    "h":"images/H.png",
    "i":"images/I.png",
    "j":"images/J.png",
    "k":"images/K.png",
    "l":"images/L.png",
    "m":"images/M.png",
    "n":"images/N.png",
    "o":"images/O.png",
    "p":"images/P.png",
    "q":"images/Q.png",
    "r":"images/R.png",
    "s":"images/S.png",
    "t":"images/T.png",
    "u":"images/U.png",
    "v":"images/V.png",
    "w":"images/W.png",
    "x":"images/X.png",
    "y":"images/Y.png",
    "z":"images/Z.png",
    ".":"images/dot.png",
    ",":"images/comma.png",
    " ":"images/space.png"
}

# gets the string to convert
userString = input("Enter the string you want to convert:\n")

# creates a list of images to pull from the images folder
try:
    imageStrings = [conversionDict[x] for x in userString.lower()]
# exists if user inputs character that cant be converted
except KeyError:
    print ('Please only use letters and ",", ".", and " ". Now exiting...')
    exit(0)

# gets all image objects and puts them in a list
images = [cv2.imread(x, cv2.IMREAD_UNCHANGED) for x in imageStrings]

# conatinates image and writes it to output.png
concatImage = hconcat_resize(images)
cv2.imwrite("output.png", concatImage)
print ("Conversion completed!")

from imutils import paths
import face_recognition
import pickle
import cv2
import os
 
#get paths of each file in folder named Images
#Images here contains my data(folders of various persons)
imagePaths = list(paths.list_images('C:/Users/shri1/sih/sih-project-2022/sih-project-final/face_function/Images'))
knownEncodings = []
knownNames = []

# loop over the image paths
for (i, imagePath) in enumerate(imagePaths):
    # extract the person name from the image path
    name = imagePath.split(os.path.sep)[-2]
    # load the input image and convert it from BGR (OpenCV ordering)
    # to dlib ordering (RGB)
    image = cv2.imread(imagePath)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    #Use Face_recognition to locate faces

    boxes = face_recognition.face_locations(rgb,model='hog')
    
    # compute the facial embedding for the face
    encodings = face_recognition.face_encodings(rgb, boxes)
    # loop over the encodings
    for encoding in encodings:
        knownEncodings.append(encoding)
        knownNames.append(name)
        
#save encodings along with their names in dictionary data
data = {"encodings": knownEncodings, "names": knownNames}

#print(data)
#use pickle to save data into a file for later use
f = open("C:/Users/shri1/sih/sih-project-2022/sih-project-final/face_function/face_enc", "wb")
f.write(pickle.dumps(data))
f.close()

print("completed")


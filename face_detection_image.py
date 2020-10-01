import face_recognition
import cv2

IMAGE_NAME = "120616_web.jpg"

image = cv2.imread(f"data/{IMAGE_NAME}")

# Find all the faces in the image using the default HOG-based model.
face_locations = face_recognition.face_locations(image)

print("Found {} faces in this photograph.".format(len(face_locations)))
for face_location in face_locations:
    # Print the location of each face in this image
    top, right, bottom, left = face_location
        
    # We can draw rectangle using OpenCV rectangle method
    cv2.rectangle(image, (left, top), (right, bottom), (255, 255, 1), 3)

cv2.imwrite("output/" + IMAGE_NAME, image)
cv2.imshow("img", image)
cv2.waitKey(0)

# Distroy windows
cv2.destroyAllWindows()

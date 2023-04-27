import cv2

# initialize the Haar cascades for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# define a function to detect faces in an image
def detect_faces(img):
    # convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    # draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # display the image with the detected faces
    cv2.imshow('Detected Faces', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# ask the user for input
input_type = input("Enter 'image' for image input or 'video' for video input: ")

if input_type == 'image':
    # ask the user for the path to the input image
    img_path = input("Enter the path to the input image: ")
    # read the image from the specified path
    image = cv2.imread(img_path)
    # Get the size of the screen
    screen_res = 1000, 1000
    # Resize the image to fit the screen
    scale_width = screen_res[0] / image.shape[1]
    scale_height = screen_res[1] / image.shape[0]
    scale = min(scale_width, scale_height)
    window_width = int(image.shape[1] * scale)
    window_height = int(image.shape[0] * scale)
    resized_image = cv2.resize(image, (window_width, window_height))
    # detect faces in the image
    detect_faces(resized_image)
    
elif input_type == 'video':
    input_type = input("Enter 'camera' for live video, or video path: ")
    if input_type == 'camera':
        # Open the default camera device
        cap = cv2.VideoCapture(0)
    else:
        # Open the video file
        cap = cv2.VideoCapture(input_type)
        # # Load the face detection classifier
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # Loop over frames from the video or live camera    
    while True:
        # Read a frame from the video or live camera
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Perform face detection on the grayscale frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw a rectangle around each face detected
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Display the frame with face detection
        cv2.imshow("Face Detection", frame)

        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture device
    cap.release()
    cv2.destroyAllWindows()

else:
    print("Invalid input type. Please enter 'image' or 'video'.")

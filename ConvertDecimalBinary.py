import cv2
import tensorflow as tf

# Load the pre-trained model
model = tf.keras.models.load_model('path_to_model')

# Load the image
image = cv2.imread("C:\\Users\\Sayan Patra\\Desktop\\Walp.png")

# Preprocess the image
preprocessed_image = preprocess_image(image)

# Perform object detection
predictions = model.predict(preprocessed_image)

# Process the predictions
detected_objects = process_predictions(predictions)

# Display the detected objects
for obj in detected_objects:
    cv2.rectangle(image, (obj['x'], obj['y']), (obj['x'] + obj['width'], obj['y'] + obj['height']), (0, 255, 0), 2)
    cv2.putText(image, obj['label'], (obj['x'], obj['y'] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# Show the image with detected objects
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
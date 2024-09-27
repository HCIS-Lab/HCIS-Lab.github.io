import numpy as np
import cv2

input_path = "framework.png"
output_path = "framework.png"


def remove_background(image_path, output_path, threshold=254):

    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Image not found or invalid image format")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    x_list, y_lisy = np.where(gray<threshold)
    x1, x2 = np.min(x_list), np.max(x_list)
    y1, y2 = np.min(y_lisy), np.max(y_lisy)    
    gray = gray[x1:x2, y1:y2]
    image = image[x1:x2, y1:y2]

    _, mask = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)

    mask = 255 - mask
    result = cv2.bitwise_and(image, image, mask=mask)

    alpha = mask
    b, g, r = cv2.split(result)
    rgba = [b, g, r, alpha]
    result = cv2.merge(rgba, 4)

    cv2.imwrite(output_path, result)

remove_background(input_path, output_path)
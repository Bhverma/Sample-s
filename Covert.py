import cv2


"""img = cv2.imread('29_324843.jpeg')


img2 = cv2.getRectSubPix(img, (98, 33), (20, 10))

cv2.imshow('img2',img2)
print("---------")
cv2.waitKey(0)"""
from PIL import Image
imgpath = r'246_323358.png'
def crop_image(imgpath, box):     # Open the image     image = Image.open(image_path)    # Crop the image using the bounding box coordinates     cropped_image = image.crop(box)
    # Return the cropped image     return cropped_image# Example usage image_path = "path/to/your/image.jpg" bounding_box = (x_min, y_min, x_max, y_max)  # Provide the coordinates of the bounding box 
    cropped_image = crop_image(image_path, bounding_box)
    cropped_image.show()


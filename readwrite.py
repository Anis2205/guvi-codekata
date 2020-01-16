import cv2
image = cv2.imread(r"C:\Users\sempe\OneDrive\Desktop\im\IMG_E6056.JPG",0)
print(image)
cv2.imshow('image',image)
k=cv2.waitKey(0)
if k==27:
   cv2.destroyAllWindows()
elif k==ord('s'):
   cv2.imwrite(r'C:\Users\sempe\OneDrive\Desktop\im\IMG_E6056.JPG_copy.jpg',image)
   cv2.destroyAllWindows()

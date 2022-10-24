from PIL import Image 
 
  
img = Image.open("segan.jpg") 
 
rotate_img= img.rotate(45)
 
rotate_img.show() 

import anvil.server
anvil.server.connect("")#enter your uplink key here

from tensorflow.keras.models import load_model 

from tensorflow.keras.preprocessing.image import img_to_array,load_img
from PIL import Image as img
from tensorflow.keras.applications.mobilenet import MobileNet

model=MobileNet(include_top=False,weights='imagenet',input_shape=(224,224,3))
testing_model=load_model('best_mobile_net (1).h5')

import anvil.media

@anvil.server.callable
def classify_image(file):
  with anvil.media.TempFile(file) as filename:
    img=load_img(filename,target_size=(224,224))
  
  
  image_arr = img_to_array(img)
  image_arr = np.expand_dims(image_arr, axis = 0) 
  image_arr /= 255.0

  
  score=testing_model.predict(image_arr)

  
  return ('its a CAT,  probability:-' if score<0.5 else 'its a DOG,  probability:-', float(score))

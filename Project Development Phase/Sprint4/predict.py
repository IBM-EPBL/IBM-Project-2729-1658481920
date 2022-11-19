
import warnings
warnings.filterwarnings('ignore')

import tensorflow as tf 
classifierLoad = tf.keras.models.load_model('skinmodel.h5')

import numpy as np
from keras.preprocessing import image
test_image = image.load_img('Output/Out/ISIC_0000019.jpg', target_size = (200, 200))
#test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)
print(test_image)
result = classifierLoad.predict(test_image)
print(result)
out=''
if result[0][0] == 1:
    print("BasalCellCarcinoma")
    out = "BasalCellCarcinoma"
elif result[0][1] == 1:
    print("CutaneousT-celllymphoma")
    out = "CutaneousT-celllymphoma"
elif result[0][2] == 1:
    print("DermatofibrosarcomaProtuberans")
    out = "DermatofibrosarcomaProtuberans"
elif result[0][3] == 1:
    print("KaposiSarcoma")
    out = "KaposiSarcoma"
elif result[0][4] == 1:
    print("MerkelCellcarCinoma")
    out = "MerkelCellcarCinoma"
elif result[0][5] == 1:
    print("SebaceousGlandCarcinoma")
    out = "SebaceousGlandCarcinoma"
elif result[0][6] == 1:
    print("SquamousCellCarcinoma")
    out = "SquamousCellCarcinoma"
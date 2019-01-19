import numpy as np

import os
import re
from PIL import Image
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import random



def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "rgb(0, 0, 0)" 




def makeImage(text):
	
	# use Trump_img.png for Trump Mask
    cloud_mask = np.array(Image.open("Obama_img.png"))

    wc = WordCloud(background_color="white", max_words=1000, mask=cloud_mask)
    # generate word cloud
    wc.generate(text)

    # show
	
    plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3), interpolation="bilinear")
    plt.axis("off")
	
    plt.show()
	



# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# use trumpSpeech_CLEAN.txt for trump data
text = open(path.join(d, 'obamaSpeech_CLEAN.txt'), encoding='utf-8')
text = text.read()
makeImage(text)

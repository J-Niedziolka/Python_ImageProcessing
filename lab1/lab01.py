import os
import matplotlib.pyplot as plt
import matplotlib
from skimage import data, color
from skimage.transform import rescale, resize, downscale_local_mean

directory = r'/home/jannie/ro'
os.chdir(directory)

camera = data.camera()

plt.imshow(camera, cmap='gray')
plt.axis('off')#try comment this line

print(camera.shape)
print(camera.ndim)

matplotlib.rcParams['font.size'] = 18

images = ('astronaut',
          'binary_blobs',
          'brick',
          'colorwheel',
          'camera',
          'cat',
          'checkerboard',
          'clock',
          'coffee',
          'coins',
          'grass',
          'gravel',
          'horse',
          'logo',
          'page',
          'text',
          'rocket',
          )

for name in images:
    caller = getattr(data, name)
    image = caller()
    plt.figure()
    plt.title(name)
    plt.axis('off')
    if image.ndim == 2:
        plt.imshow(image, cmap=plt.cm.gray)
    else:
        plt.imshow(image)

cat = data.cat()
plt.imshow(cat)

plt.axis('off')#try comment this line

print(cat.shape)
print(cat.ndim)

                
plt.show()
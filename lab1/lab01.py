import os
import matplotlib.pyplot as plt
import matplotlib
from skimage import data, color
from skimage.transform import rescale, resize, downscale_local_mean

directory = r'/home/jannie/ro'
os.chdir(directory)

# camera = data.camera()

# plt.imshow(camera, cmap='gray')
# plt.axis('off')#try comment this line

# print(camera.shape)
# print(camera.ndim)

# matplotlib.rcParams['font.size'] = 18

# images = ('astronaut',
#           'binary_blobs',
#           'brick',
#           'colorwheel',
#           'camera',
#           'cat',
#           'checkerboard',
#           'clock',
#           'coffee',
#           'coins',
#           'grass',
#           'gravel',
#           'horse',
#           'logo',
#           'page',
#           'text',
#           'rocket',
#           )

# for name in images:
#     caller = getattr(data, name)
#     image = caller()
#     plt.figure()
#     plt.title(name)
#     plt.axis('off')
#     if image.ndim == 2:
#         plt.imshow(image, cmap=plt.cm.gray)
#     else:
#         plt.imshow(image)

# cat = data.cat()
# plt.imshow(cat)

# plt.axis('off')#try comment this line

# print(cat.shape)
# print(cat.ndim)

# image = color.rgb2gray(data.astronaut())

# image_rescaled = rescale(image, 0.25, anti_aliasing=False)
# image_resized = resize(image, (image.shape[0] // 4, image.shape[1] // 4),
#                        anti_aliasing=True)
# image_downscaled = downscale_local_mean(image, (4, 3))

# fig, axes = plt.subplots(nrows=2, ncols=2)

# ax = axes.ravel()

# ax[0].imshow(image, cmap='gray')
# ax[0].set_title("Original image")

# ax[1].imshow(image_rescaled, cmap='gray')
# ax[1].set_title("Rescaled image (aliasing)")

# ax[2].imshow(image_resized, cmap='gray')
# ax[2].set_title("Resized image (no aliasing)")

# ax[3].imshow(image_downscaled, cmap='gray')
# ax[3].set_title("Downscaled image (no aliasing)")

# ax[0].set_xlim(0, 512)
# ax[0].set_ylim(512, 0)
# plt.tight_layout()
# image_rescaled_with_aaF = rescale(image, 0.25, anti_aliasing=False)
# image_rescaled_with_aaT = rescale(image, 0.25, anti_aliasing=True)
# image_resized_with_aaF = resize(image, (image.shape[0] // 4, image.shape[1] // 4),
#                         anti_aliasing=False)
# image_resized_with_aaT = resize(image, (image.shape[0] // 4, image.shape[1] // 4),
#                         anti_aliasing=True)

# fig, axes = plt.subplots(nrows=2, ncols=2)
# ax = axes.ravel()

# ax[0].imshow(image_rescaled_with_aaF, cmap='gray')
# ax[0].set_title('rescaled with aa=false')

# ax[1].imshow(image_rescaled_with_aaT, cmap='gray')
# ax[1].set_title('rescaled image with aa=true')

# ax[2].imshow(image_resized_with_aaF, cmap='gray')
# ax[2].set_title('resized with aa=false')

# ax[3].imshow(image_resized_with_aaT, cmap='gray')
# ax[3].set_title('resized with aa=true')

# plt.tight_layout()

# original = data.astronaut()
# grayscale = color.rgb2gray(original)

# fig, axes = plt.subplots(1, 2, figsize=(16, 8))
# ax = axes.ravel()

# ax[0].imshow(original)
# ax[0].set_title("Original")
# ax[1].imshow(grayscale, cmap=plt.cm.gray)
# ax[1].set_title("Grayscale")

# fig.tight_layout()

rgb_img = data.coffee()
hsv_img = color.rgb2hsv(rgb_img)
hue_img = hsv_img[:, :, 0]
value_img = hsv_img[:, :, 2]

fig, (ax0, ax1, ax2) = plt.subplots(ncols=3, figsize=(8, 2))

ax0.imshow(rgb_img)
ax0.set_title("RGB image")
ax0.axis('off')
ax1.imshow(hue_img, cmap='hsv')
ax1.set_title("Hue channel")
ax1.axis('off')
ax2.imshow(value_img)
ax2.set_title("Value channel")
ax2.axis('off')

fig.tight_layout()

plt.show()
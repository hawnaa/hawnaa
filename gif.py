import imageio.v3 as iio
filenames = ['conan-1.png', 'conan-2.png']
images = [ ]
for filename in filenames:
  images.append(iio.imread(filename))
iio.imwrite('conan.gif', images, duration = 500, loop = 0)
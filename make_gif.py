import imageio

# Create an array of image filenames
filenames = [
    '0.jpg', '1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg',
    '8.jpg', '9.jpg', '10.jpg', '11.jpg', '12.jpg', '13.jpg', '14.jpg',
    '15.jpg', '16.jpg', '17.jpg', '18.jpg', '19.jpg'
]

# Load the images into memory
images = [imageio.imread(fn) for fn in filenames]

# Save the images as an animated gif
imageio.mimsave('animated.gif', images, fps=10)

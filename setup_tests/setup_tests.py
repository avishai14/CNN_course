import numpy as np
from scipy.misc import imread, imresize,imshow
import matplotlib.pyplot as plt

def main():
    # test num py
    x = np.arange(0, 3*np.pi, 0.01)

    plt.subplot(1,2,1)
    plt.plot(x,np.cos(x))
    plt.title('cos(x)')

    plt.subplot(1,2,2)
    plt.plot(x,np.sin(x))
    plt.title('sin(x)')

    plt.show()

    im = imread('..\\test_data\\beautiful_dog.jpg')
    plt.imshow(im)
    plt.show()


if __name__ == '__main__':
    main()

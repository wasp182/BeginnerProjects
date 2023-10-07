import numpy as np
import png

class Image:
    def __init__(self,x_pixel=0,y_pixel=0,num_channel=0,filename=" "):
        self.input_path = 'input/'
        self.output_path = 'output/'
        if x_pixel and y_pixel and num_channel:
            self.x_pixel = x_pixel
            self.y_pixel = y_pixel
            self.num_channel = num_channel
            self.array = np.zeros((x_pixel,y_pixel,num_channel))
        elif filename:
            self.array = self.read_image(filename)
            self.x_pixel , self.y_pixel , self.num_channel = self.array.shape
        else:
            raise ValueError("Filename not available or specify the dimensions")

    def read_image(self, filename, gamma=2.2):
        '''
        read PNG RGB image, return 3D numpy array organized along Y, X, channel
        values are float, gamma is decoded
        '''
        im = png.Reader(self.input_path + filename).asFloat()
        resized_image = np.vstack(list(im[2]))
        resized_image.resize(im[1], im[0], 3)
        resized_image = resized_image ** gamma
        return resized_image

    def write_image(self, output_file_name, gamma=2.2):
        '''
        3D numpy array (Y, X, channel) of values between 0 and 1 -> write to png
        '''
        im = np.clip(self.array, 0, 1)
        y, x = self.array.shape[0], self.array.shape[1]
        im = im.reshape(y, x*3)
        writer = png.Writer(x, y)
        with open(self.output_path + output_file_name, 'wb') as f:
            writer.write(f, 255*(im**(1/gamma)))
        self.array.resize(y, x, 3)  # we mutated the method in the first step of the function

if __name__ == '__main__':
    im = Image(filename='lake.png')
    im.write_image('test.png')

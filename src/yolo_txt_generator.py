import imgaug.augmenters as iaa
import imgaug as ia
import cv2
import os, sys
import yaml

class YoloTxtGenerator():
    def __init__(self):
        ### load param
        try:
            config_name = './param/' + 'yolo_txt_generator.yaml'
            with open(config_name) as file:
                self.yaml = yaml.load(file, Loader=yaml.FullLoader)
        except:
            exit('ERROR: yolo_txt_generator.yaml not defined.') 
        self.load_path = self.yaml['origin_img_path']
    
    def load_images_from_folder(self):
        img_filename = []
        for filename in os.listdir(self.load_path):
            if ".png" in filename:
                img_filename.append(filename)
        return img_filename

    def write_txt_path(self, img_filename):
        print(self.load_path + '/' + self.yaml['txt_file_name'] + ".txt")
        fr = open(self.yaml['txt_save_path'] + '/' + self.yaml['txt_file_name'] + ".txt", mode='a')
        for i in range(0,len(img_filename)):
            fr.write(self.load_path+'/'+img_filename[i]+"\n")
            print("txt saving complete "+ img_filename[i])
        fr.close()

def main():
    ytg = YoloTxtGenerator()
    ytg.write_txt_path(ytg.load_images_from_folder())

if __name__ == '__main__':
    if len(sys.argv) < 1:
        print('Usage: ')
        exit('$ python yolo_txt_generator.py')
    main()
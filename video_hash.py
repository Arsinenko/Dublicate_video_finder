import cv2
from PIL import Image, ImageOps
import imagehash
from converter import hash_to_bytearray, bytearray_to_hash, hash_bytearray_to_hashes_array
from numba import jit, cuda

w, h = 100, 200

import torch
import torchvision
 
def read_video(video_path):
   reader = torchvision.io.VideoReader(video_path, "video", num_threads=0)
   #resizer = torchvision.transforms.Resize(image_size_low, antialias=True)
 
   curr_frames = []
 
   for frame in reader:
       curr_frames.append(frame["data"])
       print(frame["data"])



#@cuda.jit('void(string[:])')
def get_hash(path_to_file):
    capture = cv2.VideoCapture(path_to_file)
    fps = int(capture.get(cv2.CAP_PROP_FPS))
    length = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))

    #result = bytearray()

    for i in range(0, int(length)):
        if i % fps != 0:
            capture.grab()
        else:
            success, frame = capture.read()

            resized_image = cv2.resize(frame, (w, h))
            gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

            img = Image.fromarray(gray)
            img_hor = ImageOps.mirror(img)

            blended_hor = Image.blend(img, img_hor, alpha=0.5)
            img_ver = ImageOps.flip(blended_hor)

            blended_ver = Image.blend(blended_hor, img_ver, alpha=0.5)
            cropped = blended_ver.crop((0, 0, w / 2, h / 2))

            hash1 = imagehash.phash(cropped, 16)
            #result.extend(hash_to_bytearray(hash1))


    #capture.release()
    #return result
    return 0
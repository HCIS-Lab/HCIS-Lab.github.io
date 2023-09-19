import cv2, glob, os
from tqdm import tqdm
import imageio

from PIL import Image


input_paths = ['skt-animation_fast.mp4']
for input_path in tqdm(input_paths):
    raw = cv2.VideoCapture(input_path)
    frames = []
    
    cnt = 0
    while True:
        ret, frame = raw.read()
        if not ret:
            break
        
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frames.append(frame)

        cnt += 1
        print(cnt)
    
    output_path = f'skt-animation_fast.gif'
    print(f'{output_path} saving')
    imageio.mimsave(output_path, frames,  duration=10, loop=0)
    print(f'{output_path} saved')
    # frames = [Image.fromarray(frame) for frame in frames]
    # print(f'saving {len(frames)}')
    # frames[0].save(output_path, save_all=True, append_images=frames[1:], duration=100, loop=0)
from PIL import Image,ImageSequence
import glob
import numpy as np
import imageio

if __name__=="__main__":
    gifs = glob.glob(f'*.gif')

    for gif in gifs:
        gif_frames = Image.open(gif)
        new_frames = []
        for gif_frame in ImageSequence.Iterator(gif_frames):
            gif_frame_np = np.asarray(gif_frame.resize((gif_frame.size[0]//3, gif_frame.size[1]//3)))  
            new_frames.append(Image.fromarray(gif_frame_np))
        new_path = f'down/{gif}'
        new_frames[0].save(new_path, save_all=True, append_images=new_frames[1:], duration=100, loop=0)
        print(f'{new_path} saved')
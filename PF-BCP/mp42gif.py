# import cv2, glob, os
# from tqdm import tqdm
# import imageio

input_paths = ["demo_v5.mp4"]
output_path = f"demo-ROI.gif"

# cnt = 0
# frames = []

# for input_path in tqdm(input_paths):
    
#     print(f'Read {input_path}')
#     raw = cv2.VideoCapture(input_path, cv2.CAP_FFMPEG)
#     if not raw.isOpened():
#         print(f"Error: Could not open video file {input_path}")
#         continue

#     while True:
#         ret, frame = raw.read()

#         if not ret:
#             break
        
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         if not (110 < cnt < 140 or 240 < cnt < 260):        
#             h, w, c = frame.shape
#             frame = cv2.resize(frame, (w//5*4, h//5*4), interpolation=cv2.INTER_AREA)
#             frames.append(frame)

#         cnt += 1
#         print(cnt)
    

# imageio.mimsave(output_path, frames,  duration=1/15.0, loop=0)
# print(f'{output_path} saved')
# raw.release()  # Release the video capture object    


# import imageio
# from PIL import Image, ImageSequence

# def mp4_to_gif(input_path, output_path, fps=15):
#     # 读取视频
#     video = imageio.get_reader(input_path, 'ffmpeg')
#     frames = []
    
#     # 获取视频的每一帧并转换为PIL格式的图像
#     cnt = 0
#     for frame in video:
#         if not (110 < cnt < 140 or 240 < cnt < 260):        
#             img = Image.fromarray(frame)
#             width, height = img.size
#             new_size = (int(width * 4 / 5), int(height * 4 / 5))
#             img_resized = img.resize(new_size, Image.LANCZOS)        
#             frames.append(img_resized)
#         cnt += 1

#     # 调整帧速率
#     duration = 1 / fps
    
#     # 将帧转换为GIF
#     frames[0].save(output_path, save_all=True, append_images=frames[1:], 
#                    duration=duration * 1000, loop=0, optimize=True, quality=95)

# if __name__ == "__main__":
#     mp4_to_gif(input_paths[0], output_path, fps=15)





import subprocess

def mp4_to_gif(input_path, output_path, fps=15):
    command = [
        'ffmpeg',
        '-i', input_path,  # 输入文件
        '-loop', '0',  # 设置GIF循环（0表示无限循环）
        '-y',  # 自动覆盖输出文件
        '-filter_complex', (
            '[0:v] select=\'not(between(n\\,300\\,420))*not(between(n\\,750\\,870))\', '  # 跳过第110到140帧和240到260帧
            # 'minterpolate=fps=30:mi_mode=mci, '  # 插入帧，增加流畅度
            'setpts=N/FRAME_RATE/TB, '  # 保持时间戳连续
            # 'scale=iw*4/5:ih*4/5, '  # 缩放到4/5
            f'fps={fps}, '  # 设置帧率
            'split [a][b]; [a] palettegen [p]; [b][p] paletteuse'  # 生成和应用调色板
        ),
        output_path  # 输出文件
    ]
    
    result = subprocess.run(command, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Error occurred: {result.stderr}")
    else:
        print("GIF generated successfully!")

if __name__ == "__main__":
    mp4_to_gif(input_paths[0], output_path, fps=30)

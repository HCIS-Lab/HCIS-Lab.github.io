import subprocess

input_paths = ["demo_v5.mp4"]
output_path = f"demo-ROI.gif"


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

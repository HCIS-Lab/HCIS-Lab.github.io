import subprocess

input_paths = ["demo.mp4"]
output_path = f"demo-ROI.gif"


def mp4_to_gif(input_path, output_path, fps=30):
    command = [
        'ffmpeg',
        '-i', input_path,
        '-loop', '0',
        '-y',
        '-filter_complex', (
            '[0:v] select=\'not(between(n\\,350\\,465))*not(between(n\\,800\\,915))\', '
            # 'minterpolate=fps=30:mi_mode=mci, '
            'setpts=N/FRAME_RATE/TB, ' 
            # 'scale=iw*4/5:ih*4/5, '
            f'fps={fps}, '
            'split [a][b]; [a] palettegen [p]; [b][p] paletteuse'
        ),
        output_path
    ]
    
    result = subprocess.run(command, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"Error occurred: {result.stderr}")
    else:
        print("GIF generated successfully!")

if __name__ == "__main__":
    mp4_to_gif(input_paths[0], output_path, fps=20)

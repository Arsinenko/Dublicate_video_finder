import ffmpeg
import os

def split_to_frames(video_path, fps, sizex, sizey, out_path):
    if not os.path.exists(out_path):
        os.makedirs(out_path)

    try:
        (ffmpeg.input(video_path)
              .filter('fps', fps=fps)
              .output(f'{out_path}/frame%d.png', 
                      video_bitrate='5000k',
                      s=f'{sizex}x{sizey}',
                      sws_flags='bilinear',
                      start_number=0)
              .run(capture_stdout=True, capture_stderr=True))
    except ffmpeg.Error as e:
        print('stdout:', e.stdout.decode('utf8'))
        print('stderr:', e.stderr.decode('utf8'))

split_to_frames('videos/test.mp4', 10, 200, 150, 'frames')
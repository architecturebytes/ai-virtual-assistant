import cv2
import pyautogui
import numpy as np
import time
from decouple import config

stop_recording_flag=False

def record_screen():
    global stop_recording_flag
    max_duration=20
    fps = 15

    screen_size = pyautogui.size()
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    video_file = config("MEDIA_DIR") + "/" + config("VIDEO_FILE")
    out = cv2.VideoWriter(video_file, fourcc, fps, (screen_size.width, screen_size.height))

    frame_interval = 1 / fps
    total_frames = int(max_duration * fps)
    start_time = time.time()

    print("Screen Recording Started")
    for _ in range(total_frames):
        if stop_recording_flag:
            break
        # Capture the screen
        img = pyautogui.screenshot()
        frame = np.array(img)

        # Convert the frame to BGR (pyautogui captures in RGB)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Write the frame to the video file
        out.write(frame)

        # Sleep to maintain the frame rate
        time_elapsed = time.time() - start_time
        sleep_time = frame_interval * (_ + 1) - time_elapsed
        if sleep_time > 0:
            time.sleep(sleep_time)

    print("Screen Recording Stopped")
    # Release the VideoWriter
    out.release()


def stop_recording():
    global stop_recording_flag
    stop_recording_flag = True

if __name__ == "__main__":   
    record_screen()

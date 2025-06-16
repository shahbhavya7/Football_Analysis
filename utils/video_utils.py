import cv2

def read_video(video_path): # taking video path

    cap = cv2.VideoCapture(video_path) # cv2.VideoCapture is used to read video and return frames 
    frames = [] # list of frames , frames are single image of video
    while True:
        ret, frame = cap.read() # ret is a boolean value that tells if the video is ended or not and frame is the frame that is read returned by cv2.VideoCapture
        if not ret: # if video is ended then break the loop
            break
        frames.append(frame) # append the frame to the list
    return frames

def save_video(output_video_frames,output_video_path): # The save_video function is designed to take a list of video frames (images) and save them as a video 
    # file at a specified path
    fourcc = cv2.VideoWriter_fourcc(*'XVID') # Using 'XVID' means the video will be encoded in a format that is widely supported and offers a good balance 
    # between file size and quality. The fourcc function converts the four-character code 'XVID' into a format that OpenCV’s VideoWriter can use to encode the 
    # video.
    out = cv2.VideoWriter(output_video_path, fourcc, 24, (output_video_frames[0].shape[1], output_video_frames[0].shape[0]))
    # cv2.VideoWriter object called out, which is responsible for writing the frames to the video file. The writer is configured with the output path, codec, 
    # a frame rate of 24 frames per second, and the frame size, which is determined from the shape of the first frame in the list.
    for frame in output_video_frames: # The function then iterates over each frame in ouput_video_frames and writes it to the video file using the write method. 
        # After all frames have been written, it calls release() on the writer object to finalize and close the video file properly. This ensures that all data 
        # is flushed and the file is not left in a corrupted state.
        out.write(frame)
    out.release()
import cv2

# 打开视频文件
video_path = "path_to_your_video.mp4"
cap = cv2.VideoCapture(video_path)

# 获取视频的帧率
fps = cap.get(cv2.CAP_PROP_FPS)

# 创建一个VideoWriter对象，用于保存加速后的视频
output_path = "path_to_save_output_video.mp4"
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
output = cv2.VideoWriter(output_path, fourcc, fps, (int(cap.get(3)), int(cap.get(4))))

# 逐帧读取视频并加速
while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    # 将帧速度乘以1.03来加速视频
    new_fps = fps * 1.03

    # 写入加速后的帧
    output.write(frame)

    # 显示加速后的视频
    cv2.imshow('Accelerated Video', frame)

    # 按下 'q' 键退出
    if cv2.waitKey(int(1000 / new_fps)) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
output.release()
cv2.destroyAllWindows()

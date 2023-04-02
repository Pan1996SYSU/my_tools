import cv2

# 打开WMV视频文件
video = cv2.VideoCapture('../灰度值统计工具.wmv')

# 获取视频帧速率和总帧数
fps = int(video.get(cv2.CAP_PROP_FPS))
total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

# 计算前26秒所占的总帧数
start_frame = 0
end_frame = int(fps * 26)

# 创建输出视频对象
fourcc = cv2.VideoWriter_fourcc(*'WMV2')
output_video = cv2.VideoWriter('../output.wmv', fourcc, fps, (int(video.get(3)), int(video.get(4))))

# 开始遍历视频帧并写入输出视频
for i in range(total_frames):
    ret, frame = video.read()
    if i >= start_frame and i <= end_frame:
        output_video.write(frame)
    if i > end_frame:
        break

# 释放视频对象和输出对象
video.release()
output_video.release()

print("视频剪辑完成！")

# Open the file in binary mode
with open(r"D:\桌面\sth\aaa\ee35db74ff73478d88黑板7c09c4d9c2ef5a.bmp.png", 'rb') as f:
    # Read the file data into a bytes object
    data = f.read()

# Modify the file header as desired
# For example, change the width and height values
width, height = (100, 100)  # new width and height
data = data[:16] + width.to_bytes(4, 'big') + height.to_bytes(4, 'big') + data[24:]

# Write the modified data back to the file
with open(r"D:\桌面\sth\aaa\ee35db74ff73478d88黑板7c09c4d9c2ef5a.bmp.png", 'wb') as f:
    f.write(data)
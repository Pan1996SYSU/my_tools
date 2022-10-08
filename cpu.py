import platform

import psutil
import wmi

free = str(
    round(psutil.virtual_memory().free / (1024.0 * 1024.0 * 1024.0), 2)) + 'GB'
total = str(
    round(psutil.virtual_memory().total /
          (1024.0 * 1024.0 * 1024.0), 2)) + 'GB'
memory_use_percent = str(psutil.virtual_memory().percent) + ' %'
print('可用内存：', free)
print('总内存', total)
print('内存占用率', memory_use_percent)
print('cpu占用率', str(psutil.cpu_percent(interval=1)) + ' %')
print('物理cpu个数', psutil.cpu_count(logical=False))

print("您的系统为:" + platform.system())
print("您的操作系统名称及版本号:" + platform.platform())
print("您的操作系统版本号:" + platform.version())
print("您的CPU生产商为:" + platform.machine())
print("您的CPU信息为:" + platform.processor())
print("获取操作系统的位数:", platform.architecture())
print("计算机的网络名称:" + platform.node())
print("包含上面所有的信息汇总:", platform.uname())

cpu_info = wmi.WMI()
for cpu in cpu_info.Win32_Processor():
    print("您的CPU序列号为:" + cpu.ProcessorId.strip())
    print("您的CPU名称为:" + cpu.Name)
    print("您的CPU已使用:%d%%" % cpu.LoadPercentage)
    print("您的CPU核心数为:%d" % cpu.NumberOfCores)
    print("您的CPU时钟频率为:%d" % cpu.MaxClockSpeed)

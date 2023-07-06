import threading
import time


def prevent_lock_screen(interval):
    """防止锁屏"""

    def press_key():
        import pyautogui
        # 模拟按下一个无关键的按键（这里使用 F15 键）
        pyautogui.press('a')

    # 创建线程并启动
    def thread_function():
        while True:
            press_key()
            time.sleep(interval)

    thread = threading.Thread(target=thread_function)
    thread.start()


prevent_lock_screen(1)

from PIL import ImageGrab
import time

time.sleep(5)

for i in range(1, 11):
    img = ImageGrab.grab() #현재 스크린 이미지 가져옴
    img.save("image{}.png".format(i)) #파일로 저장 1~10

    time.sleep(2)

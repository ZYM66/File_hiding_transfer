import base64
import random
import wave
from tqdm import tqdm
import time


def encipherment():
    name_file = input('请输入要加密文件的路径:')
    name_carrier = input('请输入文件载体路径:')
    name = input('请输入处理后文件的名字:')
    infomap = {}
    gap = random.randint(4, 7)

    with open(name_file, 'rb') as f:
        data = f.read()
        data_len = len(data)

    with wave.open(name_carrier, 'rb') as f:
        infomap['channels'] = f.getnchannels()
        infomap['sampwidth'] = f.getsampwidth()
        infomap['framerate'] = f.getframerate()
        wave_data = bytearray(f.readframes(-1))

    infolist = bytes((str(data_len) + 'A' + str(infomap['channels']) + str(infomap['sampwidth']) + str(
        infomap['framerate']) + str(gap)).encode('utf-8'))
    base_key = base64.b64encode(infolist)

    with wave.open('./Hidden_file/' + name + '.wav', 'wb') as w:
        w.setnchannels(infomap['channels'])
        w.setsampwidth(infomap['sampwidth'])
        w.setframerate(infomap['framerate'])
        try:
            for i in tqdm(range(data_len)):
                wave_data[i * gap] = data[i]
            w.writeframes(wave_data)
            time.sleep(0.5)
            print('你的key(不含单引号):' + str(base_key)[1:])
        except:
            print('错误，请换更大的载体文件！')

    with open('./Hidden_file/' + name + '.txt', 'w') as w:
        text = '隐藏文件名称:' + name + '\n你的key为:' + str(base_key)[1:] + '(不含单引号)'
        w.write(text)


if __name__ == '__main__':
    encipherment()

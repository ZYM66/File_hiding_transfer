import base64
import random
import wave


def encipherment():
    name_file = input('请输入要加密文件的路径:')
    name_carrier = input('请输入文件载体路径:')
    name = input('请输入处理后文件的名字:')
    infomap = {}
    gap = random.randint(4, 7)

    with open(name_file, 'rb') as f:
        data = f.read()
        data_len = len(data)
        txt_data = bytearray(data)

    with wave.open(name_carrier, 'rb') as f:
        infomap['channels'] = f.getnchannels()
        infomap['sampwidth'] = f.getsampwidth()
        infomap['framerate'] = f.getframerate()
        wave_data = bytearray(f.readframes(-1))

    infolist = bytes((str(data_len) + 'A' + str(infomap['channels']) + str(infomap['sampwidth']) + str(
        infomap['framerate']) + str(gap)).encode('utf-8'))
    base_key = base64.b64encode(infolist)

    with wave.open(name + '.wav', 'wb') as w:
        w.setnchannels(infomap['channels'])
        w.setsampwidth(infomap['sampwidth'])
        w.setframerate(infomap['framerate'])
        try:
            for i in range(data_len):
                wave_data[i * gap] = data[i]
            w.writeframes(wave_data)
            print('你的key:' + str(base_key)[1:])
        except:
            print('错误，请换更大的载体文件！')


if __name__ == '__main__':
    encipherment()

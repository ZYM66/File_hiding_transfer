import wave
import base64


def decode():
    encode_file = input('请输入加密后的文件地址:')
    base_key = bytes(input('请输入该文件的key:').encode())
    infomap = {}
    extract_data = []

    base_key = base64.b64decode(base_key)
    info = str(base_key.decode())

    place_A = info.index('A')
    infomap['len'] = int(info[0:place_A])
    infomap['channels'] = info[place_A + 1:place_A + 2]
    infomap['sampwidth'] = info[place_A + 2:place_A + 3]
    infomap['framerate'] = info[place_A + 3:-1]
    infomap['gap'] = int(info[-1])

    with wave.open(encode_file, 'rb') as f:
        data = f.readframes(-1)


    with open('./output/提取文件.txt', 'wb') as f:
        for i in range(infomap['len']):
            extract_data.append(data[i * infomap['gap']])
        f.write(bytearray(extract_data))
    print('已经提取到output文件夹内')

if __name__ == '__main__':
    decode()

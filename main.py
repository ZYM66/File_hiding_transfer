import encipherment
import decode

print("欢迎使用文件隐藏工具".center(50,"*"))
print('1.隐藏文件')
print('2.提取文件')
choose = input('请输入需要进入的模式:')
if choose == '1':
    encipherment.encipherment()
if choose == '2':
    decode.decode()
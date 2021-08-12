import os
# 不需要用到ffmpeg的依赖，但是需要有ffmpeg可执行文件
start_dir = os.getcwd()
# 获取原始路径盘符
start_dir = start_dir + "\\"
# 你的python路径放在上面
translateScriptPrefix = start_dir + "\\ffmpeg.exe -i "
# 路径预配置，写入cmd

def convert_to_mp4(originfile):
    arrName = []
    arrName = os.path.splitext(originfile)
    out_name = arrName[0] + "1.mp4"
    # translate = translateScriptPrefix + start_dir + "\\HR数据分析\\" + originfile + " " + start_dir + "\\HR数据分析\\"+ out_name
    translate = translateScriptPrefix + start_dir + "\\" + originfile + " " + start_dir + "\\" + out_name
    print(translate)
    os.system(translate)
    print("Finished converting {}".format(out_name))

def trans_files():
    for filepath,dirnames,filenames in os.walk(start_dir):
        for filename in filenames:
            if filename.endswith('.ts'):
                print("Found file: %s" % filename)
                convert_to_mp4(filename)

# def get_files():
#     for filepath,dirnames,filenames in os.walk(start_dir):
#         for filename in filenames:
#             print(os.path.join(filepath,filename))
#             # 遍历文件夹内文件 https://blog.csdn.net/qq_39721240/article/details/90704223
trans_files()
# get_files()

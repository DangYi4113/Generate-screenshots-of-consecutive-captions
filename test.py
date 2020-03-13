import os
from PIL import Image

folderName = input("\n请输入各截图所在文件夹的名称。\n如果和这个exe程序不在同一个大文件夹下，需要输入完整的路径\n按回车键结束\n")
h_start = int(input("\n请输入每张图片中，从上到下，字幕上边缘的像素最小值\n按回车键结束\n"))
h_end = int(input("\n请输入每张图片中，从上到下，字幕下边缘的像素最大值\n按回车键结束\n"))
height_text = h_end-h_start

filenames = os.listdir(folderName)
image0 = Image.open('%s/%s' %(folderName,filenames[0]))
width, height = image0.size

results = Image.new(image0.mode,(width, h_end+(len(filenames)-1)*height_text))

results.paste(image0, box = (0,0))

for i in range(1,len(filenames)):
    imagei = Image.open('%s/%s' %(folderName,filenames[i]))
    ng = imagei.crop((0,h_start,width,h_end))
    results.paste(ng, box = (0,h_end+(i-1)*height_text))
    
results.save('results.jpg')

print('结果已输出至同一文件夹下的results.jpg文件里')

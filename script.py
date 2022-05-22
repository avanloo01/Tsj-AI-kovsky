
# import os
#
directory = r'C:\Users\arthu\Documents\School\Onderzoekscompetenties\6e\Training'
# c=222
# for i in range(222,341):
#     print(i)
#     os.rename("img" + str(i-221) + '.png', 'img' + str(i) + '.png')

# import pyautogui as pyg
# import time
#
# pyg.click(x=200, y=200, clicks=1, interval=0.5, button='left')
# pyg.typewrite("-p " + directory)
# pyg.press("enter")
# time.sleep(3)
#
# for file in range(217, 341):
#     pyg.typewrite(f"load img{file}.png")
#     pyg.press("enter")
#     pyg.typewrite("-t 250")
#     pyg.press("enter")
#     pyg.typewrite("save")
#     pyg.press('enter')

import os
from PIL import Image

# for num in range(2, 6):
#     for file in os.listdir(os.path.join(directory, str(num))):
#         os.system("cd " + os.path.join(directory, str(num)))
#         # print(os.path.join(directory, str(num), file))
#         os.system("split-image " + os.path.join(directory, str(num), file) + " 1 " + str(num))
#         print(file + " OK")
c = 1
for file in os.listdir(os.path.join(directory, 'Goed')):
    if file.endswith(".png"):
        img = Image.open(os.path.join(directory, 'Goed', file ))
        img = img.resize((512, 512))
        img.save(os.path.join(directory, '512', str(c) + ".png"))
        print(c)
        c += 1
# import os
# c = 1652
# for file in os.listdir(os.path.join(directory)):
#     os.rename(os.path.join(directory, file), os.path.join(directory, str(c) + ".png") )


# lightweight_gan --data ./Goed --batch-size 10 --gradient-accumulate-every 4 --evaluate-every 5 --num-image-tiles 10 --num-train-steps 200000 --save-every 1000 --name Tschaikovsky --image-size 128 --greyscale

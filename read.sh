# !bin/bash
python3 read.py
grep '唐诗' -rl 2.txt | xargs sed -i "s: #     唐诗:##宋词##:g" #查找替换
cp 2.txt 3.txt   # 生成一个新的文件

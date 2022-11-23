import ffmpeg 
import os
 
# 入力 
stream = ffmpeg.input("PXL_20220820_122127489.TS_2.mp4") 
# 出力 
stream = ffmpeg.output(stream, "abi_bark.mp3") 
# 実行
ffmpeg.run(stream)
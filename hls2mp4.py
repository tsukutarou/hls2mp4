import os
import glob
import shutil
import subprocess


def hls2mp4(filePath):

     #ファイルのあるディレクトリに移動
     os.chdir(os.path.dirname(__file__))

     #ファイル名の処理
     src = filePath
     fileName = os.path.basename(filePath)
     savePath = os.path.splitext(os.path.dirname(filePath)+f"/{fileName}")[0]+".mp4"
     tempDir = os.path.dirname(filePath)+"/temp"
     dst,ext = os.path.splitext(os.path.join(tempDir+"/"+fileName))

     print(src,dst,ext)

     #.hlsファイルのときのみ処理を実行
     if not ext==".hls":
         print("Error: This is not \".hls\" file.")
         return
     else:
         if not os.path.exists(tempDir):
             os.mkdir(tempDir)
         dst = dst+".zip"
         shutil.copy(src,dst)
         shutil.unpack_archive(dst,tempDir)

         print(tempDir)

         index_m3u8 = glob.glob(f"{tempDir}/*.m3u8")[0]
         
         print(index_m3u8)
         
         cmd = f"./ffmpeg/ffmpeg.exe -allowed_extensions ALL -i \"{index_m3u8}\" -c copy \"{savePath}\""
         subprocess.run(cmd)

         shutil.rmtree(tempDir)


if __name__=="__main__":

     #変換したい.hlsファイルのパス
     hlsPath = "D://Music//niconico//【ミクリンGUMI】神のまにまに【オリジナル】 - ニコニコ動画.hls"

     #実行
     hls2mp4(hlsPath)
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

     #入力が.hlsファイルのときのみ処理を実行
     if not ext==".hls":
         print("Error: This is not \".hls\" file.")
         return
     else:
         if not os.path.exists(tempDir):
             os.mkdir(tempDir)

         try:
             #.m3u8ファイルと.tsファイル群を展開
             dst = dst+".zip"
             shutil.copy(src,dst)
             shutil.unpack_archive(dst,tempDir)

             #変換を実行
             index_m3u8 = glob.glob(f"{tempDir}/*.m3u8")[0]
             cmd = f"./ffmpeg/ffmpeg.exe -allowed_extensions ALL -y -i \"{index_m3u8}\" -loglevel fatal -c copy \"{savePath}\""
             subprocess.run(cmd)

             #一時ファイルの削除
             shutil.rmtree(tempDir)
         finally:
             messageFine = f"""
     {src}
             |
             V
     {savePath}

変換は正常に完了しました。
             """
             print(messageFine)



if __name__=="__main__":

     #変換したい.hlsファイルのパス
     hlsPath = "ここパスを記述"

     #実行
     hls2mp4(hlsPath)
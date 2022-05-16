# hls2mp4

ClipboxやKingboxなどのアプリケーションでダウンロードした動画は、拡張子が「.hls」となってしまい、そのままではPCなどで再生できません。

そういった問題を解決するために、<b>パスを与えて実行するだけで.hlsを.mp4に変換するpythonプログラム</b>です。（無損失のはず）

# 使い方などはこちら

<a href="">こちら</a>

# ffmpegについて

このプログラムを実行するためには、ffmpegというフリーソフトが必要となります。

<a href="https://github.com/GyanD/codexffmpeg/releases">こちら</a>から`ffmpeg-(バージョン)-full_build.zip`をダウンロード・解凍し、`bin`内の`ffmpeg.exe`をコピーして`hls2mp4/ffmpeg/ffmpeg.exe`となるように配置してください。

# .mp4動画の上書き保存について

変換元の.hlsのあるディレクトリに既に同じ名前で拡張子違いの.mp4動画がある場合、<b>その動画ファイルが上書きされる形で変換後の.mp4ファイルが保存されます。</b>

上書きしたくない場合はあらかじめ名前を変えるなどして対処してください。

***

## 製作者

<b>Tsukutarou / つくたろう</b>

Email: email[at]tsukutarou.net

Blog: <a href="https://www.tsukutarou.net">https://www.tsukutarou.net</a>
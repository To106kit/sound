import dlYoutube.dlyoutubeAsmp3 as dlyoutubeasmp3
# import mp3ToMidi.mp3tomidi as mp3tomidi
import time
import getmp4Name.getmp4name as getmp4name


# 時間計測開始
time_sta = time.time()

# 初期化
t_title = ""

# 変換対象のyoutubeのurlに変更
t_tagUrl_list = [
                    "https://www.youtube.com/watch?v=PiCwEMCwa_U",
                    "https://www.youtube.com/watch?v=z3mxhgN7vUQ",
                    "https://www.youtube.com/watch?v=zkZARKFuzNQ",
                    "https://www.youtube.com/watch?v=4tlUwgtgdZA",
                    "https://www.youtube.com/watch?v=JGgULncKDBM",
                    "https://www.youtube.com/watch?v=Z6ji6kls_OA",
                    "https://www.youtube.com/watch?v=zHdzB9RtpD8",
                    "https://www.youtube.com/watch?v=fwzRR6Bsro4",
                    "https://www.youtube.com/watch?v=-2q3-6zqr2k",
                    "https://www.youtube.com/watch?v=mwTmvdIeYnE",
                    "https://www.youtube.com/watch?v=DC6JppqHkaM",
                    "https://www.youtube.com/watch?v=3LVAmMxICoA",
                    "https://www.youtube.com/watch?v=ODysC7SM_Yk",
                    "https://www.youtube.com/watch?v=CnPtuwiswIs",
                    "https://www.youtube.com/watch?v=FRDxf2nN5Xk",
                    "https://www.youtube.com/watch?v=OMhVQLBNyGs",
                    "https://www.youtube.com/watch?v=Dm2O_W6Rrss",
                    "https://www.youtube.com/watch?v=hYF438PiuPI",
                    "https://www.youtube.com/watch?v=2By3feOVw20",
                    "https://www.youtube.com/watch?v=e9RVh2bXA8M",
                    "https://www.youtube.com/watch?v=s1cgEj5JowM",
                    "https://www.youtube.com/watch?v=H77n6UOxIyI",
                    "https://www.youtube.com/watch?v=M6gcoDN9jBc",
                    "https://www.youtube.com/watch?v=hm1na9R2uYA",
                    "https://www.youtube.com/watch?v=BOrdMrh4uKg",
                    "https://www.youtube.com/watch?v=iVstp5Ozw2o",
                    "https://www.youtube.com/watch?v=su5o63BnOUM",
                    "https://www.youtube.com/watch?v=aRDURmIYBZ4",
                    "https://www.youtube.com/watch?v=JAN8BIagE8Q",
                    "https://www.youtube.com/watch?v=LKMw0hBDBUw",
                    "https://www.youtube.com/watch?v=S__5u0vlXkI",
                    "https://www.youtube.com/watch?v=g4_nRpHotMo",
                    "https://www.youtube.com/watch?v=CPqroobt0SA",
                    "https://www.youtube.com/watch?v=Y8HeOA95UzQ",
                    "https://www.youtube.com/watch?v=L-Bzhpm8h0o",
                    "https://www.youtube.com/watch?v=JBmzU_qn_G8",
                    "https://www.youtube.com/watch?v=CTDcqAebtF0",
                    "https://www.youtube.com/watch?v=gc0_Acq8dV4",
                    "https://www.youtube.com/watch?v=YeBt1NhOJtA",
                    "https://www.youtube.com/watch?v=cAVnxFszvKo",
                    "https://www.youtube.com/watch?v=EsflrwOsYoE",
                    "https://www.youtube.com/watch?v=C66yySFa48A",
                    "https://www.youtube.com/watch?v=jddS5q0RFpY",
                    "https://www.youtube.com/watch?v=nGZXxzN4-Pc",
                    "https://www.youtube.com/watch?v=VjktdR8Dhbc",
                    "https://www.youtube.com/watch?v=DuMqFknYHBs",
                    "https://www.youtube.com/watch?v=ReCnlwVZj1M",
                    "https://www.youtube.com/watch?v=hN5MBlGv2Ac",
                    "https://www.youtube.com/watch?v=8lx0vLTH_yg",
                    "https://www.youtube.com/watch?v=IiqfKF9BlcI",
                    "https://www.youtube.com/watch?v=cADu9rtlZGQ",
                    "https://www.youtube.com/watch?v=2I25AFSBm2g",
                    "https://www.youtube.com/watch?v=123BD9U5FIk",
                    "https://www.youtube.com/watch?v=scV4N5tkWbU",
                    "https://www.youtube.com/watch?v=4BZMWcCj_98",
                    "https://www.youtube.com/watch?v=HZZk2Mq_yjA",
                    "https://www.youtube.com/watch?v=J3_IdDAr-dk",
                    "https://www.youtube.com/watch?v=mZkeNK0RQ04",
                    "https://www.youtube.com/watch?v=8YIBaNKhwf8",
                    "https://www.youtube.com/watch?v=dIqN5XgIhFQ",
                    "https://www.youtube.com/watch?v=YCLMWDa58So",
                    "https://www.youtube.com/watch?v=H6rM6KY2sCQ",
                    "https://www.youtube.com/watch?v=PCIGe083SY0",
                    "https://www.youtube.com/watch?v=ZsNCAtQcdas",
                    "https://www.youtube.com/watch?v=gw73B2PD9Jo",
                    # "",
                    # "",
                    # "",
                    # "",
                    # "",
                ]


for t_tagUrl in t_tagUrl_list:
# urlが示す動画の名前を取得
    try:
        t_title = getmp4name.getmp4name(t_tagUrl)
        print(t_title)
    except Exception as e:
        print(t_tagUrl, e.args)

# youtubeをmp3としてダウンロード
    t_mp3path = dlyoutubeasmp3.dlyoutubeasmp3(t_tagUrl, t_title)

# demucs
# demucsgui.test_wrapper()

# mp3をmidiに変換
# mp3tomidi.mp3tomidi(t_mp3path)

# 時間計測終了
time_end = time.time()

# 経過時間（秒）
tim = time_end- time_sta

print(tim)
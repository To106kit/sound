import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
import numpy as np
import sys

def sendgmail(a_exec_time, a_synth_sound):
    # 初期化
    ## TODO: とりあえず動く要改善################################
    t_synth_sound_str = a_synth_sound
    t_synth_sound_str_strip = t_synth_sound_str.strip("'")
    t_spllit = t_synth_sound_str_strip.split('\\n')
    t_synth_sound_for_print = "\n".join(t_spllit)
    ## TODO: とりあえず動く要改善################################

    # メール送信必要項目
    sendAddress = 't.to106ki@gmail.com' #自分のメールアドレス
    password = 'eqyezsefmxmuwqux' #パスワード
    subject = '【実行完了】AutoBGM'
    bodyText = f'''AutoBGMの定期実行タスクが完了しました。\n実行時間は{a_exec_time}[min]でした。\n 以下のファイルを自動BGM合成完了しました。\n {t_synth_sound_for_print} '''
    fromAddress = 'AutoBGM'
    toAddress = 't.to106ki@gmail.com'

    # SMTPサーバに接続
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpobj.starttls()
    smtpobj.login(sendAddress, password)

    # メール作成
    msg = MIMEText(bodyText)
    msg['Subject'] = subject
    msg['From'] = fromAddress
    msg['To'] = toAddress
    msg['Date'] = formatdate()

    # 作成したメールを送信
    smtpobj.send_message(msg)
    smtpobj.close()

    print("mail was send.")

if __name__ == "__main__":
    import sys
    sendgmail(sys.argv[1],sys.argv[2])
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

def sendgmail():

    sendAddress = 't.to106ki@gmail.com' #自分のメールアドレス
    password = 'to106kita9ma' #パスワード

    subject = '【実行完了】AutoBGM'
    bodyText = 'AutoBGMの定期実行タスクが完了しました。'
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
    sendgmail()
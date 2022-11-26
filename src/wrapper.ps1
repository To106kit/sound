$StartTime = Get-Date

# download mp3 from youtube
python -u "d:\11_github\sound\src\main.py"
# separate mp3 by demucs
python -u "d:\11_github\sound\src\DemucsGui\GUI\GuiMain.py"
# synthesis wav by pydub
$synth_sound = python -u "d:\11_github\sound\src\synthesis\synthesyswab.py"

$StopTime = Get-Date
Write-Host ($StopTime - $StartTime).TotalMinutes
# AutoBGM実行トータル時間
$num = ($StopTime - $StartTime).TotalMinutes

# 小数点第四位を四捨五入して第一位までの値とする。
$mailarg = [Math]::Round($num, 1, [MidpointRounding]::AwayFromZero);
# synthesis wav by pydub
python -u "d:\11_github\sound\src\sendgmail_pack\sendgmail_mod.py" $mailarg $synth_sound

# test#3
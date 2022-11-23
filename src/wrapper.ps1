$StartTime = Get-Date

# download mp3 from youtube
python -u "d:\11_github\sound\src\main.py"
# separate mp3 by demucs
python -u "d:\11_github\sound\src\DemucsGui\GUI\GuiMain.py"
# synthesis wav by pydub
python -u "d:\11_github\sound\src\synthesis\synthesyswab.py"

$StopTime = Get-Date
Write-Host ($StopTime - $StartTime).TotalSeconds

# test
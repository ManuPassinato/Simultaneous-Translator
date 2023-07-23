import os
# os.system("start cmd /K .\conf.bat")

from whisper_mic.whisper_mic import WhisperMic

mic = WhisperMic()
result = mic.listen_loop()
print(result)
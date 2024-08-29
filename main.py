import requests
import random
import threading
from source.pranks.voicemod import voicemod
from source.pranks.tutorialsploit import tutsploit
from source.pranks.test import test

threads = []
for _ in range(30):
    threadVoicemod = threading.Thread(target=voicemod)
    threadTutorialSploit = threading.Thread(target=tutsploit)
    threadTest = threading.Thread(target=test)

    threads.append(threadVoicemod)
    threads.append(threadTutorialSploit)
    threads.append(threadTest)
    

for t in threads:
    t.start()

for t in threads:
    t.join()

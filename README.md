# bibot

TODO:
- list all packages installed
- create a requirements.txt

Power Button inspired from 
https://howchoo.com/g/mwnlytk3zmm/how-to-add-a-power-button-to-your-raspberry-pi

Power Led 
https://howchoo.com/g/ytzjyzy4m2e/build-a-simple-raspberry-pi-led-power-status-indicator
enable_uart : https://www.raspberrypi.org/documentation/configuration/device-tree.md#part4.6

ReSpeaker docs
https://wiki.seeedstudio.com/ReSpeaker_2_Mics_Pi_HAT/
https://pinout.xyz/pinout/respeaker_2_mics_phat

Sound card test
> arecord -f cd -Dhw:1 | aplay -Dhw:1

Snowboy (End of life 31/12/2020)
Yoco's model https://snowboy.kitt.ai/hotword/50459
install:
https://github.com/kitt-ai/snowboy#ubunturaspberry-pipine64nvidia-jetson-tx1nvidia-jetson-tx2
inutile de compiler Swig, apt-get install swig fonctionne
par contre, il faut compiler la lib snowboy pour python (repo/swig/Pytohn3/make) et la copier dans le projet (voir https://github.com/Kitt-AI/snowboy/issues/101)
pip3 pyaudio

Google Assistant SDK
https://developers.google.com/assistant/sdk/guides/service/python/embed/run-sample
Project-id : bibot
Device id : bibot-182de-bibou-pi-zero-f04bqq

Python3 virtual env with google assistant SDK
> source python3/bin/activate
> (python3) googlesamples-assistant-pushtotalk --project-id bibot --device-model-id bibot-182de-bibou-pi-zero-f04bqq


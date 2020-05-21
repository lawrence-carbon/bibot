import snowboydecoder
import sys
import signal
from light import Light
from bibot_assistant import BibotAssistant

yoco_model = "yoco.pmdl"
device_model_id = "bibot-182de-bibou-pi-zero-f04bqq"
device_id = "1abf8784-834b-11ea-869f-b827eb95caa4"
credentials_file = "credentials.json"
led = Light(15)
assistant = BibotAssistant(device_model_id, device_id, credentials_file, None)
interrupted = False

def signal_handler(signal, frame):
    global interrupted
    interrupted = True

def interrupt_callback():
    global interrupted
    return interrupted

def trigger_assistant():
    led.blink()
    assistant.assist()


def main():

    signal.signal(signal.SIGINT, signal_handler)
    detector = snowboydecoder.HotwordDetector(yoco_model, sensitivity=0.5)
    print('Listening... Press Ctrl+C to exit')
    detector.start(detected_callback=led.blink,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

    detector.terminate()

if __name__ == '__main__':
    main()

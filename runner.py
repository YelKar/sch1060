import time
import traceback
from threading import Thread


def start():
    thread = Thread(target=catch)
    thread.start()


def catch():
    try:
        from app import app as application
        application.run(host="0.0.0.0", port=2222)
    except Exception:
        traceback.print_exc()
        time.sleep(10)
        start()


if __name__ == '__main__':
    from app import app as application
    application.run(host="0.0.0.0", port=2222)

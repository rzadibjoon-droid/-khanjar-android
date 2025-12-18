
from plyer import notification
def notify(title, msg):
    try:
        notification.notify(title=title, message=msg)
    except:
        pass

from celery import Celery
from datetime import datetime, timedelta
import sqlite3
import traceback
import json
from hello import connect_db

app = Celery('notification_tasks', broker='redis://localhost:6379/0')

def send_google_chat_notification(email):
    # Implement your notification sending logic here
    return f"Notification sent to {email}"

@app.task
def check_login_status():
    try:
        conn = connect_db()
        cursor = conn.execute("SELECT * FROM userDetails")
        rows = cursor.fetchall()

        current_time = datetime.now()
        threshold = timedelta(hours=24)

        for row in rows:
            uID, email, password, loginTime = row
            login_time = datetime.strptime(loginTime, '%Y-%m-%d %H:%M:%S')

            time_difference = current_time - login_time

            if time_difference > threshold:
                # Send notification asynchronously using Celery
                send_google_chat_notification.delay(email)
    except Exception as e:
        traceback.print_exc()

if __name__ == "__main__":
    app.conf.beat_schedule = {
        'check_login_status': {
            'task': 'your_module.check_login_status',
            'schedule': timedelta(hours=24),
        },
    }
    app.conf.timezone = 'UTC'

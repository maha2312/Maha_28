from flask import Flask
import os
from datetime import datetime
import subprocess

app = Flask(__name__)

def get_top_output():
    # Get 'top' command output
    try:
        result = subprocess.run(['top', '-b', '-n', '1'], stdout=subprocess.PIPE, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

@app.route('/htop')
def htop():
    # Get system username
    username = os.getenv('USER', 'Unknown')
    # Get server time in IST
    ist_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S') + ' IST'
    # Get top command output
    top_output = get_top_output()

    # Return the response
    return f"""
    <h1>System Information</h1>
    <p><strong>Name:</strong> Your Full Name</p>
    <p><strong>Username:</strong> {username}</p>
    <p><strong>Server Time:</strong> {ist_time}</p>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)

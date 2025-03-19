from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    
    full_name = "Sahu-Sonali" 

    
    username = os.getlogin()

  
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1'], text=True)
    except subprocess.CalledProcessError as e:
        top_output = f"Error running top command: {e}"

 
    output = f"""
    <h1>System Information</h1>
    <p><b>Full Name:</b> {full_name}</p>
    <p><b>Username:</b> {username}</p>
    <p><b>Server Time (IST):</b> {server_time}</p>
    <h2>Top Command Output</h2>
    <pre>{top_output}</pre>
    """

    return output

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
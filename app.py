from flask import Flask, render_template, jsonify
import platform, time

app = Flask(__name__)
START_TIME = time.time()

@app.get('/')
def index():
    return render_template('index.html')

@app.get('/api/status')
def status():
    return jsonify({
        'ok': True,
        'python': platform.python_version(),
        'message': 'Python backend online'
    })

@app.get('/api/system-info')
def system_info():
    return jsonify({
        'system': platform.system(),
        'version': platform.version(),
        'architecture': platform.architecture()[0],
        'node': platform.node(),
        'processor': platform.processor(),
        'uptime_seconds': round(time.time() - START_TIME, 1)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

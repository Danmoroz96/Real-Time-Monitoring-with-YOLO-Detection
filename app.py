from flask import Flask, Response
import cv2

app = Flask(__name__)
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    raise RuntimeError("Could not open webcam.")

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break

        ret, buffer = cv2.imencode('.jpg', frame)
        if not ret:
            continue

        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Home Monitoring Stream</title>
        </head>
        <body>
            <h2>Live Camera Stream</h2>
            <img src="/video_feed" width="640">
        </body>
    </html>
    """

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
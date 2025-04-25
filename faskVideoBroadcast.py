from flask import Flask, Response, render_template_string
import cv2

app = Flask(__name__)

# Replace with your phone's IP Webcam stream URL
PHONE_CAM_URL = "https://random.ngrok-free.app/video"


def generate_frames():
    cap = cv2.VideoCapture(PHONE_CAM_URL)
    if not cap.isOpened():
        print("❌ ERROR: Cannot open video stream!")
        return

    while True:
        success, frame = cap.read()
        if not success:
            print("❌ ERROR: No frame received!")
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# Route for the video feed
@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Route for the main page to display the video
@app.route('/')
def index():
    return render_template_string("""
        <html>
        <head>
            <title>Live Video Feed</title>
        </head>
        <body>
            <h1>Live Video Stream</h1>
            <img src="{{ url_for('video_feed') }}" width="80%">
        </body>
        </html>
    """)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

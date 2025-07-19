# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required

# # Create your views here.

# @login_required(login_url="/Accounts/Login")
# def object(request):
#     return render(request, "objec/object.html")

import cv2
import numpy as np
from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Global VideoCapture object (single camera instance)
cap = cv2.VideoCapture(0)

@login_required(login_url="/Accounts/Login")
def object(request):
    return render(request, "objec/object.html")


# Generator for normal webcam frames
def generate_original():
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        _, jpeg = cv2.imencode('.jpg', frame)
        frame_bytes = jpeg.tobytes()
        yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n\r\n')


# Generator for simulated (color-filtered) frames
def generate_simulated(mode):
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if mode == "red":
            # Highlight red color
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            lower1 = np.array([0, 120, 70])
            upper1 = np.array([10, 255, 255])
            lower2 = np.array([170, 120, 70])
            upper2 = np.array([180, 255, 255])
            mask1 = cv2.inRange(hsv, lower1, upper1)
            mask2 = cv2.inRange(hsv, lower2, upper2)
            mask = cv2.bitwise_or(mask1, mask2)
            frame = cv2.bitwise_and(frame, frame, mask=mask)

        elif mode == "gray":
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

        # Add more modes as needed...

        _, jpeg = cv2.imencode('.jpg', frame)
        frame_bytes = jpeg.tobytes()
        yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n\r\n')


# Stream the original webcam feed
@login_required(login_url="/Accounts/Login")
def original_feed(request):
    return StreamingHttpResponse(generate_original(),
                                content_type='multipart/x-mixed-replace; boundary=frame')


# Stream the simulated feed with selected mode
@login_required(login_url="/Accounts/Login")
def simulated_feed(request):
    mode = request.GET.get("mode", "none")
    return StreamingHttpResponse(generate_simulated(mode),
                                content_type='multipart/x-mixed-replace; boundary=frame')

def video_feed(request):
    return StreamingHttpResponse(generate_original(), content_type='multipart/x-mixed-replace; boundary=frame')

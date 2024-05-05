from django.shortcuts import render
from django.http import JsonResponse, StreamingHttpResponse
from django.views.decorators import gzip

from cart.bar_scan import VideoCamera

# Models import 
from cart_data.models import ScannedItem, ItemData

def home_page(request):
    return render(request, "index.html")

# Camera Display Page
def camera(request):    
    global cam 
    cam = VideoCamera()   
    return render(request, 'camera.html')



# Camera Streaming Logic
@gzip.gzip_page   
def cameraView(request):   
    stat = False
    global cam
    stream = StreamingHttpResponse(gen(request, cam, stat), content_type = "multipart/x-mixed-replace;boundary=frame")
       
    
    return stream



def gen(request, camera, stat):
    
    while not stat:
        frame, stat, barcode_data = camera.get_frame()
        if stat:
            if ItemData.objects.filter(bar_data = barcode_data).exists():
                # Add user later
                db = ScannedItem(scanned_item = barcode_data)
                db.save()
            else:
                db = ScannedItem(scanned_item = "Dont exists") 
                db.save()
            return
        yield (b'--frame \r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')



def offCamera(request):
    global cam 
    cam.release_camera()
    return JsonResponse({"res" : "Camera Off"}) 
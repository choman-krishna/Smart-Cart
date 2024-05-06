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

def updateScanned(request):
    if request.method == "GET":
        # Get the last scanned item from the database
        scanned_db = ScannedItem.objects.last()

        # Initialize default values
        item_name = "Dont exists"
        item_price = -999
        item_image_url = ""

        # If a scanned item exists in the database
        if scanned_db and scanned_db.scanned_item != "Dont exists":
            # Get item data from ItemData model based on the barcode
            item_data = ItemData.objects.filter(bar_data=scanned_db.scanned_item).first()

            if item_data:
                item_name = item_data.item_name
                item_price = item_data.prize
                # Get the image URL
                item_image_url = "../static"+ item_data.item_img.url

        # Return JSON response
        return JsonResponse({
            "name": item_name,
            "price": item_price,
            "img": item_image_url
        })
    
def addToCart(request):
    # Reconsider this logic 
    scanned_db = ScannedItem.objects.last()
    scanned_db.in_cart = True
    scanned_db.save()
    add_lst = list(ItemData.objects.filter(bar_data = scanned_db.scanned_item).values())
    print(add_lst)
    return JsonResponse(add_lst[0])
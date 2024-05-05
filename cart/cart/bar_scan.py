import cv2
import threading
from pyzbar.pyzbar import decode


class VideoCamera(object):   
    
    
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        _, self.frame = self.video.read()
        self.bar_scanned = False

        self.scanned_otp = None    
        self.coupon_status = None

        self.thread_flag = True

        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()
        self.thread_flag = False

    def release_camera(self):
        self.video.release()
        self.thread_flag = False

    def get_frame(self):
        
        img = self.frame
        _, jpeg = cv2.imencode('.jpeg', img)


        # Qr Scanning Start


        
        self.bar_scanned = self.read_barcodes(self.frame)
                  

        # Qr Scanning ends

        
            


        return jpeg.tobytes(), self.bar_scanned 




    def read_barcodes(self, frame):
        # Convert the frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Decode barcodes
        barcodes = decode(gray_frame)
        if barcodes:
            for barcode in barcodes:
                # Get the barcode data and type
                barcode_data = barcode.data.decode("utf-8")
                barcode_type = barcode.type
                print(f"Found {barcode_type} \n barcode: {barcode_data}")    
                self.release_camera()
                self.bar_scanned = True
                return self.bar_scanned
    
    def update(self):
        try:
            while self.thread_flag:
                _, self.frame = self.video.read()
        except:
            pass
             



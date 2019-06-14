from pyzbar import pyzbar
import argparse
import cv2
import qrcode
import qrcode.image.svg
#from qrcode.image.pure import PymagingImage
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
##qr code reader 
def read_codes(img):
    barcodes = pyzbar.decode(img)
    content = []	
    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        code = {
            "type" : barcodeType,
            "data" : barcodeData
        }
        content.append(code)
    return content
print(read_codes(image)[0]['data'])
import qrcode
import json 
import qrcode.image.svg
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--id", required=True,
	help="the id of the user")
ap.add_argument("-c", "--color", required=True,
	help="color of the container")
ap.add_argument("-s", "--size", required=True,
	help="siqe of the container")
ap.add_argument("-f", "--format", required=True,
	help="the format of the generated image")
args = vars(ap.parse_args())
qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border = 4,
)
def generate_qr(id,color,size,image_format):
    ##image-format : png , bmp , jpeg , svg
    data = {}
    data['id'] = id
    data['color'] = str(color)
    data['size'] = str(size)
    json_data = json.dumps(data)
    title = "image."+str(image_format)
    if (image_format != 'svg'):
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image()
    else :
        factory = qrcode.image.svg.SvgPathImage
        img = qrcode.make(data, image_factory = factory)
    img.save(title)
id = str(args["id"])
color = str(args["color"])
size = str(args["size"])
format = str(args["format"])
generate_qr(id,color,size,format)
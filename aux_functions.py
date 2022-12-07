
def decode(encoded_img):
    aux_path = '/tmp/tmp.png'
    with open(aux_path, "wb") as f:
        f.write(base64.b64decode(encoded_file))
        f.close()

    out = cv2.imread(aux_path)

    return out


def encode(img):
    aux_path = '/tmp/tmp.png'
    cv2.imwrite(aux_path, img)

    with open(aux_path, "rb") as f:
        code = base64.b64encode(f.read())
        f.close()
    return code.decode("utf-8")


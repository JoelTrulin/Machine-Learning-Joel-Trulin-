import cv2
import json
import keras
import base64
import numpy as np
import tensorflow as tf
import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
os.environ["OPENCV_LOG_LEVEL"] = "SILENT"


physical_devices = tf.config.list_physical_devices('GPU')
for devices in physical_devices:
    tf.config.experimental.set_memory_growth(devices, True)


def faceid(Data, model_path, mode='base64'):
    """     Inputs
    Data: input in (str, tensor, ndarray)
    model_path: str
    when mode = base64
        Data should be a list of base64 which is in str
    when mode = video
        Data should be a str for video path
    when mode = Image
        Data should be in ndarray
        For single image as input the dim should be 3 eg (width, height, channel)
        For multiple image as input the dim should be 4 eg (batch, width, height, channel)
            Returns
    Dict with predicted label as key and list of Image, conf_scr, laplcn_scr
    """

    def variance_of_laplacian(image):
        return cv2.Laplacian(image, cv2.CV_64F).var()

    checkin = {0: "Left", 1: "Lower", 2: "Right", 3: "Smile", 4: "Upper"}

    """Preprocessing base64 image to tensors"""
    if mode == 'base64':
        Image_base64 = list(map(lambda u: u[1:], Data))
        Image_bytes = list(map(base64.b64decode, Image_base64))
        Images = list(map(tf.image.decode_image, Image_bytes))
        Images = list(map(lambda x: x.numpy(), Images))
        Images_resized = np.array(
            list(map(lambda x: cv2.resize(x, (768, 768)), Images)))

    elif mode == 'video':
        Images = list()
        cap = cv2.VideoCapture(Data)
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                break
            Images.append(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        Images_resized = np.array(
            list(map(lambda x: cv2.resize(x, (768, 768)), Images)))

    elif mode == 'Image':
        Images = np.expand_dims(Data, axis=0)
        res_img = cv2.resize(Data, (768, 768))
        res_img = cv2.cvtColor(res_img, cv2.COLOR_BGR2RGB)
        Images_resized = res_img.reshape(1, 768, 768, 3)

    if Images_resized.shape[0] > 1:
        laplcn_scr = list(map(variance_of_laplacian, Images_resized))
        laplcn_img = list(zip(Images_resized, laplcn_scr))
        laplcn_img = sorted(laplcn_img, key=lambda u: u[1], reverse=True)[:30]
        laplcn_scr = list(map(lambda u: u[1], laplcn_img))
        Images_resized = np.array(list(map(lambda u: u[0], laplcn_img)))

    """Inference"""
    try:
        pred_arr = model.predict(Images_resized, batch_size=20)
    except:
        model = keras.models.load_model(model_path)
        pred_arr = model.predict(Images_resized, batch_size=20)
    prediction = np.argmax(pred_arr, axis=1)

    prediction = list(map(lambda u: checkin[u], prediction))
    conf_scr = np.amax(pred_arr, axis=1)

    data = list(zip(prediction, Images, conf_scr, laplcn_scr))

    def select_frame(feat, category):
        feat = list(filter(lambda u: u[0] == category, feat))
        return sorted(feat, key=lambda u: u[2], reverse=True)[0]

    left = select_frame(data, 'Left')
    right = select_frame(data, 'Right')
    upper = select_frame(data, 'Upper')
    lower = select_frame(data, 'Lower')
    smile = select_frame(data, 'Smile')

   
    result = {'left': left[1:] if left is not None else None,
              'right': right[1:] if right is not None else None,
              'upper': upper[1:] if upper is not None else None,
              'lower': lower[1:] if lower is not None else None,
              'smile': smile[1:] if smile is not None else None}
    return result

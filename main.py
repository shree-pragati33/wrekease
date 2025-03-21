from inference_sdk import InferenceHTTPClient

CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="b6Tz6aloc8yeUAMSBBA2"
)
image = "https://dentshop.com/wp-content/uploads/2018/12/dent-removal-768x512.jpg"
result = CLIENT.infer(image, model_id="etiquetado-de-danos/1")
print("\n FIRST RESULT \n")
print(result)

result2 = CLIENT.infer(image, model_id="damage_severity/1")
print("\n SECOND RESULT \n")
print(result2)

result3 = CLIENT.infer(image, model_id="scratches-and-dents-detection-1/5")
print("\n THIRD RESULT \n")
print(result3)
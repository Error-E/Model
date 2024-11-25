from keras.models import load_model
from keras.preprocessing.image import load_img
import time
import numpy as np
import matplotlib.pyplot as plt
import gdown 
import pyscreenshot as ImageGrab
import matplotlib.pyplot as plt
from PIL import Image
import pyautogui as pag
from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaFileUpload
import tkinter as tk
import datetime

# url = 'https://drive.google.com/drive/folders/1GY-WwfF6IZrUqGCAbnzqMmkHG8kMiqAY'
# gdown.download_folder(url, quiet=True, use_cookies=False)



model = load_model('skibidi dop dop/Model/model_hero.h5')


class_labels = ['Batman', 'Spider-Man', 'captain America', 'hulk']  

root = tk.Tk()

def button_clicked():
    global root 
    root.quit()

button = tk.Button(root, 
                text="Start", 
                command=button_clicked,
                activebackground="blue", 
                activeforeground="white",
                anchor="center",
                bd=3,
                bg="lightgray",
                cursor="hand2",
                disabledforeground="gray",
                fg="black",
                font=("Arial", 12),
                height=2,
                highlightbackground="black",
                highlightcolor="green",
                highlightthickness=2,
                justify="center",
                overrelief="raised",
                padx=60,
                pady=20,
                width=15,
                wraplength=100)

button.pack(padx=100, pady=50)
while True :



    root.mainloop()



    print('--------------GAME START--------------')
    image = ImageGrab.grab(bbox=(900,300,1900,900))
    image.save('hi.png')
    image = load_img('hi.png', target_size=(224, 224))
    img = np.array(image)
    img = img / 255.0
    print(img.size)
    img = img.reshape(1, 224, 224, 3)


    predictions = model.predict(img)


    predicted_class = np.argmax(predictions, axis=1)[0]
    pred_list = [f"{i:.2f}%" for i in predictions[0]*100]

    print("Predicted Probabilities:", pred_list)
    print("Predicted Class:", class_labels[predicted_class])

    plt.figure(figsize=(15,10))
    plt.imshow(image)
    plt.title(f"Predicted Hero : {class_labels[predicted_class]} ({pred_list[np.argmax(predictions[0])]})" , size = 32)

    plt.axis('off')
    layer = 220


    plt.show()

    plt.pause(3)
    plt.close()

    now = time.ctime().split()
    credential = service_account.Credentials.from_service_account_file('one_two.json' , scopes = ['https://www.googleapis.com/auth/drive'])
    drive_service = build('drive', 'v3', credentials=credential)
    # file_metadata = {'name': 'test1.png', 'parents': [new_folder['id']]}
    media = MediaFileUpload('hi.png')
    file_metadata = {'name': f'{class_labels[predicted_class]}_{pred_list[np.argmax(predictions[0])]}_{now[0]}_{now[3]}_1.png', 'parents':['187FOYHlfa62ece4PP3iA6N4TYHDUFkXW']}
    img = drive_service.files().create(body = file_metadata , media_body = media).execute()

    print('DONE')
    
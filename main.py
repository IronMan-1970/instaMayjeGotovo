# -*- coding: utf-8 -*-
import PIL
from instagrapi import Client
import keyboard
import requests
from PIL import Image
from io import BytesIO
import os
import openai

cl = Client()
cl.login("nikaaksenina", "N52483156")
def download_photo(url, file_path):
    response = requests.get(url)
    if response.status_code == 200:
        try:
            img = Image.open(BytesIO(response.content))
            img.save(file_path)
            print("Photo downloaded successfully!")
        except PIL.UnidentifiedImageError:
            print("Failed to identify the image file.")
    else:
        print("Failed to download photo.")



print("Виберіть завдання:"
      "\n1 запостити іпсо"
      "\n2 закоментити іпсо"
      "\n3 залайкати іпсо")
menuChooser = input()

if menuChooser=='1':  # if key 'q' is pressed
            photo_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRipjtAVbwcoE8WC8332VHt2IjP7GPHB0A3jQ&usqp=CAU"
            save_path = "photos/photo.jpg"
            download_photo(photo_url, save_path)
            print(cl.account_info().dict())
            media = cl.photo_upload(
                "photos/photo.jpg",
                caption="Прем`єра 2023 року! Веселі пригоди! Венздей Адамс та Хаґі Ваґі у <<Грі в Кальмара>>! Найкрутіші герої, яких обожнюють діти. Танці, інтерактивний екшн! Світлове шоу та багато мультимедійних ефектів! Ви поринете у світ <<Гри в Кальмара>> Ближче побачите улюблених Хаґі Ваґі, Кісі Місі, Ванк Панк, Скарі Ларі! Познайомитесь з жахливо прикольною Венздей Адамс! Та нарешті преможите злодія!")


elif menuChooser=='2':
            media_id = cl.media_id(cl.media_pk_from_url(
                'https://www.instagram.com/p/CtyeYlHMIBa/?utm_source=ig_web_button_share_sheet&igshid=MzRlODBiNWFlZA=='))
            comment = cl.media_comment(media_id, "Запад нас слєваєт")
            comment.dict()


else:
    media_id = cl.media_id(cl.media_pk_from_url(
        'https://www.instagram.com/p/CtyeYlHMIBa/?utm_source=ig_web_button_share_sheet&igshid=MzRlODBiNWFlZA=='))
    like = cl.media_like(media_id)


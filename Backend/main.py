from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

app = FastAPI()

app.add_middleware(
CORSMiddleware,
allow_origins=["*"],
allow_credentials=False,
allow_methods=["*"],
allow_headers=["*"],
)

class MeetData(BaseModel):
    link: str

@app.get("/")
def home():
    return {"status": "Server Running"}

@app.post("/join")
def join_meet(data: MeetData):


    print("Received:", data.link)
    data.link=data.link.strip()

    if not data.link.startswith("http"):
        data.link = "https://" + data.link

    print("Opening:", data.link)

    options = webdriver.ChromeOptions()

    options.add_argument(r"--user-data-dir=C:\Users\91919\AppData\Local\Google\Chrome\User Data"
    )

    options.add_argument("--profile-directory=Default")

    driver = webdriver.Chrome(options=options)

    driver.get(data.link)


    

    time.sleep(10)

    all_buttons = driver.find_elements(By.TAG_NAME, "button")

    print("Total buttons:", len(all_buttons))

    for i, btn in enumerate(all_buttons):
        try:
            print(i, btn.text, btn.get_attribute("aria-label"))
        except Exception as e:
            print("Button Error:",e)

    return {
    "success": True
}



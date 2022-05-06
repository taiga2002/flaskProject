import os

data = """{
    "users": [
        {
            "_id": "714edd71-799d-4c25-bb55-9dba9b095ae9",
            "display name": "Dev Bali",
            "username": "devbali"
        },
        {
            "_id": "9e045d37-a955-4292-96f1-c726a5f9b073",
            "display name": "Rhythm Seth",
            "username": "socialguy"
        },
        {
            "_id": "f1e681cc-900e-4a07-9548-2e9b33b30fd7",
            "display name": "Charlie Shou",
            "username": "charlie"
        }
    ],
    "pleets": [
        {
            "_id": "45be55eb-27d1-4350-8d51-9ca2512229ea",
            "user_id": "714edd71-799d-4c25-bb55-9dba9b095ae9",
            "text": "Sample pleet",
            "datetime": 1642567497
        },
        {
            "_id": "ba20e7f2-66e0-4698-8ce6-2bae9652eacd",
            "user_id": "f1e681cc-900e-4a07-9548-2e9b33b30fd7",
            "text": "Working on the next assignment",
            "datetime": 1642565497
        },
        {
            "_id": "c98399c2-a788-4e4d-868f-1fc6f1649ca1",
            "user_id": "9e045d37-a955-4292-96f1-c726a5f9b073",
            "text": "मैं कमाठीपुरा राष्ट्रवादी हूं - I am a Kamathipura nationalist",
            "datetime": 1642567297
        }
    ]
}
"""

def reset():
    here = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.join(here, "../src/data.json")
    with open(data_file, "w", encoding="utf-8") as myfile:
        myfile.write(data)
    
if __name__ == "__main__":
    reset()
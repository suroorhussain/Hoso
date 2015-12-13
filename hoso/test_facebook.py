import facebook
import channels
import status_generator

access_token = """CAACEdEose0cBAB0PWEJSBFPQcnwGkgAFNF179SL31zDSX0iQSbE3v7ocY9M0DponZCvfGZAFa9a93IIWAPwGPJa32Mz99kxX6zHxbue0QnqM787jCed8ThTgKqz2V98GK3axVmFcPtUBOqRG9VcqCD455NSa7z9uxj9lTQs5ku6HmPQHJjEnvP8FvgjJb0T8eXmjfAxgZDZD"""
def test_facebook_broadcast():
    message1 = status_generator.generate_status()
    face_book = channels.fb(access_token, message1)
    face_book.broadcast()
    if face_book.status != "Feed limit reached. Please Try again after 24 hours":
        assert face_book.status == "Success"

def test_facebook_broadcast_expiry():
    access_token = """CAACEdEose0cBABzZAIKQQ4DTrbJS0sru0heXJwIm70abeOF705azqlgx9ulWi9GCHorQcFDIptDWSR1CVnb6hBDlDk1ZAUa1P4YPTAplTvPWzIPxAZAymEEtnjQGcYOG2KdZClZBaardPGKC153upC7w4C4KY5O3KgsqOj01CO4yrEV99rUBhMmjtrkZB8fEuYzsMa8idJ6gZDZD"""
    message2 = status_generator.generate_status()
    face_book = channels.fb(access_token, message2)
    face_book.broadcast()
    assert face_book.status == "Token expired"

def test_facebook_broadcast_duplicate_message():
    message3 = status_generator.generate_status()
    face_book = channels.fb(access_token, message3)
    face_book.broadcast()
    face_book.broadcast()
    if face_book.status != "Feed limit reached. Please Try again after 24 hours":
        assert face_book.status == "Duplicate message"

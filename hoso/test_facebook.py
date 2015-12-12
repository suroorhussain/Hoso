import facebook
import channels
import status_generator

access_token = """CAACEdEose0cBAFbU0YzCZBFNOAI2WCSfCUO7vgx73QuiCmzuLm07Gagv8SZCH5hk24n9JmBNpSRgN9y8dN8c1lcERO5njT2wQNshvxL8ycTj6qirONxdocwXmFnYEzpPKw950voDQqmzYzZCZAQRkLSIyEJBNts20jDcYcWe7AmAD2ZCUuB9QshOv4ZC0tRn3tNUxhkHmENwZDZD"""
def test_facebook_broadcast():
    message1 = status_generator.generate_status()
    face_book = channels.fb(access_token, message1)
    face_book.broadcast()
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
    assert face_book.status == "Duplicate message"

import channels
import facebook

def test_facebook_broadcast():
    try:
        access_token = """CAACEdEose0cBABzZAIKQQ4DTrbJS0sru0heXJwIm70abeOF705azqlgx9ulWi9GCHorQcFDIptDWSR1CVnb6hBDlDk1ZAUa1P4YPTAplTvPWzIPxAZAymEEtnjQGcYOG2KdZClZBaardPGKC153upC7w4C4KY5O3KgsqOj01CO4yrEV99rUBhMmjtrkZB8fEuYzsMa8idJ6gZDZD"""
        graph = facebook.GraphAPI(access_token)
        user = graph.get_object("me")
        message = "Testing facebook"
        face_book = channels.fb(access_token, message)
        result = face_book.broadcast()
        assert user["id"] in result["id"]
    except facebook.GraphAPIError as e:
        print e

def test_facebook_broadcast_expiry():
    access_token = """CAACEdEose0cBADHPW80j9CVomN5gjM1ssVmA6oqPm0UVUvAtOUBWz9mxfSYElFvhH5VFmS6osdYCWUYxTB9yNSdaG9E8q6VlGZA6LZAPAIccdqsbiCglJ5V7mZBWP0hXBGGg5WjDiltuZB8OCB4qs5DFWFzVsB2W3cWVCwwXfeq7OcLLDZCaYFbmINRhYXU4b7hGYBkdFAwZDZD"""
    graph = facebook.GraphAPI(access_token)
    try:
        user = graph.get_object("me")
    except facebook.GraphAPIError as e:
        assert 'expired' in e[0]

    

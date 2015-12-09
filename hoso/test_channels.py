import channels
import facebook

def test_facebook_broadcast():
    access_token = """CAACEdEose0cBADHPW80j9CVomN5gjM1ssVmA6oqPm0UVUvAtOUBWz9mxfSYElFvhH5VFmS6osdYCWUYxTB9yNSdaG9E8q6VlGZA6LZAPAIccdqsbiCglJ5V7mZBWP0hXBGGg5WjDiltuZB8OCB4qs5DFWFzVsB2W3cWVCwwXfeq7OcLLDZCaYFbmINRhYXU4b7hGYBkdFAwZDZD"""
    graph = facebook.GraphAPI(access_token)
    user = graph.get_object("me")
    message = "Testing facebook"
    face_book = channels.fb(access_token, message)
    result = face_book.broadcast()
    assert user["id"] in result["id"]

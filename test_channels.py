import channels
import facebook

def test_facebook_broadcast():
    access_token = """CAACEdEose0cBAH8DfFEcTzrYXrdBlsPwJZBwqjZBqZAHyjDBViaZANLPHs3xXEeE91uyww5MZAcuLoA2dzGmqwo49ubUd7VHPbMcmjMlmieBXYv9AOfU5D6bCeCnLUILCEktevMnyiELHZAQcbE1zKXVkjKZA3oFgV1F7YU49eB5ZAGF1TqwbEgK4w0qQIIeCMWf3mylueh7VQZDZD"""
    graph = facebook.GraphAPI(access_token)
    user = graph.get_object("me")
    message = "Testing facebook broadcast"
    face_book = channels.fb(access_token, message)
    result = fb.broadcast()
    assert user["id"] == result["id"]

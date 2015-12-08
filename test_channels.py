import channels
import facebook

def test_facebook_broadcast():
    access_token = """CAACEdEose0cBAPbYUGlhZCSygVMF7iNXMdmbxTZC70ZC8TB8DltmLRNoZC8fvTxR3nMp19KOk3geQy8cHzM9VSd2CUIOBcwmemSnE4V57LdvnSgdYs9Ri1haRnU7kiBPTgZBuJwS97CiQ4hYZC3hz6gk9oVJQZA1blmnxQD6RaC2bHHiSwxrwGdqiIyZCN7GZC15WjzTAzR0vJAZDZD"""
    graph = facebook.GraphAPI(access_token)
    user = graph.get_object("me")
    message = "Testing facebook"
    face_book = channels.fb(access_token, message)
    result = face_book.broadcast()
    assert user["id"] in result["id"]

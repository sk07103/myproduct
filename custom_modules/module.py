# requestされたurlのidとログイン中ユーザーのuser_idが一致していることをチェック
def check_userid(request, user_id):
    check_result = True
    url_id = int(request.path.split('/')[-1])
    if url_id != user_id:
        check_result = False
    return check_result

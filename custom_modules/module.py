import logging
from django.core.mail import EmailMultiAlternatives

logger = logging.getLogger('file')

# Amazon SESを使用してメールを送信
def send_email(subject, text_content, from_email, to_emails):
    logger.info('send_emailが呼び出されました。')
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to_emails])
    msg.send()

# requestされたurlのidとログイン中ユーザーのuser_idが一致していることをチェック
def check_userid(request, user_id):
    check_result = True
    url_id = int(request.path.split('/')[-1])
    if url_id != user_id:
        check_result = False
    return check_result

#
# import smtplib
#
# from email.mime.text import MIMEText
#
# from config import settings
#
# def send_email():
#     """Функция по отправке сообщений пользователю"""
#     file_content = 'test'
#
#     msg = MIMEText(file_content)
#     msg['Subject'] = 'test_test'
#     msg['From'] = settings.EMAIL_HOST_USER
#     msg['To'] = '2402as@gmail.com'
#
#     smtp_server = settings.EMAIL_HOST
#     smtp_port = settings.EMAIL_PORT
#     smtp_username = settings.EMAIL_HOST_USER
#     smtp_password = settings.EMAIL_HOST_PASSWORD
#
#     s = smtplib.SMTP_SSL(smtp_server, smtp_port)
#     s.login(smtp_username, smtp_password)
#
#     s.sendmail(settings.EMAIL_HOST_USER, ['2402as@gmail.com'], msg.as_string())
#     s.quit()
#
#
#
#
# if __name__== '__main__':
#     send_email()

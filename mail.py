import smtplib, json, time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr, getaddresses, formatdate, make_msgid


smtp_server = ""
smtp_port = 465
username = ""
password = ""

mail_html = "mail.html"
subject = "Community Invitation"

plain_text_content = "Hi username,\n\nYou're invited to join Black Stack Hub!\nDive into live projects, whether you're into backend, frontend, cloud, or just starting out. Build, grow, and innovate together with our vibrant community.\n\nJoin here: https://whatsapp.com/channel/0029Vay3l3F7dmejaNTEq82G \n\nBest regards,\nBlack Stack Hub"

with open(mail_html, "r") as file:
    html_content = file.read()

with open('data.json', 'r') as file:
    data = json.load(file)

def send_email(name, receiver_email):
    global html_content, plain_text_content
    htmlcontent = html_content.replace("username", name)
    plaintextcontent = plain_text_content.replace("username", name)
    msg = MIMEMultipart('alternative')
    msg["From"] = formataddr(("Black Stack Hub", username))
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg["Message-ID"] = make_msgid()
    msg["Date"] = formatdate(localtime=True)
    msg.attach(MIMEText(plaintextcontent, "plain"))
    msg.attach(MIMEText(htmlcontent, "html"))

    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(username, password)
            server.sendmail(username, receiver_email, msg.as_string())
        return True
    except Exception as e:
        return False

start_sending = False
sent_mail = 0
count_mail = 0
total_mail = 0

if sent_mail > 0 and sent_mail % 200 != 0:
    print("Sleeping for 1 hour 2 minutes...")
    time.sleep(3720)

for state, users in data.items():
    for user in users:
        count_mail += 1
        start_sending = True
        if start_sending:
            if send_email(user['username'], user['primary_link']):
                sent_mail += 1
            total_mail += 1
            print(f"Total sent: {sent_mail}/{total_mail} Username: {user['username']}, Primary Link: {user['primary_link']}")
            if sent_mail > 0 and sent_mail % 200 == 0:
                print("Sleeping for 1 hour 2 minutes...")
                time.sleep(3720)
        else:
            print('finding, not yet started: ', count_mail)

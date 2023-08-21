import time
from flask import Flask, render_template,send_from_directory,request,redirect
import os
import csv
import smtplib, ssl
from email.message import EmailMessage

app = Flask(__name__)
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "Anonymous"  # Enter your address
receiver_email = "omarkhalifa426@gmail.com"  # Enter receiver address
password = "knoqmuajdwblggkz"

msg = EmailMessage()

msg['Subject'] = "email"
msg['From'] = sender_email
msg['To'] = receiver_email

context = ssl.create_default_context()

# @app.route('/')
# def home():
#     return redirect("https://www.instagram.com/trendyfactory.eg", code=302)

@app.route('/')
def home():
    return render_template('index.html')





@app.route('/<string:page_name>')
def page(page_name):
    return render_template(page_name)


def csv_write(data):
    subject= data['subject']
    email= data['email']
    message = f'Email: {email} \n subject{subject}'
    msg.set_content(message, 'html')
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login('omarkhalifa226@gmail.com', password)
        server.send_message(msg, from_addr=sender_email, to_addrs=receiver_email)


@app.route('/submit',methods=['POST','GET'])
def submit():
    if request.method == 'POST':
        data = request.form.to_dict()
        csv_write(data)
        return redirect('/index.html')
    else:
        return "You havn't submit the data"




def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')

if '__main__' == __name__:
    app.run()




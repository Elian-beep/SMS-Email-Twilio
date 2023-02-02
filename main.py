from twilio.rest import Client

import sendgrid
import os
from sendgrid.helpers.mail import *

account_sid = ''
auth_token = ''
sendgrid_token = ''

case_name = input("Your name: ")
case_about = input("Your process: ")
msg = f"Olá, meu nome é {case_name} e estou participando do {case_about}"

# --------- (SMS) INRFORMAÇÕES DE CONTATO
client = Client(account_sid, auth_token)
from_number = '+13608003717'
numbers = ['+5592985878449', '+5592993169741']
# number_one = '+559791388065'
# number_two = '+559288192972'
# number_three = '+559293290162'

# --------- (EMAIL) INRFORMAÇÕES DO EMAIL
from_email = Email("elian.19batista@gmail.com")
emails = ["elianoliver101@gmail.com"]
subject = "DESAFIO TALENT LAB ITACOATIARA"
content = Content("text/plain", msg)
sg = sendgrid.SendGridAPIClient(api_key=sendgrid_token)

try:
    for i in range(len(numbers)):
        message = client.messages.create(
            from_=from_number,
            to=numbers[i],
            body=msg
        )
    print(f'Mensagem enviada com sucesso! SID: {message.sid}')
    # for i in range(len(emails)):
    #     mail = Mail(from_email, To(emails[i]), subject, content)
    #     response = sg.client.mail.send.post(request_body=mail.get())
    #     # print(mail)
    # # print(f'Email enviada com sucesso! SID: {message.sid}')

except Exception as e:
    print(f'Não foi possível enviar a mensagem: {e}')

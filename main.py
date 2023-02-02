from twilio.rest import Client

account_sid = 'ACa6e0fe1cd5f2ad6893420a24f8ada073'
auth_token = '326cb82bf2732040b9b54138bcee71b0'

client = Client(account_sid, auth_token)

from_number = '+13608003717'
to_number = '+5592993169741'

numbers = ['+5592985878449', '+5592993169741']
# number_one = '+559791388065'
# number_two = '+559288192972'
# number_three = '+559293290162'

case_name = input("Your name: ")
case_about = input("Your process: ")
msg = f"Olá, meu nome é {case_name} e estou participando do {case_about}"

try:
    for i in range(len(numbers)):
        message = client.messages.create(
            from_=from_number,
            to=numbers[i],
            body=msg
    )
    print(f'Mensagem enviada com sucesso! SID: {message.sid}')
except Exception as e:
    print(f'Não foi possível enviar a mensagem: {e}')


# try:
#     message = client.messages.create(
#         from_=from_number,
#         to=to_number,
#         body=msg
#     )

#     print(f'Mensagem enviada com sucesso! SID: {message.sid}')
# except Exception as e:
#     print(f'Não foi possível enviar a mensagem: {e}')
from twilio.rest import Client
import twilio

#OBS: NECESSÁRIO AUTENTICAÇÃO PARA CONSUMIR A API DO TWILLO

account_sid = 'ACb7b858e87e438703c5e6471686a81690'  # CONTA TWILLO

token = '66f50c497313ef3010aaadaa577cba82'  # TOKEN DA CONTA TWILLO

remetente = 'NÚMERO DA SUA CONTA'  # REMETENTE OBS: NÚMERO DA CONTA TWILLO
destino = 'NÚMERO DO DESTINATÁRIO'  # DESTINATÁRIO, NECESSÁRIO CADASTRAR DESTINATÁRIO NO TILLO

client = Client(account_sid, token)

message = client.messages.create(from_=remetente,
                                 body='KOE CAIO, PYTHON É FODAAA',
                                 to=destino)
# ENVIAR O SMS, COM REMETENTE, DESTINATÁRIO E MSG

print(message.sid)

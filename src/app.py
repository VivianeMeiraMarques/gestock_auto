users = []
def cadastro_user(nome, email):
    novo_user ={
        'nome':nome,
        'email':email
    }

    for user in users:
        if user['email'] == email:
            return 'email ja cadastrado'

    users.append(novo_user)
    return 'sucesso'

#controller
def cadastro(nome, cpf):
    print('ola')
    new_user = {
        "nome": nome,
        "cpf": cpf
    }
    return save(new_user)

#service
def save(new_user):
    if new_user["nome"] and new_user["cpf"]:
        return True #salvo no banco de dados
    return False #erro ao salvar no banco de dados
#-------------------------------------------------
def wellcome(email):
    if email:
        resposta = send_mail(email)
        if resposta:
            return "email enviado"
        return "erro de provedor de email"

def send_mail(email):
    return True
#-------------------------------------------------
def fetch_product_price_from_api(product_id):
    raise NotImplementedError("simulação")

def get_product_price(product_id):
    response = fetch_product_price_from_api(product_id)
    if response['status_code'] == 200:
        return response['json']['preco']
    raise Exception("Erro")
#-------------------------------------------------
def processar_pagamento(valor):
    if valor:
        resposta = enviar_pagamento(valor)
        if resposta:
            return "pagamento confirmado"
        return "erro no pagamento"

def enviar_pagamento(valor):
    return True
#-------------------------------------------------
#13
def enviar_email(email, mensagem):
    print(f'Enviando email para {email}:\n{mensagem}')

def enviar_sms(telefone, mensagem):
    print(f'Enviando SMS para {telefone}\n{mensagem}')

def criar_user(nome, email, telefone):
    user = {
        "nome": nome,
        "email": email,
        "telefone": telefone
    }
    print('User criado com sucesso!')
    enviar_email(email, "cadastro realizado")
    enviar_sms(telefone, "cadastro realizado")

    
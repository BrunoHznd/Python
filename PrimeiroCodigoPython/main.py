import pandas as pd
from twilio.rest import Client

# Retrieve your Account SID and Auth Token from environment variables
account_sid = 'ACcb1c64ea3ea30fe46317ffd5196c1afb'
auth_token = '4f0fc3aa27276ae0f1dfe12a00380e77'

# Initialize the Twilio client
client = Client(account_sid, auth_token)

# List of months
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

# Loop through each month
for mes in lista_meses:
    # Read the Excel file for the current month
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')

    # Check if any sales exceed 55,000
    if (tabela_vendas['Vendas'] > 55000).any():
        # Find the seller and sales amount
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]

        # Print the result
        print(f'No mês {mes}, encontrou alguém que bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')

        # Send an SMS notification via Twilio
        message = client.messages.create(
            from_='+15076877806',
            body=f'No mês {mes}, encontrou alguém que bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}',
            to='+5513991742722'
        )

        # Print the message SID
        print(message.sid)

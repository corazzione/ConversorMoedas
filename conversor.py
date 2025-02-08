import requests

def obter_taxas_cambio(api_key):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
    response = requests.get(url)
    dados = response.json()
    if dados["result"] == "success":
        return dados["conversion_rates"]
    else:
        print("Erro ao obter taxas de câmbio.")
        return None

def converter_moeda(valor, moeda_origem, moeda_destino, taxas):
    if moeda_origem not in taxas or moeda_destino not in taxas:
        print("Moeda não suportada.")
        return None
    valor_em_usd = valor / taxas[moeda_origem]
    valor_convertido = valor_em_usd * taxas[moeda_destino]
    return valor_convertido

def main():
    api_key = "667adccdcfa386f321895ab3"  # para obter a chave api= https://app.exchangerate-api.com/
    taxas = obter_taxas_cambio(api_key)

    if taxas:
        print("Bem-vindo ao Conversor de Moedas!")
        valor = float(input("Digite o valor a ser convertido: "))
        moeda_origem = input("Digite a moeda de origem (ex: BRL): ").upper()
        moeda_destino = input("Digite a moeda de destino (ex: USD): ").upper()

        valor_convertido = converter_moeda(valor, moeda_origem, moeda_destino, taxas)
        if valor_convertido:
            print(f"{valor} {moeda_origem} = {valor_convertido:.2f} {moeda_destino}")

if __name__ == "__main__":
    main()
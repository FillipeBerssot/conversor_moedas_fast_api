import requests
from fastapi import HTTPException

from conversor_moedas_fast_api.settings.settings import Settings

ALPHA_VANTAGE_API_NEW_KEY = Settings().ALPHA_VANTAGE_API_NEW_KEY
HTTP_OK = 200


def converter_currency(from_currency: str, to_currency: str, price: float):
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={ALPHA_VANTAGE_API_NEW_KEY}'

    try:
        response = requests.get(url=url)

        if response.status_code != HTTP_OK:
            raise HTTPException(
                status_code=response.status_code,
                detail=(
                    f'Erro na requisição para a API externa. Status: '
                    f'{response.status_code}'
                ),
            )

    except requests.exceptions.RequestException as error:
        raise HTTPException(
            status_code=400,
            detail=f'Erro na conexão com a API externa: {str(error)}',
        )

    except Exception as error:
        raise HTTPException(
            status_code=400,
            detail=f'Erro inesperado ao realizar a requisição: {str(error)}',
        )

    try:
        data = response.json()

    except ValueError as error:
        raise HTTPException(
            status_code=400,
            detail=f'Erro ao interpretar a resposta JSON: {str(error)}',
        )

    if 'Error Message' in data:
        raise HTTPException(
            status_code=400, detail=f'Erro da API: {data["Error Message"]}'
        )
    if 'Note' in data:
        note_text = data['Note']
        if 'standard API call frequency' in note_text:
            raise HTTPException(
                status_code=429,
                detail=f'Limite de requisições excedido: {note_text}',
            )
        else:
            raise HTTPException(
                status_code=400, detail=f'Nota da API: {note_text}'
            )

    if 'Realtime Currency Exchange Rate' not in data:
        raise HTTPException(
            status_code=400,
            detail=(
                'O campo "Realtime Currency Exchange Rate" não existe '
                'na resposta '
                'da API. Verifique se os parâmetros informados '
                '(from_currency e to_currency) estão corretos e se o par '
                f'de moedas está disponível. Error: {data}'
            ),
        )

    try:
        exchange_rate = float(
            data['Realtime Currency Exchange Rate']['5. Exchange Rate']
        )
    except (KeyError, ValueError) as error:
        raise HTTPException(
            status_code=400,
            detail=f'Erro ao converter a taxa de câmbio para float: {error}',
        )

    return {'converted_value': price * exchange_rate}

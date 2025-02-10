from typing import List

from fastapi import APIRouter, HTTPException, Path, Query

from conversor_moedas_fast_api.schemas.converter import (
    ConverterOutputSchema,
)
from conversor_moedas_fast_api.services.converter_currency import (
    converter_currency,
)

router = APIRouter()


@router.get('/{from_currency}', response_model=List[ConverterOutputSchema])
def converter_router(
    from_currency: str = Path(
        description='Código da moeda de origem (ex.: "BRL")',
        pattern=r'^[A-Z]{3}$',
        example='BRL',
    ),
    to_currencies: str = Query(
        description='Códigos das moedas de destino separados '
        'por vírgula (ex.: "USD","EUR","JPY")',
        pattern=r'^[A-Z]{3}(,[A-Z]{3})*$',
        example='USD,EUR,JPY',
    ),
    price: float = Query(
        gt=0,
        description='Valor a ser convertido (deve ser maior que 0)',
        example=10.0,
    ),
):
    split_currencies = to_currencies.split(',')

    results = []

    for currency in split_currencies:
        try:
            converted_value = converter_currency(
                from_currency=from_currency,
                to_currency=currency,
                price=price,
            )
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

        results.append(
            ConverterOutputSchema(
                message='Success',
                data=[
                    {'currency': currency, 'converted_value': converted_value}
                ],
            )
        )

    return results

from http import HTTPStatus


def test_converter_router_return_OK(client, vcr_cassette):
    LEN_DATA = 3

    cassette_name = 'converter_router_ok.yaml'

    with vcr_cassette.use_cassette(cassette_name):
        response = client.get(
            '/conversor_moedas_fast_api/v1/converter/BRL?to_currencies=USD,EUR,JPY&price=10'
        )

    assert response.status_code == HTTPStatus.OK

    data = response.json()

    assert isinstance(data, list)
    assert len(data) == LEN_DATA

    for item in data:
        assert 'message' in item
        assert 'data' in item
        assert isinstance(item['data'], list)

        assert len(item['data']) > 0
        assert 'currency' in item['data'][0]
        assert 'converted_value' in item['data'][0]


def test_converter_router_return_BAD_REQUEST(client, vcr_cassette):
    TO_CURRENCIES_EXPECTED = 'ZZZ'

    cassette_name = 'converter_router_BAD_REQUEST.yaml'

    with vcr_cassette.use_cassette(cassette_name):
        response = client.get(
            f'/conversor_moedas_fast_api/v1/converter/BRL?to_currencies={TO_CURRENCIES_EXPECTED}&price=10'
        )

    assert response.status_code == HTTPStatus.BAD_REQUEST

    data = response.json()

    assert 'Erro' in data['detail']

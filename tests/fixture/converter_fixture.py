import pytest
import vcr

vcr_instance = vcr.VCR(
    cassette_library_dir='tests/cassettes',
    record_mode='once',
    decode_compressed_response=True,
)


@pytest.fixture
def vcr_cassette():
    """
    Fixture que retorna a instância do VCR configurada.

    Todos os testes que utilizarem essa fixture terão suas requisições HTTP
    interceptadas e gravadas/reproduzidas a partir dos cassetes armazenados
    em 'tests/cassettes'.
    """

    return vcr_instance

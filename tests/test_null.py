
import pytest

from fastjsonschema import JsonSchemaException


exc = JsonSchemaException('data must be null')
@pytest.mark.parametrize('value, expected', [
    (0, exc),
    (None, None),
    (True, exc),
    ('abc', exc),
    ([], exc),
    ({}, exc),
])
def test_null(asserter, value, expected):
    asserter({'type': 'null'}, value, expected)

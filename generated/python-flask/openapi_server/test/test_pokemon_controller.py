import unittest

from flask import json

from openapi_server.models.error_response import ErrorResponse  # noqa: E501
from openapi_server.models.pokemon import Pokemon  # noqa: E501
from openapi_server.models.pokemon_create_request import PokemonCreateRequest  # noqa: E501
from openapi_server.models.pokemon_list_response import PokemonListResponse  # noqa: E501
from openapi_server.models.pokemon_update_request import PokemonUpdateRequest  # noqa: E501
from openapi_server.test import BaseTestCase


class TestPokemonController(BaseTestCase):
    """PokemonController integration test stubs"""

    def test_create_pokemon(self):
        """Test case for create_pokemon

        Create Pokemon
        """
        pokemon_create_request = {"level":8,"name":"name","isLegendary":False,"type":"type"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/pokemon',
            method='POST',
            headers=headers,
            data=json.dumps(pokemon_create_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_pokemon_by_id(self):
        """Test case for delete_pokemon_by_id

        Delete Pokemon by ID
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/pokemon/{pokemon_id}'.format(pokemon_id=UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d')),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_pokemon_by_id(self):
        """Test case for get_pokemon_by_id

        Get Pokemon by ID
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/pokemon/{pokemon_id}'.format(pokemon_id=UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d')),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_pokemon(self):
        """Test case for list_pokemon

        List Pokemon
        """
        query_string = [('limit', 20),
                        ('offset', 0)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/pokemon',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_replace_pokemon_by_id(self):
        """Test case for replace_pokemon_by_id

        Replace Pokemon by ID
        """
        pokemon_create_request = {"level":8,"name":"name","isLegendary":False,"type":"type"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/pokemon/{pokemon_id}'.format(pokemon_id=UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d')),
            method='PUT',
            headers=headers,
            data=json.dumps(pokemon_create_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_pokemon_by_id(self):
        """Test case for update_pokemon_by_id

        Update Pokemon by ID
        """
        pokemon_update_request = {"level":8,"name":"name","isLegendary":True,"type":"type"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/pokemon/{pokemon_id}'.format(pokemon_id=UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d')),
            method='PATCH',
            headers=headers,
            data=json.dumps(pokemon_update_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()

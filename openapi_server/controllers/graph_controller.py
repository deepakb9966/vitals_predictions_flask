import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.future_values_get200_response import FutureValuesGet200Response  # noqa: E501
from openapi_server.models.message_dto import MessageDto  # noqa: E501
from openapi_server import util
from src.predict import graph


def future_values_get(step_length):  # noqa: E501
    """future_values_get

     # noqa: E501

    :param step_length: 
    :type step_length: int

    :rtype: Union[FutureValuesGet200Response, Tuple[FutureValuesGet200Response, int], Tuple[FutureValuesGet200Response, int, Dict[str, str]]
    """
    return str(graph(step_length))

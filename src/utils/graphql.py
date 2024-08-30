from src.services.FrontifyClient import FrontifyClient
from typing import Callable, Optional, Tuple, List


def gql(query: str) -> Callable[[FrontifyClient, Optional[dict]], Tuple[dict, Optional[List[dict]]]]:
    return lambda client, variables: client.graphql(query, variables)

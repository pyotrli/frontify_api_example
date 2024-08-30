import json
from base64 import b64decode, b64encode


def decode_base64_string(base64_string: str) -> dict:
    base64_bytes = base64_string.encode("ascii")

    string_in_bytes = b64decode(base64_bytes)
    string_as_string = string_in_bytes.decode("ascii")
    return json.loads(string_as_string)


# accepted obj_types: "asset", "project", "metadata"... check others in API docs
def encode_obj_to_base64(identifier: int, obj_type: str) -> str:
    # catch incorrect identifier types
    if not isinstance(identifier, int):
        raise Exception('ID must be an int (number) - got something else')

    obj = {
        "identifier": identifier,
        "type": obj_type
    }

    # turn json to encoded base64 str
    s = json.dumps(obj)
    b = s.encode('ascii')
    encoded_bytes = b64encode(b)
    bytes_as_string = encoded_bytes.decode('ascii')

    return bytes_as_string


def smart_encode_projectid(frontify_projectid: str) -> str:
    '''accepts both an integer and an encoded base64 string as project ID'''
    try:
        frontify_project_number = int(frontify_projectid)
        frontify_projectid = encode_obj_to_base64(identifier=frontify_project_number, obj_type='project')
        return frontify_projectid
    except ValueError:
        return frontify_projectid

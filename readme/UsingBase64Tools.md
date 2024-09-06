# Using Base64 Tools
In this repository, we include a handful of utilities to work with the Base64 encoded IDs used by Frontify. 

These can be found in [base64tools.py](/examples/python/src/utils/base64tools.py).

## Frontify IDs
IDs returned by the Frontify API are in a Base64 encoded string representation of a JSON object with the format:

```json
{
    "identifier": 12345,
    "type": "object_type"
}
```

For the purposes of examples shown in this repository, the most commen object types are:
- project (library or workspace project)
- asset
- customMetadataProperty
- customMetadataPropertyOption

## Usage
### decode_base64_string
Decodes the provided Base64 string and returns a Python dictionary representing the decoded Base64 ID. The dictionary will include only the keys `identifier` and `type`.

```python
decode_base64_string("eyJpZGVudGlmaWVyIjoxMjM0NSwidHlwZSI6ImFzc2V0In0=")
```

returns
```python
{
    "identifier": 12345,
    "type": "asset"
}
```

### encode_obj_to_base64
Encodes a numeric identifier to a Base64 ID recognisable by the Frontify API. Useful when working with IDs obtained from URLs.

E.g. the asset ID `12345` taken from demo.frontify.com/screens/**12345** can be converted as follows:

```python
encode_obj_to_base64(12345, "asset")
```

returns
```python
"eyJpZGVudGlmaWVyIjoxMjM0NSwidHlwZSI6ImFzc2V0In0="
```

### smart_encode_projectid
Accepts both an integer and an encoded Base64 string as project ID. Useful when working with queries that require a project ID, or for when working with mixed IDs. Returns the Base64 encoded project ID.
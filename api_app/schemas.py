book = {
    "type": "object",
    "properties": {
        "title": {
            "type": "string"
        },
        "sub_title": {
            "type": ["string", "null"],
        },
        "author": {
            "type": "string"
        },
        "publisher": {
            "type": "string"
        },
        "year": {
            "type": "integer"
        },
        "pages": {
            "type": "integer"
        }

    },
    "required": ["title", "sub_title", "author", "publisher", "year", "pages"]
}

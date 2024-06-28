product_insert_schema = {
    'name' : { 'type': 'string', 'required': True, 'empty': False},
    'price' : { 'type': 'integer', 'required': True, 'min': 1},
    'description': { 'type': 'string', 'required': True, 'minlength': 6}
}
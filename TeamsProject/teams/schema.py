from .models import TeamMember

member_create_schema = {'firstName': {'type': 'string'},
                        'lastName': {'type': 'string'},
                        'phoneNumber': {'type': 'string', 'minlength': 10, 'maxlength': 15},
                        'email': {'type': 'string',
                                  'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'},
                        'role': {'type': 'integer', 'allowed': TeamMember.Role.values}}

member_update_schema = {'firstName': {'type': 'string', 'required': False},
                        'lastName': {'type': 'string', 'required': False},
                        'phoneNumber': {'type': 'string', 'minlength': 10, 'maxlength': 15, 'required': False},
                        'email': {'type': 'string', 'required': False,
                                  'regex': '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'},
                        'role': {'type': 'integer', 'allowed': TeamMember.Role.values, 'required': False}}

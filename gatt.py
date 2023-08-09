from value_type import ValueType, Language

# GATT Specific setting file

# Basic configuration
service = {
    'name': 'Expose',
    'uuid': '121e8e18-23c1-0bd5-b6d9-6180dba956bc'
}

characteristics = [
    {
        'name': 'Event',
        'uuid': '1c8e7830-dc60-b4d3-3763-604b1403950a',
        'direction': 'BIDI',
        'args': {
            'type': ValueType.String,
            'size': None,
            'names': ['msg']
        }
    },
    {
        'name': 'Lux',
        'uuid': '16cf81e3-0212-58b9-0380-0dbc6b54c51d',
        'direction': 'PtoC',
        'args': {
            'type': ValueType.Float,
            'size': 4,
            'names': ['iso', 'f', 'ss', 'lv', 'ev', 'lux']
        }
    },
    {
        'name': 'RGB',
        'uuid': '67f46ec5-3d54-54c2-ae2d-fb318a4973b0',
        'direction': 'PtoC',
        'args': {
            'type': ValueType.Float,
            'size': 4,
            'names': ['r', 'g', 'b', 'ir']
        }
    },
    {
        'name': 'ISO',
        'uuid': '241abff2-5d09-b5a3-4a77-cfc19cfac587',
        'direction': 'CtoP',
        'args': {
            'type': ValueType.Int,
            'size': 4,
            'names': ['iso']
        }
    },

]

# For BleGattClient.swift
client_services = [
    'Expose',
    'Battery'
]

#############################################################
# The following is type assign configuration by language.
# Does not need to be changed under normal use.
#############################################################


def type_swift():
    for characteristic in characteristics:
        if characteristic['args']['type'] == ValueType.Int:
            characteristic['args']['type_fixed'] = 'Int32'
        elif characteristic['args']['type'] == ValueType.Float:
            characteristic['args']['type_fixed'] = 'Float32'
        elif characteristic['args']['type'] == ValueType.String:
            characteristic['args']['type_fixed'] = 'String'


def type_cpp():
    for characteristic in characteristics:
        if characteristic['args']['type'] == ValueType.Int:
            characteristic['args']['type_fixed'] = 'int'
        elif characteristic['args']['type'] == ValueType.Float:
            characteristic['args']['type_fixed'] = 'float'
        elif characteristic['args']['type'] == ValueType.String:
            characteristic['args']['type_fixed'] = 'std::string'


def fix_type(language: Language):
    if language == Language.Cpp:
        type_cpp()
    elif language == Language.Swift:
        type_swift()

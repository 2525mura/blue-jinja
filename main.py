from jinja2 import Template, Environment, FileSystemLoader


def main():
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template/peripheral/esp32/BleService.h.jinja')
    # template = env.get_template('template/peripheral/esp32/BleService.cpp.jinja')
    # template = env.get_template('template/peripheral/esp32/BleServiceDelegate.h.jinja')

    service_conf = {
        'name': 'Expose',
        'uuid': '4fafc201-1fb5-459e-8fcc-c5c9c331914b'
    }

    characteristics_conf = [
        {
            'name': 'Event',
            'uuid': 'beb5483e-36e1-4688-b7f5-ea07361b26a8',
            'direction': 'BIDI',
            'args': {
                'type': 'std::string',
                'size': None,
                'names': ['msg']
            }
        },
        {
            'name': 'Lux',
            'uuid': '16cf81e3-0212-58b9-0380-0dbc6b54c51d',
            'direction': 'PtoC',
            'args': {
                'type': 'float',
                'size': 4,
                'names': ['iso', 'f', 'ss', 'lv', 'ev', 'lux']
            }
        },
        {
            'name': 'RGB',
            'uuid': '67f46ec5-3d54-54c2-ae2d-fb318a4973b0',
            'direction': 'PtoC',
            'args': {
                'type': 'float',
                'size': 4,
                'names': ['r', 'g', 'b', 'ir']
            }
        },
        {
            'name': 'ISO',
            'uuid': '241abff2-5d09-b5a3-4a77-cfc19cfac587',
            'direction': 'CtoP',
            'args': {
                'type': 'int',
                'size': 4,
                'names': ['iso']
            }
        },

    ]

    rendered = template.render(service_conf=service_conf, characteristics_conf=characteristics_conf)
    print(str(rendered))


if __name__ == '__main__':
    main()

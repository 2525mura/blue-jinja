import os
import gatt
from jinja2 import Template, Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))


def peripheral_esp32_server(path: str):
    os.makedirs(path, exist_ok=True)
    with open(f'{path}/BleService{gatt.service["name"]}.h', mode='w') as f:
        template = env.get_template('template/peripheral/esp32_server/BleService.h.jinja')
        rendered = template.render(service_conf=gatt.service, characteristics_conf=gatt.characteristics)
        f.write(rendered)

    with open(f'{path}/BleService{gatt.service["name"]}.cpp', mode='w') as f:
        template = env.get_template('template/peripheral/esp32_server/BleService.cpp.jinja')
        rendered = template.render(service_conf=gatt.service, characteristics_conf=gatt.characteristics)
        f.write(rendered)

    with open(f'{path}/BleService{gatt.service["name"]}Delegate.h', mode='w') as f:
        template = env.get_template('template/peripheral/esp32_server/BleServiceDelegate.h.jinja')
        rendered = template.render(service_conf=gatt.service, characteristics_conf=gatt.characteristics)
        f.write(rendered)


def main():
    peripheral_esp32_server(path='out_esp32')


if __name__ == '__main__':
    main()

import os
import shutil
import gatt
from value_type import Language
from jinja2 import Template, Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('.'))


def copy_common_src(src_path: str, dst_path: str):
    for filename in os.listdir(src_path):
        shutil.copy(os.path.join(src_path, filename), dst_path)


def peripheral_esp32_server(path: str):
    gatt.fix_type(language=Language.Cpp)
    os.makedirs(path, exist_ok=True)
    copy_common_src(src_path='template/peripheral/esp32_server/common_src', dst_path=path)
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


def central_ios_client(path: str):
    gatt.fix_type(language=Language.Swift)
    os.makedirs(path, exist_ok=True)
    copy_common_src(src_path='template/central/ios_client/common_src', dst_path=path)
    with open(f'{path}/BleGattClient.swift', mode='w') as f:
        template = env.get_template('template/central/ios_client/BleGattClient.swift.jinja')
        rendered = template.render(client_services_conf=gatt.client_services)
        f.write(rendered)
    with open(f'{path}/BleService{gatt.service["name"]}.swift', mode='w') as f:
        template = env.get_template('template/central/ios_client/BleService.swift.jinja')
        rendered = template.render(service_conf=gatt.service, characteristics_conf=gatt.characteristics)
        f.write(rendered)


def main():
    peripheral_esp32_server(path='out_esp32')
    central_ios_client(path='out_ios')


if __name__ == '__main__':
    main()

# Author Andrew Chupin
# Coding in UTF-8

# Generate JSON app by request
from builder.lib.model.entity.driver_app_new import DriverApplicationNew
from std.std import validate_field


def parse_app_by_json(parsed_json: dict) -> DriverApplicationNew:
    id = validate_field(parsed_json['id'])
    app_name = validate_field(parsed_json['app_name'])
    tenant_name = validate_field(parsed_json['tenant_name'])
    bundle = validate_field(parsed_json['bundle'])
    host = validate_field(parsed_json['host'])
    new_host = validate_field(parsed_json['new_host'])
    chat_host = validate_field(parsed_json['chat_host'])
    geocode_host = validate_field(parsed_json['geocode_host'])
    push_key = validate_field(parsed_json['push_key'])
    google_map_key = validate_field(parsed_json['google_map_key'])
    app_type = validate_field(parsed_json['app_type'])
    version_app = validate_field(parsed_json['version_app'])
    use_worker_reg = validate_field(parsed_json['use_worker_reg'])
    worker_reg_url = validate_field(parsed_json['worker_reg_url'])
    worker_reg_description = validate_field(parsed_json['worker_reg_description'])
    worker_reg_button = validate_field(parsed_json['worker_reg_button'])
    yandex_key = validate_field(parsed_json['yandex_key'])
    allow_root = validate_field(parsed_json['allow_root'])
    use_sms_auth = validate_field(parsed_json['use_sms_auth'])

    return DriverApplicationNew(id=id, app_name=app_name, tenant_name=tenant_name, bundle=bundle,
                             host=host, new_host=new_host, chat_host=chat_host, geocode_host=geocode_host,
                             push_key=push_key, google_map_key=google_map_key, app_type=app_type,
                             version_app=version_app, use_worker_reg=use_worker_reg, worker_reg_url=worker_reg_url,
                             worker_reg_description=worker_reg_description, worker_reg_button=worker_reg_button,
                             yandex_key=yandex_key, allow_root=allow_root, use_sms_auth=use_sms_auth)

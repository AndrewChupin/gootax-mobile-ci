
from backend.model.entity.build_config import BuildConfig
from backend.model.helper.build_helper import validate_version, validate_email
from std.error.base_error import BaseError
from std.std import validate_field, str_to_bool

def generate_build_config(form: dict, index: int) -> BuildConfig:
    try:
        version_code = int(validate_version(form["version_code"]))
        version_name = str(validate_version(form["version_name"])).strip()
        email = str(validate_email(form["email"])).strip()
        build_type = str(validate_field(form["build_type"])).strip()
        ios_company_name = str(validate_field(form["ios_company_name"])).strip()
        build_market = str_to_bool(validate_field(form["build_market"]))
        is_create_app = str_to_bool(form["create_app"])
        id_build_email = str(validate_email(form["build_email"])).strip()
        id_company_id = str(validate_field(form["company_id"])).strip()
        branch = str(validate_field(form["branch"])).strip()
    except BaseError as e:
        raise e

    return BuildConfig(
        build_type = build_type,
    build_market = build_market,
    create_app = is_create_app,
    email = email,
        app_id=index,
    version_code = version_code,
    version_name = version_name,
    ios_company_name = ios_company_name,
    branch = branch,
    build_email = id_build_email,
    company_id = id_company_id
    )

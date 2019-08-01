import time

from builder.lib.script.launcher.launcher_factory import LauncherFactory
from std.network import api
import requests

from std.std import merge


class MobileApi:

    @staticmethod
    def post_build_status(base_url: str, app_index: int, status: int, build_type: str) -> None:
        data = {
            "app_index": app_index,
            "status": status,
            "time": time.time()
        }

        route: str

        if build_type == LauncherFactory.BUILD_IOS or build_type == LauncherFactory.BUILD_ANDROID:
            route = api.post_update_build_status
        elif build_type == LauncherFactory.BUILD_DRIVER:
            route = api.post_driver_update_build_status
        elif build_type == LauncherFactory.BUILD_DRIVER_NEW:
            route = api.post_driver_new_update_build_status

        requests.post(url=merge(base_url + route), data=data)


    @staticmethod
    def post_app_build(base_url: str, data: dict) -> None:
        requests.post(url=merge(base_url + api.post_app_build), form=data)

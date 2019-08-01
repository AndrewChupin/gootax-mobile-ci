from builder.lib.script.launcher.driver import AndroidDriverLauncher
from builder.lib.script.launcher.ios import IosLauncher

from builder.lib.script.launcher.android import AndroidLauncher


class LauncherFactory:

    BUILD_DRIVER = "android_driver"
    BUILD_DRIVER_NEW = "android_driver_new"
    BUILD_ANDROID = "android"
    BUILD_IOS = "ios"

    @staticmethod
    def create_launcher(build_type, application, params, theme=None):
        if build_type == LauncherFactory.BUILD_ANDROID:
            return AndroidLauncher(application=application,
                                   theme=theme,
                                   params=params)
        elif build_type == LauncherFactory.BUILD_DRIVER:
            return AndroidDriverLauncher(application=application, params=params, is_new=False)
        elif build_type == LauncherFactory.BUILD_DRIVER_NEW:
            return AndroidDriverLauncher(application=application, params=params, is_new=True)
        else:
            return IosLauncher(application=application,
                               theme=theme,
                               params=params)


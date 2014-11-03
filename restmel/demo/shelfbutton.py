import os
import subprocess

import restmel

package_path = os.path.dirname(restmel.__file__)
app_path = os.path.join(package_path, "demo", "app.qml")


def launch(qmlpath):
    """Run QML application

    Arguments:
        qmlpath (str): Absolute path to qmlscene

    """

    CREATE_NO_WINDOW = 0x08000000
    subprocess.Popen([qmlpath, app_path], creationflags=CREATE_NO_WINDOW)

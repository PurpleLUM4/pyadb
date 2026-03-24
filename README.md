# Python Android Debug Bridge Wrapper

Simple Android debug bridge wrapper for Python designed for Linux.
Note: This may not work on Windows machines without adjusting the wrappers code.

## Exports
```py
# adb - class
adb.server_running() -> bool
adb.start_server() -> None
adb.kill_server() -> None
adb.devices() -> dict
adb.device_state(DEVICE_ID: str) -> str
adb.shell(DEVICE_ID: str, COMMAND: str) -> str # Leave command arg blank for interactive shell
adb.packages(DEVICE_ID: str) -> list
adb.install(DEVICE_ID: str, APK_PATH: str) -> bool
adb.uninstall(DEVICE_ID: str, PACKAGE: str) -> bool
adb.push(DEVICE_ID: str, LOCAL_PATH: str, REMOTE_PATH: str) -> bool
adb.pull(DEVICE_ID: str, REMOTE_PATH: str, LOCAL_PATH: str) -> bool
```

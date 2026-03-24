#!/usr/bin/env python3

import re
import os
import subprocess

class adb:
    def server_running() -> bool:
        proc = subprocess.Popen(["ps", "-e"], stdout=subprocess.PIPE)
        stdout = proc.communicate()[0].decode().strip()

        return " adb\n" in stdout

    def start_server() -> None:
        subprocess.Popen(["adb", "start-server"])
    
    def kill_server() -> None:
        subprocess.Popen(["adb", "kill-server"])

    def devices() -> dict:
        proc = subprocess.Popen(["adb", "devices"], stdout=subprocess.PIPE)
        stdout = proc.communicate()[0].decode().strip()

        dictionary_to_return = {}

        for stdout_line in stdout.split("\n"):
            if stdout_line.lower() == "list of devices attached":
                continue

            device_id = stdout_line.split("\t")[0]
            device_state = stdout_line.split("\t")[1]

            dictionary_to_return[device_id] = device_state

        return dictionary_to_return

    def device_state(device_id : str):
        return adb.devices()[device_id]

    def shell(device_id: str, command = "") -> str:
        proc = subprocess.Popen(["adb", "-s", device_id, "shell"] + command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate()

        return (stdout + stderr).decode().strip()
    
    def packages(device_id: str) -> list:
        proc = subprocess.Popen(["adb", "-s", device_id, "shell", "pm", "list", "packages"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate()

        return (stdout + stderr).decode().strip().split("\n")

    def install(device_id: str, apk_path: str) -> bool:
        proc = subprocess.Popen(["adb", "-s", device_id, "install", apk_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate()

        return "success" in (stdout + stderr).decode().lower()
    
    def uninstall(device_id: str, package: str) -> bool:
        proc = subprocess.Popen(["adb", "-s", device_id, "uninstall", package], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate()

        return "success" in (stdout + stderr).decode().lower()

    def push(device_id: str, local_path: str, remote_path: str) -> bool:
        local_path = os.path.abspath(local_path)

        proc = subprocess.Popen(["adb", "-s", device_id, "push", local_path, remote_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate()

        return local_path.lower() + ": 1 file pushed, 0 skipped" in (stdout + stderr).decode().strip().lower()

    def pull(device_id: str, remote_path: str, local_path: str) -> bool:
        local_path = os.path.abspath(local_path)

        proc = subprocess.Popen(["adb", "-s", device_id, "pull", remote_path, local_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate()

        return remote_path.lower() + ": 1 file pulled, 0 skipped" in (stdout + stderr).decode().strip().lower()

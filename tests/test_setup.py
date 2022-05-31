import re
import subprocess

SETUP_CMD = ["python3", "setup.py"]
VERSION_RE = re.compile(r"\d\d?.\d\d?.\d\d?")


def stdout_setup(option):
    return subprocess.run(
        SETUP_CMD + [f"--{option}"], capture_output=True, encoding="utf8"
    ).stdout.strip()


def test_setup_name():
    assert stdout_setup("name") == "cornerstone"


def test_setup_version():
    res = stdout_setup("version")
    assert VERSION_RE.match(res) is not None


def test_setup_description():
    assert stdout_setup("description") is not None


def test_setup_long_description():
    assert stdout_setup("long-description") is not None

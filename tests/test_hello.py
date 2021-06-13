import pytest


def test_hello_world(script_runner):
    ret = script_runner.run('hello-world')
    assert ret.success

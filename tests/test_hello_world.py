
import pytest

def test_success(script_runner):
    ret = script_runner.run('hello-world')
    assert ret.success
    assert ret.stdout.rstrip() == 'Hello world!'

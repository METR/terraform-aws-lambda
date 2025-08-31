from unittest.mock import Mock

import pytest
from pytest import raises

from package import (
    BuildPlanManager,
    get_build_system_from_pyproject_toml_manual,
    get_build_system_from_pyproject_toml_stdlib,
)


@pytest.mark.parametrize(
    "parser",
    [
        get_build_system_from_pyproject_toml_manual,
        get_build_system_from_pyproject_toml_stdlib,
    ],
)
def test_get_build_system_from_pyproject_toml_manual_inexistent(parser):
    assert parser("fixtures/inexistent/pyproject.toml") is None


@pytest.mark.parametrize(
    "parser",
    [
        get_build_system_from_pyproject_toml_manual,
        get_build_system_from_pyproject_toml_stdlib,
    ],
)
def test_get_build_system_from_pyproject_toml_manual_unknown(parser):
    assert parser("fixtures/pyproject-unknown.toml") is None


def test_build_manager_sucess_command():
    bpm = BuildPlanManager(args=Mock())
    # Should not have exception raised
    bpm.execute(build_plan=[["sh", "/tmp", "pwd"]], zip_stream=None, query=None)


def test_build_manager_failing_command():
    bpm = BuildPlanManager(args=Mock())
    with raises(Exception):
        bpm.execute(
            build_plan=[[["sh", "/tmp", "NOTACOMMAND"]]],
            zip_stream=None,
            query=None,
        )


@pytest.mark.parametrize(
    "parser",
    [
        get_build_system_from_pyproject_toml_manual,
        get_build_system_from_pyproject_toml_stdlib,
    ],
)
def test_get_build_system_from_pyproject_toml_manual_poetry(parser):
    assert parser("examples/fixtures/python-app-poetry/pyproject.toml") == "poetry"


@pytest.mark.parametrize(
    "parser",
    [
        get_build_system_from_pyproject_toml_manual,
        get_build_system_from_pyproject_toml_stdlib,
    ],
)
def test_get_build_system_from_pyproject_toml_manual_uv(parser):
    assert parser("examples/fixtures/python-app-uv/pyproject.toml") == "uv"

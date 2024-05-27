# -*- coding: utf-8 -*-
import math
import os
import stat
from pathlib import Path

import pytest

import aioshutil

pytestmark = [pytest.mark.asyncio]


async def test_copyfileobj(tmp_path: Path):
    (tmp_path / "temp.txt").write_text("Hello World!", encoding="utf-8")
    with open(tmp_path / "temp.txt", "r") as fsrc, open(
        tmp_path / "temp1.txt", "w"
    ) as fdst:
        await aioshutil.copyfileobj(fsrc, fdst)
    assert (tmp_path / "temp1.txt").read_text() == "Hello World!"


async def test_copyfile(tmp_path: Path):
    (tmp_path / "temp.txt").write_text("Hello World!", encoding="utf-8")
    await aioshutil.copyfile(tmp_path / "temp.txt", tmp_path / "temp1.txt")
    assert (tmp_path / "temp1.txt").read_text() == "Hello World!"


async def test_copymode(tmp_path: Path):
    (tmp_path / "temp.txt").write_text("Hello World!", encoding="utf-8")
    (tmp_path / "temp1.txt").write_text("Hello World!", encoding="utf-8")
    os.chmod(tmp_path / "temp.txt", stat.S_IEXEC)
    await aioshutil.copymode(tmp_path / "temp.txt", tmp_path / "temp1.txt")
    assert (tmp_path / "temp1.txt").stat().st_mode == (
        tmp_path / "temp.txt"
    ).stat().st_mode


async def test_copystat(tmp_path: Path):
    tmp_path.joinpath("temp.txt").write_text("Hello World!", encoding="utf-8")
    tmp_path.joinpath("temp1.txt").write_text("Hello World!", encoding="utf-8")
    tmp_path.joinpath("temp1.txt").chmod(stat.S_IEXEC)
    await aioshutil.copystat(tmp_path / "temp.txt", tmp_path / "temp1.txt")
    assert math.isclose(
        tmp_path.joinpath("temp1.txt").stat().st_atime,
        tmp_path.joinpath("temp.txt").stat().st_atime,
        rel_tol=1e-6,
    )
    assert (
        tmp_path.joinpath("temp1.txt").stat().st_mode
        == tmp_path.joinpath("temp.txt").stat().st_mode
    )


async def test_copy(tmp_path: Path):
    tmp_path.joinpath("temp.txt").write_text("Hello World!", encoding="utf-8")
    tmp_path.joinpath("temp.txt").chmod(
        tmp_path.joinpath("temp.txt").stat().st_mode | stat.S_IEXEC
    )
    await aioshutil.copy(tmp_path.joinpath("temp.txt"), tmp_path.joinpath("temp1.txt"))
    assert (
        tmp_path.joinpath("temp1.txt").stat().st_mode
        == tmp_path.joinpath("temp.txt").stat().st_mode
    )


async def test_copy2(tmp_path: Path):
    tmp_path.joinpath("temp.txt").write_text("Hello World!", encoding="utf-8")
    tmp_path.joinpath("temp.txt").chmod(
        tmp_path.joinpath("temp.txt").stat().st_mode | stat.S_IEXEC
    )
    await aioshutil.copy2(tmp_path.joinpath("temp.txt"), tmp_path.joinpath("temp1.txt"))
    assert math.isclose(
        tmp_path.joinpath("temp1.txt").stat().st_atime,
        tmp_path.joinpath("temp.txt").stat().st_atime,
        rel_tol=1e-6,
    )
    assert (
        tmp_path.joinpath("temp1.txt").stat().st_mode
        == tmp_path.joinpath("temp.txt").stat().st_mode
    )


async def test_copytree(tmp_path: Path):
    (tmp_path / "foo").mkdir()
    tmp_path.joinpath("foo", "bar.txt").write_text("Hello World!", encoding="utf-8")
    await aioshutil.copytree(tmp_path / "foo", tmp_path / "bar")
    assert (tmp_path / "bar" / "bar.txt").exists()


async def test_move(tmp_path: Path):
    tmp_path.joinpath("temp.txt").write_text("Hello World!", encoding="utf-8")
    await aioshutil.move(tmp_path.joinpath("temp.txt"), tmp_path.joinpath("temp1.txt"))
    assert not tmp_path.joinpath("temp.txt").exists()
    assert tmp_path.joinpath("temp1.txt").exists()

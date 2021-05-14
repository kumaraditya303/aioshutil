# -*- coding: utf-8 -*-
"""
Asynchronous shutil module.
"""
import asyncio
import shutil
from functools import partial, wraps
from typing import Any, Awaitable, Callable, TypeVar, cast

__all__ = [
    "copyfileobj",
    "copyfile",
    "copymode",
    "copystat",
    "copy",
    "copy2",
    "copytree",
    "move",
    "rmtree",
    "Error",
    "SpecialFileError",
    "ExecError",
    "make_archive",
    "get_archive_formats",
    "register_archive_format",
    "unregister_archive_format",
    "get_unpack_formats",
    "register_unpack_format",
    "unregister_unpack_format",
    "unpack_archive",
    "ignore_patterns",
    "chown",
    "which",
    "get_terminal_size",
    "SameFileError",
]

T = TypeVar("T", bound=Callable[..., Any])


def sync_to_async(func: T):
    @wraps(func)
    async def run_in_executor(*args, **kwargs):
        loop = asyncio.get_event_loop()
        pfunc = partial(func, *args, **kwargs)
        return await loop.run_in_executor(None, pfunc)

    return cast(Awaitable[T], run_in_executor)


rmtree = sync_to_async(shutil.rmtree)
copyfile = sync_to_async(shutil.copyfile)
copyfileobj = sync_to_async(shutil.copyfileobj)
copymode = sync_to_async(shutil.copymode)
copystat = sync_to_async(shutil.copystat)
copy = sync_to_async(shutil.copy)
copy2 = sync_to_async(shutil.copy2)
copytree = sync_to_async(shutil.copytree)
move = sync_to_async(shutil.move)
Error = shutil.Error
SpecialFileError = shutil.SpecialFileError
ExecError = shutil.ExecError
make_archive = sync_to_async(shutil.make_archive)
get_archive_formats = sync_to_async(shutil.get_archive_formats)
register_archive_format = sync_to_async(shutil.register_archive_format)
unregister_archive_format = sync_to_async(shutil.unregister_archive_format)
get_unpack_formats = sync_to_async(shutil.get_unpack_formats)
register_unpack_format = sync_to_async(shutil.register_unpack_format)
unregister_unpack_format = sync_to_async(shutil.unregister_unpack_format)
unpack_archive = sync_to_async(shutil.unpack_archive)
ignore_patterns = sync_to_async(shutil.ignore_patterns)
chown = sync_to_async(shutil.chown)
which = sync_to_async(shutil.which)
get_terminal_size = sync_to_async(shutil.get_terminal_size)
SameFileError = shutil.SameFileError


if hasattr(shutil, "statvfs"):  # pragma: no cover
    __all__.append("disk_usage")
    disk_usage = sync_to_async(shutil.disk_usage)

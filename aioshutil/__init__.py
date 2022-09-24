# -*- coding: utf-8 -*-
"""
Asynchronous shutil module.
"""
from __future__ import annotations

import asyncio
import shutil
from functools import partial, wraps
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Coroutine,
    Optional,
    Sequence,
    TypeVar,
    Union,
    overload,
)

try:
    from typing import ParamSpec, TypeAlias  # type: ignore
except ImportError:
    # Python versions < 3.10
    from typing_extensions import ParamSpec, TypeAlias

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

P = ParamSpec("P")
R = TypeVar("R")

if TYPE_CHECKING:  # pragma: no cover
    # type hints for wrapped functions with overloads (which are incompatible
    # with ParamSpec).

    import sys
    from os import PathLike

    StrPath: TypeAlias = Union[str, PathLike[str]]
    BytesPath: TypeAlias = Union[bytes, PathLike[bytes]]
    StrOrBytesPath: TypeAlias = Union[str, bytes, PathLike[str], PathLike[bytes]]
    _PathReturn: TypeAlias = Any
    _StrPathT = TypeVar("_StrPathT", bound=StrPath)

    @overload
    async def copy(
        src: StrPath, dst: StrPath, *, follow_symlinks: bool = ...
    ) -> _PathReturn:
        ...

    @overload
    async def copy(
        src: BytesPath, dst: BytesPath, *, follow_symlinks: bool = ...
    ) -> _PathReturn:
        ...

    async def copy(src, dst, *, follow_symlinks=...):
        ...

    @overload
    async def copy2(
        src: StrPath, dst: StrPath, *, follow_symlinks: bool = ...
    ) -> _PathReturn:
        ...

    @overload
    async def copy2(
        src: BytesPath, dst: BytesPath, *, follow_symlinks: bool = ...
    ) -> _PathReturn:
        ...

    async def copy2(src, dst, *, follow_symlinks=...):
        ...

    @overload
    async def register_archive_format(
        name: str,
        function: Callable[..., object],
        extra_args: Sequence[tuple[str, Any] | list[Any]],
        description: str = ...,
    ) -> None:
        ...

    @overload
    async def register_archive_format(
        name: str,
        function: Callable[[str, str], object],
        extra_args: None = ...,
        description: str = ...,
    ) -> None:
        ...

    async def register_archive_format(name, function, extra_args=..., description=...):
        ...

    @overload
    async def register_unpack_format(
        name: str,
        extensions: list[str],
        function: Callable[..., object],
        extra_args: Sequence[tuple[str, Any]],
        description: str = ...,
    ) -> None:
        ...

    @overload
    async def register_unpack_format(
        name: str,
        extensions: list[str],
        function: Callable[[str, str], object],
        extra_args: None = ...,
        description: str = ...,
    ) -> None:
        ...

    async def register_unpack_format(
        name, extensions, function, extra_args=..., description=...
    ):
        ...

    @overload
    async def chown(
        path: StrOrBytesPath, user: Union[str, int], group: None = ...
    ) -> None:
        ...

    @overload
    async def chown(
        path: StrOrBytesPath, user: None = ..., *, group: Union[str, int]
    ) -> None:
        ...

    @overload
    async def chown(path: StrOrBytesPath, user: None, group: Union[str, int]) -> None:
        ...

    @overload
    async def chown(
        path: StrOrBytesPath, user: Union[str, int], group: Union[str, int]
    ) -> None:
        ...

    async def chown(path, user=..., group=...):
        ...

    if sys.version_info >= (3, 8):

        @overload
        async def which(
            cmd: _StrPathT, mode: int = ..., path: Optional[StrPath] = ...
        ) -> Union[str, _StrPathT, None]:
            ...

        @overload
        async def which(
            cmd: bytes, mode: int = ..., path: Optional[StrPath] = ...
        ) -> Optional[bytes]:
            ...

        async def which(
            cmd, mode=..., path=...
        ) -> Union[bytes, str, StrPath, PathLike[str], None]:
            ...

    else:

        async def which(
            cmd: _StrPathT, mode: int = ..., path: StrPath | None = ...
        ) -> str | _StrPathT | None:
            ...


def sync_to_async(func: Callable[P, R]) -> Callable[P, Coroutine[Any, Any, R]]:
    @wraps(func)
    async def run_in_executor(*args: P.args, **kwargs: P.kwargs) -> R:
        loop = asyncio.get_event_loop()
        pfunc = partial(func, *args, **kwargs)
        return await loop.run_in_executor(None, pfunc)

    return run_in_executor


rmtree = sync_to_async(shutil.rmtree)
copyfile = sync_to_async(shutil.copyfile)
copyfileobj = sync_to_async(shutil.copyfileobj)
copymode = sync_to_async(shutil.copymode)
copystat = sync_to_async(shutil.copystat)
copy = sync_to_async(shutil.copy)  # type: ignore # noqa: F811
copy2 = sync_to_async(shutil.copy2)  # type: ignore # noqa: F811
copytree = sync_to_async(shutil.copytree)
move = sync_to_async(shutil.move)
Error = shutil.Error
SpecialFileError = shutil.SpecialFileError
ExecError = shutil.ExecError
make_archive = sync_to_async(shutil.make_archive)
get_archive_formats = sync_to_async(shutil.get_archive_formats)
register_archive_format = sync_to_async(shutil.register_archive_format)  # type: ignore # noqa: F811
unregister_archive_format = sync_to_async(shutil.unregister_archive_format)
get_unpack_formats = sync_to_async(shutil.get_unpack_formats)
register_unpack_format = sync_to_async(shutil.register_unpack_format)  # type: ignore # noqa: F811
unregister_unpack_format = sync_to_async(shutil.unregister_unpack_format)
unpack_archive = sync_to_async(shutil.unpack_archive)
ignore_patterns = sync_to_async(shutil.ignore_patterns)
chown = sync_to_async(shutil.chown)  # type: ignore # noqa: F811
which = sync_to_async(shutil.which)  # type: ignore # noqa: F811
get_terminal_size = sync_to_async(shutil.get_terminal_size)
SameFileError = shutil.SameFileError


if "disk_usage" in shutil.__all__:  # pragma: no cover
    __all__.append("disk_usage")
    disk_usage = sync_to_async(shutil.disk_usage)

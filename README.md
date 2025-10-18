# aioshutil: Asynchronous shutil module.

[![Downloads](https://static.pepy.tech/badge/aioshutil)](https://pepy.tech/project/aioshutil) ![](https://img.shields.io/pypi/v/aioshutil)  ![](https://img.shields.io/pypi/pyversions/aioshutil) ![](https://img.shields.io/pypi/implementation/aioshutil)

# Introduction

`aioshutil` is a Python library which provides asynchronous version of function of shutil module. `shutil` module is blocking and using it in asyncio applications will block the event loop and slow down the application, `aioshutil` provides asynchronous friendly versions of the functions of the `shutil` module as it performs blocking io in a thread pool.

# Installation

```console
$ pip install aioshutil
```

# Usage

The API of `aioshutil` module is same as `shutil` module except that it is asynchronous.

```python
from aioshutil import rmtree
await rmtree("/tmp")
```

`aioshutil` provides the following functions:

- `copyfileobj`
- `copyfile`
- `copymode`
- `copystat`
- `copy`
- `copy2`
- `copytree`
- `move`
- `rmtree`
- `make_archive`
- `get_archive_formats`
- `register_archive_format`
- `unregister_archive_format`
- `get_unpack_formats`
- `register_unpack_format`
- `unregister_unpack_format`
- `unpack_archive`
- `ignore_patterns`
- `chown`
- `which`
- `get_terminal_size`

`aioshutil` provides the following exceptions for consistency with `shutil` module:

- `Error`
- `SpecialFileError`
- `SameFileError`

# -*- coding: utf-8 -*-
import pytest


def pytest_collection_modifyitems(items):
    for item in items:
        # Only Python tests, not the typing tests
        if isinstance(item, pytest.Function):
            item.add_marker(pytest.mark.asyncio)

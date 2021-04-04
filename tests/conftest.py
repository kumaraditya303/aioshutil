# -*- coding: utf-8 -*-
import pytest


def pytest_collection_modifyitems(items):
    for item in items:
        item.add_marker(pytest.mark.asyncio)

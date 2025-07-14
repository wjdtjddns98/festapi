import asyncio
from typing import Any, Generator
from unittest.mock import Mock, patch

import pytest
import pytest_asyncio
from _pytest.fixtures import FixtureRequest
from tortoise.backends.base.config_generator import generate_config
from tortoise.contrib.test import finalizer, initializer

from app.configs import config
from app.configs.tortoise_config import TORTOISE_APP_MODELS

TEST_DB_LABEL = "models"
TEST_DB_TZ = "Asia/seoul"


def get_test_db_config() -> dict[str, Any]:
    tortoise_config = generate_config(
        db_url=f"mysql://{config.MYSQL_USER}:{config.MYSQL_PASSWORD}@{config.MYSQL_HOST}:{config.MYSQL_PORT}/test",
        app_modules={TEST_DB_LABEL: TORTOISE_APP_MODELS},
        connection_label=TEST_DB_LABEL,
        testing=True,
    )
    tortoise_config["timezone"] = TEST_DB_TZ

    return tortoise_config


@pytest.fixture(scope="session", autouse=True)
def initialize(request: FixtureRequest) -> Generator[None, None]:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    with patch("tortoise.contrib.test.getDBConfig", Mock(return_value=get_test_db_config())):
        initializer(modules=TORTOISE_APP_MODELS)
    yield
    finalizer()
    loop.close()


@pytest_asyncio.fixture(scope="session", autouse=True)
def event_loot() -> None:
    pass

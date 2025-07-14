from app.configs.base_config import Config


def get_config() -> Config:
    return Config(_env_file=".env", _env_file_encoding="utf-8")


config = get_config()

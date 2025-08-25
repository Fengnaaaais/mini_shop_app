from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class DBSettings(BaseModel):
    url: str
    echo: bool


class Settigns(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env", ".env.template"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="API__CONIFG__",
    )
    db: DBSettings

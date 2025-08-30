from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class AccessTokenSettings(BaseModel):
    token: str
    lifetime_seconds: int


class DBSettings(BaseModel):
    url: str
    echo: bool


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env.template", ".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="API__CONFIG__",
    )
    db: DBSettings
    access_token: AccessTokenSettings


settings = Settings()

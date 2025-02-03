import os
import yaml
from pydantic_settings import BaseSettings
from pydantic import BaseModel


class DBConfig(BaseModel):
    user: str
    password: str
    host: str
    port: str
    dbName: str


class InfraConfig(BaseModel):
    db: DBConfig


class SecretConfig(BaseModel):
    jwt: str


class ServerConfig(BaseModel):
    profile: str
    port: int


class Config(BaseModel):
    server: ServerConfig
    secret: SecretConfig
    infra: InfraConfig


def load_config(file_path: str) -> Config:
    with open(file_path, "r") as file:
        yaml_data = yaml.safe_load(file)
    return Config(**yaml_data)


print(os.path.dirname(os.path.abspath(__file__)) + "config.dev.yaml")

settings = load_config("config.yaml")

import os
import yaml
from pydantic_settings import BaseSettings
from pydantic import BaseModel
from pydantic import Field


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


class Settings(BaseSettings):
    server: ServerConfig = Field(default_factory=ServerConfig)
    secret: SecretConfig = Field(default_factory=SecretConfig)
    infra: InfraConfig = Field(default_factory=InfraConfig)

    @classmethod
    def from_yaml(cls, yaml_file: str):
        with open(yaml_file, "r") as file:
            yaml_data = yaml.safe_load(file)
        return cls(**yaml_data)


print(os.path.dirname(os.path.abspath(__file__)) + "config.dev.yaml")

settings = load_config("config.yaml")

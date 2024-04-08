from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    DB_TEST_HOST: str
    DB_TEST_USER: str
    DB_TEST_PASS: str
    DB_TEST_NAME: str

    # dev
    @property
    def DATABASE_URL_aiomysql(self):  # async
        # DSN
        return f"mysql+aiomysql://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}/{self.DB_NAME}"

    # test
    @property
    def TEST_DATABASE_URL_aiomysql(self):  # async
        # DSN
        return f"mysql+aiomysql://{self.DB_TEST_USER}:{self.DB_TEST_PASS}@{self.DB_TEST_HOST}/{self.DB_TEST_NAME}"
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

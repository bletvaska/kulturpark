from functools import cache
from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


@cache
class Settings(BaseSettings):
    broker: str = 'mosquitto'
    port: int = 1883
    user: str | None = None
    password: str | None = None
    topic_prefix: str = 'kulturpark/tapgame'
    idle_duration: int = 20
    inactive_view_duration: int = 5
    results_view_duration: int = 20
    error_view_duration: int = 30
    gameplay_duration: int = 60
    game_over_view_duration: int = 10
    gauss_bins: int = 9
    db_uri: str = 'sqlite:///db.sqlite'

    @computed_field
    @property
    def keyboard_topic(self) -> str:
        return f'{self.topic_prefix}/keyboard'
    
    @computed_field
    @property
    def screen_topic(self) -> str:
        return f'{self.topic_prefix}/screen'
    
    @computed_field
    @property
    def results_topic(self) -> str:
        return f'{self.topic_prefix}/results'
        
    @computed_field
    @property
    def backend_topic(self) -> str:
        return f'{self.topic_prefix}/backend'
    
    @computed_field
    @property
    def bridge_topic(self) -> str:
        return f'{self.topic_prefix}/bridge'

    model_config = SettingsConfigDict(
        env_prefix='TAPGAME_',
        env_file_encoding='utf-8',
        env_file='.env',
        extra='allow',
    )



@cache
def get_settings() -> Settings:
    return Settings()

class Config:
    """Common configurations."""

    SQLALCHEMY_DATABASE_URI = 'sqlite:///radio.db'


class DevelopmentConfig(Config):
    """Development configurations."""

    ENV = 'development'
    TESTING = True
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    """Production configurations."""

    ENV = 'production'
    TESTING = False
    DEBUG = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}

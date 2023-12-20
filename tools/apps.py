from django.apps import AppConfig
from django.conf import settings
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from numpy import load

class ToolsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tools'

    def ready(self):
        # Load the model and tokenizer on app startup
        self.model = load_model(settings.SENTIMENT_ANALYSIS_MODEL_PATH)
        self.tokenizer = Tokenizer()
        self.tokenizer.word_index = load(settings.TOKENIZER_WORD_INDEX_PATH, allow_pickle=True).item()
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from numpy import load

def predict_sentiment(new_review:str) -> str:
    # Load the saved model
    model = load_model('./ml_models/sentiment_analysis_model.h5')

    max_length = 200  

    # Initialize a tokenizer with the same settings used during training
    tokenizer = Tokenizer()

    # Load the vocabulary created during training
    tokenizer.word_index = load('./tokens/tokenizer_word_index.npy', allow_pickle=True).item()

    # Tokenize the new review
    sequences = tokenizer.texts_to_sequences([new_review])

    # Pad the sequences to the same length as used during training
    padded_sequences = pad_sequences(sequences, maxlen=max_length, padding='post', truncating='post')

    # Make predictions
    predictions = model.predict(padded_sequences)

    # Interpret predictions
    return 'positive' if predictions[0] > 0.5 else 'negative'

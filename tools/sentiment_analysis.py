from tensorflow.keras.preprocessing.sequence import pad_sequences

def predict_sentiment(model, tokenizer, new_review:str) -> str:
    max_length = 200  

    # Tokenize the new review
    sequences = tokenizer.texts_to_sequences([new_review])

    # Pad the sequences to the same length as used during training
    padded_sequences = pad_sequences(sequences, maxlen=max_length, padding='post', truncating='post')

    # Make predictions
    predictions = model.predict(padded_sequences)

    # Interpret predictions
    return 'positive' if predictions[0] > 0.5 else 'negative'

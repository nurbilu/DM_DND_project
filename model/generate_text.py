import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model

# Load the model and tokenizer
model = load_model('/dnd_model.h5')

# Recreate the tokenizer used in training
tokenizer = ...  # Load or recreate the tokenizer used in training
max_sequence_len = ...  # Set this to the value used in training
total_words = ...  # Set this to the value used in training

def generate_text(seed_text, next_words, max_sequence_len):
    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
        predicted = model.predict([token_list, np.random.random((1, 10))], verbose=0)  # Replace with actual structured input
        predicted_word_index = np.argmax(predicted, axis=1)[0]
        output_word = tokenizer.index_word[predicted_word_index]
        seed_text += " " + output_word
    return seed_text

print(generate_text("The dungeon is dark", 20, max_sequence_len))

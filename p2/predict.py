from .preprocess_audio import get_mel
import tensorflow as tf
from tensorflow import keras
from keras.layers import Layer
import numpy as np

class L1Dist(Layer):

    def __init__(self, **kwargs):
        super().__init__()

    def call(self, input_embedding, validation_embedding):
        return tf.math.abs(input_embedding - validation_embedding)


class VAuthModel:

    def __init__(self):
        self.embedder = tf.keras.models.load_model('p2/models/embedder_network_v2.h5')
        self.saimese = tf.keras.models.load_model('p2/models/saimese_v2.h5')
        self.threshold = 0.6  # 0.425 for v5

    def get_embeddings(self, mel):
        """
        Get the embeddings from the mel spectrogram
        """
        embeddings = self.embedder.predict(mel)

        return embeddings

    def predict(self, em1, em2):
        """
        Compares the two embeddings and returns True if the speakers are same
        """

        diff = tf.math.abs(em1 - em2)

        op = self.saimese.predict(diff)
        #print(op)

        if op < self.threshold:
            return True
        else:
            return False


if __name__ == '__main__':
    mel1 = get_mel('wav files/mel1.wav')
    mel2 = get_mel('wav files/mel3.wav')

    model = VAuthModel()

    em1 = model.get_embeddings(mel1)
    em2 = model.get_embeddings(mel2) 
    print(em1)   # em1 and em2 will go in the database

    result = model.predict(em1, em2)

    #print(result)

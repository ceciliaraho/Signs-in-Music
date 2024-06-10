# Signs-in-Music
Sign language translator in music for the course Creative Programming and Computing

## Abstract
Our project, "Signs-in-Music," aims to develop a graphic and audio translator of sign language to foster an emotional bond between hearing and deaf individuals. By translating sign language into music and visual art, we create an immersive artistic experience that reflects the emotional content expressed through sign language.

## Description
"Signs-in-Music" bridges the gap between deaf and hearing communities by transforming sign language into a multisensory experience. Using real-time video capture and hand gesture recognition, we translate specific signs into spoken English words. These words are then used to find corresponding songs through the Spotify API. The emotional features of these songs are extracted and used to generate a dynamic particle system, creating a visual representation of the emotion behind the sign.

## How to use
1. Run the Python code 

## How it works
1. Real-Time Video Capture and Gesture Recognition:
   * Dataset Creation (implemented in `main1.py` and `utils.py`): We created a custom dataset consisting of 10 specific signs: 'art', 'baby', 'cherry', 'hello', 'iloveyou', 'mommy', 'music', 'party', 'sun', and 'thanks'.
   * Model Training (implemented in `data_processing.py`): Using this dataset, we trained a neural network to recognize these gestures.
   * Neural Network Architecture:
     - Input Layer: Receives images of hand gestures.
     - Convolutional Layers: Extracts spatial features from the images using Conv1D layers.
       - First Conv1D layer: 32 filters, kernel size of 3, ReLU activation, L2 regularization.
       - MaxPooling1D layer: Pool size of 2.
       - BatchNormalization and Dropout (0.5) layers.
       - Second Conv1D layer: 64 filters, kernel size of 3, ReLU activation, L2 regularization.
       - MaxPooling1D layer: Pool size of 2.
       - BatchNormalization and Dropout (0.5) layers.
     - LSTM Layer: Extracts temporal features from the sequence of frames.
       - LSTM layer: 64 units, ReLU activation, L2 regularization.
       - Dropout (0.5) layer.
     - Dense Layers: Interprets the extracted features to classify the gestures
        - First Dense layer: 32 units, ReLU activation, L2 regularization, Dropout (0.5).
        - Output Dense layer: Softmax activation to classify into one of the 10 gestures.
   * Compilation: The model is compiled with Adam optimizer, categorical cross-entropy loss, and categorical accuracy metrics.

   * Python code (implemented in `analysis_visualization.py` and `utils.py`): Captures real-time video from a computer camera and uses the trained model to recognize hand gestures. Each gesture is associated with a corresponding label (e.g., 🤟 the gesture for "I love you").

3. Integration with Spotify API:
   * The recognized word is used to search for songs with the same word in their title.
   * One of the retrieved songs is selected for further processing.
4. Emotional Feature Extraction and Artistic Visualization:
   * The python code extracts the main emotional features of the selected song (e.g., sadness,
     movement).
   * A particle system is generated based on these features, creating an immersive visual artistic
     experience.
   * Parameters of the particle system change according to the extracted features, allowing users to
     visually perceive the emotional concept expressed through sign language.

## Technology
* Python: Used for real-time video capture and hand gesture recognition.
* OpenCV: A library for computer vision tasks, utilized for gesture recognition.
* TensorFlow or PyTorch: Machine learning frameworks used to train the gesture recognition model.
* Spotify API for Developers: Used to search for songs matching the recognized sign language words.
* Javascript: A flexible software sketchbook and a language for learning how to code within the context of the visual arts, used to create the particle system and visual effects based on the emotional content of the music.

## Authors
* Casale Lelio
* Raho Cecilia
* Sironi Alice

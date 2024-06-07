# Signs-in-Music
Sign language translator in music for the course Creative Programming and Computing

## Abstract
Our project, "Signs-in-Music," aims to develop a graphic and audio translator of sign language to foster an emotional bond between hearing and deaf individuals. By translating sign language into music and visual art, we create an immersive artistic experience that reflects the emotional content expressed through sign language.

## Description
"Signs-in-Music" bridges the gap between deaf and hearing communities by transforming sign language into a multisensory experience. Using real-time video capture and hand gesture recognition, we translate specific signs into spoken English words. These words are then used to find corresponding songs through the Spotify API. The emotional features of these songs are extracted and used to generate a dynamic particle system, creating a visual representation of the emotion behind the sign.

## How it works
1. Real-Time Video Capture and Gesture Recognition:
   * Python code captures real-time video from a computer camera.
   * Hand gestures are recognized and associated with corresponding labels (e.g., the gesture for "I
     love you").
2. Integration with Spotify API:
   * The recognized word is used to search for songs with the same word in their title.
   * One of the retrieved songs is selected for further processing.
3. Emotional Feature Extraction and Artistic Visualization:
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

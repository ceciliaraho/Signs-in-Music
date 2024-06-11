# Signs-in-Music
Sign language translator in music for the course Creative Programming and Computing

## Abstract
Our project, "Signs-in-Music," aims to develop a graphic and audio translator of sign language to foster an emotional bond between hearing and deaf individuals. By translating sign language into music and visual art, we create an immersive artistic experience that reflects the emotional content expressed through sign language.

## Description
"Signs-in-Music" bridges the gap between deaf and hearing communities by transforming sign language into a multisensory experience. Using real-time video capture and hand gesture recognition, we translate specific signs into spoken American words. These words are then used to find corresponding songs through the Spotify API. The emotional features of these songs are extracted and used to generate a dynamic particle system, creating a visual representation of the emotion behind the sign.

## How it works
1. HTML files: a web interface is developed using Flask, a Python micro-framework for web development.
   * `index.html`, serves as the main page of the application. It features a greeting message from Professor Ludwig Von Drake and a 'START' button that redirects users to the '/book' route upon clicking.
   * `book.html`, represents a digital dictionary containing sign language entries. Each sign language entry is presented on a separate page within a virtual book interface. Users can navigate through the dictionary by flipping pages, and each page provides a description and visual representation of a sign along with a 'TRY NOW' button.
Upon clicking the 'TRY NOW' button for a specific sign, an AJAX request is sent to the Flask server at the '/analysis' route with the corresponding sign identifier. This triggers the real-time sign recognition process, allowing users to interactively practice sign language gestures.

2. Real-Time Video Capture and Gesture Recognition:
   * Dataset Creation (implemented in `create_dataset.py` and `utils.py`): We created a custom dataset consisting of 10 specific signs: 'art', 'baby', 'cherry', 'hello', 'iloveyou', 'mommy', 'music', 'party', 'sun', and 'thanks'.
   * Model Training (implemented in `data_processing.py`): Using this dataset, we trained a neural network to recognize these gestures; Compilation: The model is compiled with Adam optimizer, categorical cross-entropy loss, and categorical accuracy metrics.

   * Python code (implemented in `main_analysis_visualization.py` and `utils.py`): Captures real-time video from a computer camera and uses the trained model to recognize hand gestures. Each gesture is associated with a corresponding label (e.g., 🤟 the gesture for "I love you").

3. Integration with Spotify API:
   * The recognized word is used to search for songs with the same word in their title.
   * One of the retrieved songs is selected for further processing.
4. Emotional Feature Extraction and Artistic Visualization:
   * The python code extracts the main features of the selected song (e.g., instantaneous energy, loudness, key).
   * A particle system is generated based on these features, creating an immersive visual artistic
     experience.
   * Parameters of the particle system change according to the extracted features, allowing users to
     visually perceive the emotional concept expressed through sign language.

## Technology
* HTML and CSS: Used for the graphical interface.
* Python: Used for real-time video capture and hand gesture recognition.
* Flask: It is a web framework for building web applications in Python, that allows users to interact with the sign recognition system.
* OpenCV: A library for computer vision tasks, utilized for gesture recognition.
* TensorFlow: Machine learning frameworks used to train the gesture recognition model.
* Spotify API for Developers: Used to search for songs matching the recognized sign language words.
* Javascript: A flexible software sketchbook and a language for learning how to code within the context of the visual arts, used to create the particle system and visual effects based on the emotional content of the music.

## Report
`Sign_in_Music.pdf`

## Authors
* Casale Lelio
* Raho Cecilia
* Sironi Alice

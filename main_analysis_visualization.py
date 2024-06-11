# analysis_and_visualization.py
import cv2
import numpy as np
import mediapipe as mp
from tensorflow import keras
from keras.layers import Dense
from keras.models import Sequential, load_model
from utils import mediapipe_detection, draw_styled_landmarks, extract_keypoints
import os
from flask import Flask, request, render_template, send_from_directory
from spoty_main import spotify_search
import webbrowser

client_id = "b3a47786876e4b3caf05c32b0bf2feea"
client_secret = "f7021e75f1144c0fa6ccade8bfbf8ce8"
query_limit = 10
path = "static/data/selectedSong.mp3"

app = Flask(__name__, static_folder='static')

webbrowser.open("http://localhost:5000")
@app.route('/')

def main():
    return render_template('main.html')

@app.route('/book')
def book():
    return render_template('book.html')

@app.route('/particle')
def particle():
    return render_template('index.html')

@app.route('/data/<path:filename>')
def serve_data(filename):
    return send_from_directory('static/data', filename)

@app.route('/analysis', methods=['POST'])
def analysis():
    # Get the current working directory
    data = request.get_json()
    my_string = data.get('myString')
    cwd = os.getcwd()

    # Construct the absolute path to the file
    file_path = os.path.join(cwd, 'action_new.h5')

    #  upload model
    model = load_model(file_path)

    mp_holistic = mp.solutions.holistic

    actions = np.array(['art', 'baby', 'cherry', 'hello', 'iloveyou', 'mommy', 'music', 'party', 'sun', 'thanks'])
    colors = [(245, 117, 16), (117, 245, 16), (16, 117, 245)]

    
    sequence = []
    sentence = []
    predictions = []
    threshold = 0.1

    # Webcam Configuration
    cap = cv2.VideoCapture(0)
    cv2.namedWindow('Webcam', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Webcam', cv2.WND_PROP_TOPMOST, 1)
    window_width = 1000  
    window_height = 650  
    cv2.resizeWindow('Webcam', window_width, window_height)


    # Set mediapipe model 
    with mp_holistic.Holistic(min_detection_confidence=0.4, min_tracking_confidence=0.4) as holistic:
        while cap.isOpened():
            # Read frame
            ret, frame = cap.read()

            # Mediapipe detection
            image, results = mediapipe_detection(frame, holistic)
            #print(results)

            # Draw landmarks
            draw_styled_landmarks(image, results)

            # Prevision
            keypoints = extract_keypoints(results)
            sequence.append(keypoints)
            sequence = sequence[-40:]
            #print(sequence)
            print(len(sequence))
            if len(sequence) == 40:
                res = model.predict(np.expand_dims(sequence, axis=0))[0]
                print(actions[np.argmax(res)])
                predictions.append(np.argmax(res))
                #print(sequence)

                if np.unique(predictions[-10:])[0] == np.argmax(res):
                    if res[np.argmax(res)] > threshold:
                        sentence = actions[np.argmax(res)]
                        if my_string == sentence:
                            print(sentence)
                            cv2.rectangle(image, (0, 0), (640, 40), (245, 117, 16), -1)
                            cv2.putText(image, ' '.join(sentence), (3,35), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
                            spotify_search(sentence, client_id, client_secret, query_limit, path)
                            cap.release()
                            cv2.destroyAllWindows()
                        else:
                            # Display a message on the frame
                            cv2.rectangle(image, (0, 0), (640, 40), (0, 0, 255), -1)
                            cv2.putText(image, 'Incorrect sign', (3, 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
                
            # frame visualization
            cv2.imshow('Webcam', image)

            # Break loop 
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        
        # close webcam 
        cap.release()
        cv2.destroyAllWindows()
        
    return 'Analysis completed'

if __name__ == '__main__':
    app.run(debug=True)




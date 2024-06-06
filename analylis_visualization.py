# analysis_and_visualization.py
import cv2
import numpy as np
import mediapipe as mp
from tensorflow.keras.models import load_model
from utils import mediapipe_detection, draw_styled_landmarks, extract_keypoints, prob_viz


#from spoty_main import spotify_search

#client_id = "b3a47786876e4b3caf05c32b0bf2feea"
#client_secret = "f7021e75f1144c0fa6ccade8bfbf8ce8"
#query_limit = 10
#path = "selectedSong.mp3"

# Carica il modello addestrato
model = load_model('action_new.h5')

mp_holistic = mp.solutions.holistic

# Configurazione
#actions = np.array(['hello', 'iloveyou', 'mommy', 'sun', 'thanks'])
actions = np.array(['art', 'baby', 'cherry', 'hello', 'iloveyou', 'mommy', 'music', 'party', 'sun', 'thanks'])
colors = [(245, 117, 16), (117, 245, 16), (16, 117, 245)]

# Variabili di rilevamento
sequence = []
sentence = []
predictions = []
threshold = 0.1

# Configurazione della webcam
cap = cv2.VideoCapture(0)

# Set mediapipe model 
with mp_holistic.Holistic(min_detection_confidence=0.4, min_tracking_confidence=0.4) as holistic:
    while cap.isOpened():
        # Leggi il frame dalla webcam
        ret, frame = cap.read()

        # Effettua la rilevazione con Mediapipe
        image, results = mediapipe_detection(frame, holistic)
        #print(results)

        # Disegna i landmarks
        draw_styled_landmarks(image, results)

        # Logica di previsione
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

            # Logica di visualizzazione
            if np.unique(predictions[-10:])[0] == np.argmax(res):
                if res[np.argmax(res)] > threshold:
                    if len(sentence) > 0: 
                        if actions[np.argmax(res)] != sentence[-1]:
                            sentence.append(actions[np.argmax(res)])
                            sentence = sentence[-5:]  # Mantieni solo le ultime 5 azioni uniche
                    else:
                        sentence.append(actions[np.argmax(res)])

            if len(sentence) > 5: 
                sentence = sentence[-5:]
            
             # Verifica se il numero di azioni rilevate supera il numero di colori definiti
            if len(actions) > len(colors):
            # Aggiungi colori aggiuntivi alla lista colors
                for _ in range(len(actions) - len(colors)):
                    colors.append((np.random.randint(0, 256), np.random.randint(0, 256), np.random.randint(0, 256)))

            # Viz probabilities
            image = prob_viz(res, actions, image, colors)
        

        cv2.rectangle(image, (0, 0), (640, 40), (245, 117, 16), -1)
        cv2.putText(image, ' '.join(sentence), (3,35), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
            
        # Visualizza il frame
        cv2.imshow('Live Video', image)

        # Interrompi il loop alla pressione del tasto 'q'
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    # Rilascia la webcam e chiudi le finestre
    cap.release()
    cv2.destroyAllWindows()






# utils.py
import cv2
import mediapipe as mp
import numpy as np 
import random

from scipy import stats

#actions = np.array(['art', 'baby', 'cherry', 'hello', 'iloveyou', 'mommy', 'music', 'party', 'sun', 'thanks'])
mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils

def mediapipe_detection(image, model):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False #image is no longer writeable
    results = model.process(image) 
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    return image, results

def draw_styled_landmarks(image, results): #draw hand connections
    # Draw pose connections
    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS,
                             mp_drawing.DrawingSpec(color=(80,22,10), thickness=2, circle_radius=4), 
                             mp_drawing.DrawingSpec(color=(80,44,121), thickness=2, circle_radius=2)
                             ) 
    mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS, 
                              mp_drawing.DrawingSpec(color=(80,110,10)),
                              mp_drawing.DrawingSpec(color=(80,256,121)) )
    mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

#def augment_keypoints(keypoints, aug_type):
    # Applica la trasformazione specificata ai keypoints
    #if aug_type == 'rotation':
      #  angle = random.uniform(-30, 30)  # Angolo di rotazione casuale tra -30 e 30 gradi
    #    rotation_matrix = np.array([[np.cos(np.radians(angle)), -np.sin(np.radians(angle))],
     #                               [np.sin(np.radians(angle)), np.cos(np.radians(angle))]])
       # keypoints = np.reshape(keypoints, (-1, 3))
        #keypoints[:, :2] = np.matmul(keypoints[:, :2], rotation_matrix.T)
        #keypoints = np.reshape(keypoints, (-1))
    # Aggiungi altre trasformazioni qui (traslazione, ridimensionamento, ecc.)
    #return keypoints

def extract_keypoints(results, aug_type=None):
    pose = np.array([[res.x, res.y, res.z, res.visibility] for res in results.pose_landmarks.landmark]).flatten() if results.pose_landmarks else np.zeros(33*4)
    lh = np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).flatten() if results.left_hand_landmarks else np.zeros(21*3) 
    rh = np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).flatten() if results.right_hand_landmarks else np.zeros(21*3) 
    keypoints= np.concatenate([pose, lh, rh])

    #aug_type = random.choice(['rotation', None])
    #keypoints = augment_keypoints(keypoints, aug_type)
    
    return keypoints



def prob_viz(res, actions, input_frame, colors):
    output_frame = input_frame.copy()
    for num, prob in enumerate(res):
        # Calcola la larghezza del rettangolo basata sulla probabilità
        rect_width = int(prob * 100)
        
        # Calcola la posizione del rettangolo e del testo
        rect_top_left = (0, 60 + num * 40)
        rect_bottom_right = (rect_width, 90 + num * 40)
        text_position = (5, 85 + num * 40)

        # Disegna il rettangolo colorato
        cv2.rectangle(output_frame, rect_top_left, rect_bottom_right, colors[num], -1)

        # Disegna il testo sull'azione
        cv2.putText(output_frame, actions[num], text_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        
    return output_frame


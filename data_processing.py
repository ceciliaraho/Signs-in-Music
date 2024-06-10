import os
import numpy as np
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout, BatchNormalization, Conv1D, MaxPooling1D, Flatten
from keras.callbacks import TensorBoard, EarlyStopping
from keras.optimizers import Adam
from keras.regularizers import l2
from sklearn.metrics import multilabel_confusion_matrix, accuracy_score

DATA_PATH = os.path.join('MP_Data')
actions = np.array(['art', 'baby', 'cherry', 'hello', 'iloveyou', 'mommy', 'music', 'party', 'sun', 'thanks'])
no_sequences = 30
sequence_length = 40

label_map = {label: num for num, label in enumerate(actions)}
sequences, labels = [], []
for action in actions:
    for sequence in np.array(os.listdir(os.path.join(DATA_PATH, action))).astype(int):
        window = []
        for frame_num in range(sequence_length):
            res = np.load(os.path.join(DATA_PATH, action, str(sequence), "{}.npy".format(frame_num)))
            noise = np.random.normal(0, 0.05, res.shape)
            res += noise
            window.append(res)
        sequences.append(window)
        labels.append(label_map[action])

X = np.array(sequences)
print(X.shape)
y = to_categorical(labels).astype(int)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, stratify=y)
print(y_test.shape)

import matplotlib.pyplot as plt

labels_count = np.sum(y, axis=0)
plt.bar(actions, labels_count)
plt.xlabel('Actions')
plt.ylabel('Number of samples')
plt.show()

# Save X_train e y_train in file numpy
np.save('X_train_new.npy', X_train)
np.save('y_train_new.npy', y_train)
np.save('X_test_new.npy', X_test)
np.save('y_test_new.npy', y_test)

log_dir = os.path.join('Logs')
tb_callback = TensorBoard(log_dir=log_dir)
early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)

model = Sequential() 
model.add(Conv1D(32, kernel_size=3, activation='relu', input_shape=(sequence_length, X.shape[2]), kernel_regularizer=l2(0.01)))
model.add(MaxPooling1D(pool_size=2))
model.add(BatchNormalization())
model.add(Dropout(0.5))
model.add(Conv1D(64, kernel_size=3, activation='relu', kernel_regularizer=l2(0.01)))
model.add(MaxPooling1D(pool_size=2))
model.add(BatchNormalization())
model.add(LSTM(64, return_sequences=False, activation='relu', kernel_regularizer=l2(0.01)))
model.add(Dropout(0.5))
model.add(Dense(32, activation='relu', kernel_regularizer=l2(0.01)))
model.add(Dropout(0.5))
model.add(Dense(actions.shape[0], activation='softmax'))

model.compile(optimizer=Adam(learning_rate=0.001), loss='categorical_crossentropy', metrics=['categorical_accuracy'])

history = model.fit(X_train, y_train, epochs=500, batch_size=32, validation_split=0.2, callbacks=[tb_callback, early_stopping])
model.summary()

res = model.predict(X_test)
print(actions[np.argmax(res[4])])
print(actions[np.argmax(y_test[4])])

#model.save('action2.h5')
model.save('action_new.h5')

yhat = model.predict(X_test)
ytrue = np.argmax(y_test, axis=1).tolist()
yhat = np.argmax(yhat, axis=1).tolist()
print(multilabel_confusion_matrix(ytrue, yhat))
print(accuracy_score(ytrue, yhat))

#Plot delle metriche di addestramento e validazione
plt.figure(figsize=(12, 4))
plt.subplot(1, 2, 1)
plt.plot(history.history['categorical_accuracy'], label='Training Accuracy')
plt.plot(history.history['val_categorical_accuracy'], label='Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()

plt.show()
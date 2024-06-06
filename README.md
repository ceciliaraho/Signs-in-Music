# Signs-in-Music
Sign language translator in music for the course Creative Programming and Computing

Our goal is to develop a graphic and audio translator of sign language, to form an emotional bond between hearing people and deaf people. This translator has the purpose to create a visual artistic experience that is correlated with the concept expressed through the sign language

The main parts used to create this project are:
- Python code to capture real time video and to recognize hand gestures from computer camera. Then each gesture is associated to a label which represents its translation in spoken English. (e.g. means “I love you”)
- Spotify API for Developers, to search songs that have the generated word in the title and select one of them.
- Processing to extract the main emotional features of the song (e.g. sadness, movement, …) and to create a particle system that allows the user to be immersed in an artistic experience that represents the emotional concept expressed by the user through the sign language. The parameters of the particle system are changed according to the features extracted from the song.

const comicTexts = [
  "Welcome to Signs in Music! I'll be your guide in this new world.",
  "Signs in Music is a graphic and audio translator of American Sign Language (ASL), that generates an emotional bond between hearing people and deaf people.",
  "You're probabily wondering \"How can I use this site if I don't know sign language?!\". Well... We have thought of everything!",
  "We have created a dictionary that contains brief explanations of how to correctly make the signs.",
  "The site will guide you through an interface that recognizes the sign language using a neural network and searches for a song with a name related to the gesture.",
  "Each sign will generate a graphical interface, whose characteristics change accordingly to the features of the selected song.",
  "I wouldn't want to spoil anything else, so... press start to enjoy the artistic experience!"
];

let index = 0;

document.addEventListener('keydown', function(event) {
  if (event.code === 'Space') {
    if (index < comicTexts.length - 1) {
      document.getElementById('comic-text').textContent = comicTexts[index];
      index++;
    } else if (index === comicTexts.length - 1) {
      document.getElementById('comic-text').textContent = comicTexts[index];
      index++;
      document.getElementById('start-button').classList.remove('hidden');
    }     
  }
});

## Pacman Party

## Description
This project is a Python-based implementation of the classic arcade game Pac-Man, developed using the Pygame library. The game features Pac-Man navigating through a maze, collecting food pellets, and avoiding ghosts. The objective is to eat all the pellets in the maze while avoiding the ghosts, which can be temporarily eaten when Pac-Man consumes a power pellet.

## Prerequisites
- Python 3.x
- Pip (Python package installer)
- Pygame (pip install pygame)

## Installation
Clone the repository:
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
python game.py

##Movement
Arrow keys

##Objective
Navigate through maze to maximize score, while simeltaneously avoiding ghosts

##How it Works
The Enemy class in the provided Pac-Man game code manages the behavior of the ghosts. Each ghost is initialized with a random direction and positioned within the maze. The update method controls their movement, where ghosts typically follow Pac-Man or flee when in "power mode." This behavior is influenced by a random chance mechanism. The ghosts change direction to avoid walls and follow paths in the maze.

If a ghost collides with Pac-Man, the game checks if Pac-Man is in "power mode." If so, the ghost is reset to a new position; otherwise, Pac-Man loses a life. The class also includes methods for resetting the ghost's position and switching between normal and scared states based on the game's power-up status.

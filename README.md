# A* Path Finding Visualizer

## 📖 About 
### An A* Path Finding interactive visualizer made with Pygame.


Project made with the purpose of studying [A\* search algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm), Python classes and functions and visual interaction with Pygame.


Project under [MIT License](LICENSE.txt).

## 📽️ Demos
<p align="center">
<img src="gifs/test.gif" alt="test" height=350>
<img src="gifs/test2.gif" alt="test1" height=350>
</p>

## 💻 Usage 

1. Run `main.py`:

    - `python main.py` if  Windows
    - `python3 main.py` if Linux/macOS

2. Interact with the display:
    
    - First `left click` sets the `start` node;
    - Second `left click` sets `end` node;
    - The other clicks sets the `barriers` nodes, i.e. blocked nodes that won't be able to be passed through;
    - Any node can be reseted with a `right click` on it;
    - Press `space` to start the algorithm;
    - Pressing `c` resets it all.

3. The quantity of nodes can be changed applying other values to the `ROWS` constant in `main.py` file. The standard is set to `40`.


## ⚙️ Setup
First, clone this repo with:

`git clone https://github.com/cauabernardino/astar_pathfinding`

Then install the requirements:

- For Windows: `pip install -r requirements.txt`
- For Linux/macOS: `pip3 install -r requirements.txt`

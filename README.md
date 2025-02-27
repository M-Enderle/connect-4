# Connect-4 🎮

<div align="center">

![Connect 4 Game](https://img.shields.io/badge/Game-Connect%204-red)
![Python](https://img.shields.io/badge/Python-3.6+-blue)
![License](https://img.shields.io/badge/License-MIT-green)

</div>

A command-line implementation of the classic Connect 4 game with multiple game modes, including AI opponents!

<div align="center">
  
```
+-----+-----+-----+-----+-----+-----+-----+
|  1  |  2  |  3  |  4  |  5  |  6  |  7  |
+=====+=====+=====+=====+=====+=====+=====+
|     |     |     |     |     |     |     |
+-----+-----+-----+-----+-----+-----+-----+
|     |     |     |     |     |     |     |
+-----+-----+-----+-----+-----+-----+-----+
|     |     |     |     |     |     |     |
+-----+-----+-----+-----+-----+-----+-----+
|     |     |  ○  |  x  |     |     |     |
+-----+-----+-----+-----+-----+-----+-----+
|     |  ○  |  x  |  ○  |     |     |     |
+-----+-----+-----+-----+-----+-----+-----+
|  x  |  x  |  ○  |  ○  |  x  |     |     |
+-----+-----+-----+-----+-----+-----+-----+
```

</div>

## ✨ Features

- 🎲 Multiple game modes:
  - Human vs Human
  - Human vs AI
  - AI vs AI (watch the computers battle!)
- 💾 Save and load game functionality
- 🤖 AI opponent with strategic gameplay
- 📋 Simple and intuitive terminal-based interface

## 🚀 Installation

### Option 1: Standard Installation

```bash
# Clone this repository
git clone https://github.com/M-Enderle/connect-4.git

# Change to the project directory
cd connect-4

# Install required dependencies
pip install -r requirements.txt
```

### Option 2: Docker

```bash
# Build the Docker image
docker build -t connect-4 .

# Run the container
docker run -i connect-4
```

### Option 3: Docker Compose

```bash
# Run with Docker Compose
docker-compose run connect-4
```

## 🎮 Usage

Start the game by running:

```bash
python -m connect_4.main
```

### Controls

- Use the displayed menu to navigate through options
- Select columns by entering the corresponding number (1-7)
- Follow on-screen prompts to play, save, or load games

## 🎯 Game Rules

1. Players take turns dropping colored discs into a 7-column, 6-row grid
2. The pieces fall straight down, occupying the lowest available space in the column
3. The objective is to be the first to form a horizontal, vertical, or diagonal line of four discs
4. The game ends when a player connects four discs or when the board is full (draw)

## 🔧 Development

This project was developed as part of a Software Engineering course in the 4th semester at Deggendorf Institute of Technology.

## 📄 License

MIT License - See LICENSE file for details

---

<div align="center">
  Made with ❤️ by Moritz Enderle
</div>
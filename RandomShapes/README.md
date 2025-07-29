# Baby Games 🎮

An interactive keyboard game designed for babies who love to press keys and watch colorful shapes appear on the screen!

## Features

- **Full-screen immersive experience** - Takes over the entire screen for maximum engagement
- **Diverse shape types** - Circles, squares, triangles, stars, hearts, diamonds, and many more
- **Rich color palette** - Different key types produce different color families
- **Smooth animations** - Shapes move, rotate, and scale dynamically
- **Particle effects** - Special effects for fireworks, sparkles, and explosions
- **Safe exit** - Press `Ctrl+Shift+C` to exit the game safely

## Key Mappings

### Letter Keys (A-Z)
- Create basic shapes with bright, vibrant colors
- Colors: Red, Blue, Green, Yellow, Purple, Orange, Pink, Cyan

### Number Keys (0-9)
- Create special themed shapes
- Colors: Gold, Silver, Bronze, Emerald, Ruby, Sapphire, Amethyst, Topaz

### Special Keys
- **Space**: Explosion effect
- **Enter**: Burst pattern
- **Tab**: Spiral
- **Backspace**: Fade effect
- **Escape**: Shimmer effect

### Arrow Keys
- Create directional shapes with elemental colors
- Colors: Electric, Fire, Ice, Earth, Wind, Light, Dark, Cosmic

## Setup Instructions

1. **Create and activate virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the game:**
   ```bash
   python main.py
   ```

## How to Play

1. Start the game - it will go full-screen automatically
2. Press any key to create colorful shapes
3. Watch as shapes move, rotate, and interact on screen
4. Press `Ctrl+Shift+C` to exit the game

## Architecture

The game is built with a modular architecture for easy maintenance:

- **`main.py`** - Main game loop and entry point
- **`display.py`** - Full-screen display management
- **`input_handler.py`** - Keyboard input processing and key mappings
- **`shapes.py`** - Shape definitions and drawing methods
- **`shape_manager.py`** - Shape lifecycle and management
- **`animation_manager.py`** - Animation and particle effects

## Technical Details

- **Framework**: Pygame 2.5.2
- **Python**: 3.10+
- **Display**: Full-screen mode
- **Performance**: Optimized for smooth 60 FPS gameplay
- **Memory Management**: Automatic cleanup of old shapes to prevent memory issues

## Safety Features

- **Automatic shape cleanup** - Shapes disappear after 10 seconds
- **Performance limits** - Maximum 50 shapes on screen at once
- **Safe exit combination** - `Ctrl+Shift+C` to exit without force-quitting
- **Edge bouncing** - Shapes bounce off screen edges instead of disappearing

## Customization

You can easily customize the game by modifying:

- **Colors**: Edit the color mappings in `input_handler.py`
- **Shapes**: Add new shape types in `shapes.py`
- **Effects**: Modify particle effects in `animation_manager.py`
- **Key mappings**: Change which keys create which shapes in `input_handler.py`

## Troubleshooting

- **Game won't start**: Make sure pygame is installed and you're in the virtual environment
- **Full-screen issues**: Try running with `python main.py` from terminal
- **Performance issues**: The game automatically limits shapes, but you can reduce `max_shapes` in `shape_manager.py`

Enjoy watching your baby discover the magic of interactive computing! 🎉
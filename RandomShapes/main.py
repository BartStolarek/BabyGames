#!/usr/bin/env python3
"""
Baby Games - Interactive Keyboard Game
A fun game for babies to press keys and watch colorful shapes appear!
"""

import sys
import pygame
from display import Display
from input_handler import InputHandler
from shape_manager import ShapeManager
from animation_manager import AnimationManager


class BabyGame:
    def __init__(self):
        """Initialize the baby game."""
        pygame.init()
        self.display = Display()
        self.input_handler = InputHandler()
        self.shape_manager = ShapeManager()
        self.animation_manager = AnimationManager()
        
        # Set screen bounds for shape manager
        width, height = self.display.get_screen_bounds()
        self.shape_manager.set_screen_bounds(width, height)
        
        self.running = True
        self.clock = pygame.time.Clock()
        
    def run(self):
        """Main game loop."""
        print("🎮 Baby Games started! Press any key to create shapes!")
        print("💡 Press Ctrl+Shift+C to exit the game")
        
        while self.running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    self.handle_key_press(event)
            
            # Update animations and shapes
            self.animation_manager.update()
            self.shape_manager.update()
            
            # Render everything
            self.display.clear()
            self.shape_manager.draw(self.display.screen)
            self.animation_manager.draw_particles(self.display.screen)
            self.display.update()
            
            # Cap the frame rate
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()
    
    def handle_key_press(self, event):
        """Handle keyboard input and create shapes."""
        # Check for exit combination (Ctrl+Shift+C)
        if (event.key == pygame.K_c and 
            pygame.key.get_mods() & pygame.KMOD_CTRL and 
            pygame.key.get_mods() & pygame.KMOD_SHIFT):
            print("👋 Goodbye! Thanks for playing!")
            self.running = False
            return
        
        # Create a new shape for any other key press
        shape = self.shape_manager.create_shape_from_key(event.key)
        if shape:
            self.animation_manager.add_shape(shape)
            print(f"✨ Created {shape.shape_type} with color {shape.color_name}!")


def main():
    """Main entry point."""
    try:
        game = BabyGame()
        game.run()
    except KeyboardInterrupt:
        print("\n👋 Game interrupted. Goodbye!")
        pygame.quit()
        sys.exit()
    except Exception as e:
        print(f"❌ Error: {e}")
        pygame.quit()
        sys.exit(1)


if __name__ == "__main__":
    main()
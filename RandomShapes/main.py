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
        print("🖱️  Mouse buttons create special effects:")
        print("   Left click: Rainbow trail")
        print("   Middle click: Expanding circles")
        print("   Right click: Star burst")
        print("   Side button 1: Spiral effect")
        print("   Side button 2: Fireworks")
        print("   Side button 3: Butterfly swarm")
        print("   Side button 4: Cosmic portal")
        
        last_time = pygame.time.get_ticks()
        
        try:
            while self.running:
                current_time = pygame.time.get_ticks()
                dt = current_time - last_time
                last_time = current_time
                
                # Get current mouse position
                mouse_pos = pygame.mouse.get_pos()
                
                # Handle events
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                    elif event.type == pygame.KEYDOWN:
                        self.handle_key_press(event)
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        self.handle_mouse_click(event)
                
                # Update animations and shapes
                self.animation_manager.update()
                self.shape_manager.update()
                self.shape_manager.update_mouse_tail(mouse_pos, dt)
                
                # Render everything
                self.display.clear()
                self.shape_manager.draw(self.display.screen)
                self.shape_manager.draw_mouse_tail(self.display.screen)
                self.animation_manager.draw_particles(self.display.screen)
                self.display.update()
                
                # Cap the frame rate
                self.clock.tick(60)
        finally:
            # Clean up resources
            self.shape_manager.cleanup()
        
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
    
    def handle_mouse_click(self, event):
        """Handle mouse button clicks and create special effects."""
        button = event.button
        mouse_pos = event.pos
        
        # Get action description
        action_desc = self.input_handler.get_mouse_action_description(button)
        print(f"🖱️  Mouse button {button} pressed at {mouse_pos}: {action_desc}")
        
        # Handle the mouse action
        self.shape_manager.handle_mouse_action(button, mouse_pos)


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
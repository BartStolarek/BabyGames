"""
Display module for Baby Games
Handles full-screen window creation and rendering.
"""

import pygame


class Display:
    def __init__(self):
        """Initialize the full-screen display."""
        # Get display info
        info = pygame.display.Info()
        self.width = info.current_w
        self.height = info.current_h
        
        # Set up full-screen display
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
        pygame.display.set_caption("Baby Games - Press any key!")
        
        # Set up colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        
        # Hide mouse cursor for full immersion
        pygame.mouse.set_visible(False)
        
        print(f"🖥️  Full-screen display initialized: {self.width}x{self.height}")
    
    def clear(self):
        """Clear the screen with black background."""
        self.screen.fill(self.BLACK)
    
    def update(self):
        """Update the display."""
        pygame.display.flip()
    
    def get_center(self):
        """Get the center point of the screen."""
        return (self.width // 2, self.height // 2)
    
    def get_random_position(self):
        """Get a random position on the screen."""
        import random
        return (random.randint(50, self.width - 50), 
                random.randint(50, self.height - 50))
    
    def get_screen_bounds(self):
        """Get the screen bounds for shape positioning."""
        return (self.width, self.height)
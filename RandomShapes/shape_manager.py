"""
Shape Manager module for Baby Games
Handles shape creation, management, and lifecycle.
"""

import random
import pygame
from shapes import Shape
from input_handler import InputHandler


class ShapeManager:
    def __init__(self):
        """Initialize the shape manager."""
        self.shapes = []
        self.input_handler = InputHandler()
        self.max_shapes = 50  # Limit to prevent performance issues
        self.shape_lifetime = 10000  # 10 seconds in milliseconds
        self.screen_width = 1920  # Default, will be updated
        self.screen_height = 1080  # Default, will be updated
        
    def set_screen_bounds(self, width, height):
        """Set the screen bounds for shape positioning."""
        self.screen_width = width
        self.screen_height = height
        
    def create_shape_from_key(self, key):
        """Create a new shape based on the pressed key."""
        # Get shape type and color from input handler
        shape_type = self.input_handler.get_shape_type(key)
        available_colors = self.input_handler.get_available_colors(key)
        color_name = random.choice(available_colors)
        
        # Get random position (avoid edges)
        margin = 100
        x = random.randint(margin, self.screen_width - margin)
        y = random.randint(margin, self.screen_height - margin)
        
        # Random size between 30 and 100
        size = random.randint(30, 100)
        
        # Create the shape
        shape = Shape(shape_type, color_name, x, y, size)
        
        # Add to shapes list
        self.shapes.append(shape)
        
        # Clean up old shapes if we have too many
        self.cleanup_old_shapes()
        
        return shape
    
    def cleanup_old_shapes(self):
        """Remove shapes that are too old or if we have too many."""
        current_time = pygame.time.get_ticks()
        
        # Remove shapes older than lifetime
        self.shapes = [shape for shape in self.shapes 
                      if current_time - shape.creation_time < self.shape_lifetime]
        
        # If still too many shapes, remove oldest ones
        if len(self.shapes) > self.max_shapes:
            # Sort by creation time and keep only the newest ones
            self.shapes.sort(key=lambda s: s.creation_time, reverse=True)
            self.shapes = self.shapes[:self.max_shapes]
    
    def update(self):
        """Update all shapes."""
        for shape in self.shapes:
            shape.update()
            
            # Bounce off screen edges using actual screen dimensions
            if shape.x <= 0 or shape.x >= self.screen_width:
                shape.velocity_x *= -1
            if shape.y <= 0 or shape.y >= self.screen_height:
                shape.velocity_y *= -1
        
        # Clean up old shapes
        self.cleanup_old_shapes()
    
    def draw(self, screen):
        """Draw all shapes."""
        for shape in self.shapes:
            shape.draw(screen)
    
    def clear_all(self):
        """Clear all shapes."""
        self.shapes.clear()
    
    def get_shape_count(self):
        """Get the current number of shapes."""
        return len(self.shapes)
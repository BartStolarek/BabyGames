"""
Shape Manager module for Baby Games
Handles shape creation, management, and lifecycle.
"""

import random
import pygame
from shapes import Shape
from input_handler import InputHandler
from sound_manager import SoundManager
from particle_system import ParticleSystem


class ShapeManager:
    def __init__(self):
        """Initialize the shape manager."""
        self.shapes = []
        self.input_handler = InputHandler()
        self.sound_manager = SoundManager()
        self.particle_system = ParticleSystem()
        self.max_shapes = 10  # Limit to 10 shapes as requested
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
        
        # Check if we need to remove the oldest shape before adding new one
        if len(self.shapes) >= self.max_shapes:
            print(f"🎯 Shape limit reached ({self.max_shapes})! Removing oldest shape...")
            self.remove_oldest_shape_with_pop()
        
        # Add to shapes list
        self.shapes.append(shape)
        
        # Debug info
        print(f"✨ Created {shape.shape_type} with color {shape.color_name}! Total shapes: {len(self.shapes)}")
        
        # Play a baby-friendly sound
        self.sound_manager.play_shape_sound()
        
        return shape
    
    def remove_oldest_shape_with_pop(self):
        """Remove the oldest shape with a popping animation."""
        if not self.shapes:
            return
            
        # Find the oldest shape
        oldest_shape = min(self.shapes, key=lambda s: s.creation_time)
        
        # Create popping effect at the shape's position
        self.particle_system.create_pop_effect(
            oldest_shape.x, 
            oldest_shape.y, 
            oldest_shape.color,
            num_particles=20
        )
        
        # Remove the oldest shape
        self.shapes.remove(oldest_shape)
        
        # Debug info
        print(f"💥 Popped oldest {oldest_shape.shape_type} at ({oldest_shape.x:.0f}, {oldest_shape.y:.0f})! Shapes remaining: {len(self.shapes)}")
        
        # Play a pop sound (if available)
        # self.sound_manager.play_pop_sound()  # Uncomment if you add this method
    
    def cleanup_old_shapes(self):
        """Remove shapes that are too old."""
        current_time = pygame.time.get_ticks()
        
        # Remove shapes older than lifetime
        shapes_to_remove = []
        for shape in self.shapes:
            if current_time - shape.creation_time >= self.shape_lifetime:
                shapes_to_remove.append(shape)
        
        # Remove old shapes with pop effect
        for shape in shapes_to_remove:
            self.particle_system.create_pop_effect(
                shape.x, 
                shape.y, 
                shape.color,
                num_particles=15
            )
            self.shapes.remove(shape)
    
    def update(self):
        """Update all shapes and particles."""
        for shape in self.shapes:
            shape.update()
            
            # Bounce off screen edges using actual screen dimensions
            if shape.x <= 0 or shape.x >= self.screen_width:
                shape.velocity_x *= -1
            if shape.y <= 0 or shape.y >= self.screen_height:
                shape.velocity_y *= -1
        
        # Update particle system
        self.particle_system.update()
        
        # Clean up old shapes
        self.cleanup_old_shapes()
    
    def draw(self, screen):
        """Draw all shapes and particles."""
        # Draw shapes first
        for shape in self.shapes:
            shape.draw(screen)
        
        # Draw particles on top
        self.particle_system.draw(screen)
    
    def clear_all(self):
        """Clear all shapes and particles."""
        self.shapes.clear()
        self.particle_system.clear_all()
    
    def get_shape_count(self):
        """Get the current number of shapes."""
        return len(self.shapes)
    
    def get_particle_count(self):
        """Get the current number of particles."""
        return self.particle_system.get_particle_count()
    
    def cleanup(self):
        """Clean up resources."""
        self.sound_manager.cleanup()
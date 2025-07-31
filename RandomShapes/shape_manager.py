"""
Shape Manager module for Baby Games
Handles shape creation, management, and lifecycle.
"""

import random
import math
import pygame
from shapes import Shape
from input_handler import InputHandler
from sound_manager import SoundManager
from particle_system import ParticleSystem
from mouse_tail import MouseTail


class ShapeManager:
    def __init__(self):
        """Initialize the shape manager."""
        self.shapes = []
        self.input_handler = InputHandler()
        self.sound_manager = SoundManager()
        self.particle_system = ParticleSystem()
        self.mouse_tail = MouseTail(max_length=35)
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
    
    def handle_mouse_action(self, button, mouse_pos):
        """Handle mouse button actions."""
        action = self.input_handler.get_mouse_action(button)
        x, y = mouse_pos
        
        if action == "rainbow_trail":
            self.create_rainbow_trail_effect(x, y)
        elif action == "middle_click":
            self.create_expanding_circles(x, y)
        elif action == "right_click":
            self.create_star_burst(x, y)
        elif action == "side_button_1":
            self.create_spiral_effect(x, y)
        elif action == "side_button_2":
            self.create_fireworks(x, y)
        elif action == "side_button_3":
            self.create_butterfly_swarm(x, y)
        elif action == "side_button_4":
            self.create_cosmic_portal(x, y)
        
        # Play sound for any mouse action
        self.sound_manager.play_shape_sound()
    
    def create_rainbow_trail_effect(self, x, y):
        """Create a rainbow trail effect at the given position."""
        colors = ["red", "orange", "yellow", "green", "blue", "purple"]
        for i, color in enumerate(colors):
            # Create shapes in a trail pattern
            trail_x = x + i * 20
            trail_y = y + i * 10
            shape = Shape("circle", color, trail_x, trail_y, 20 + i * 5)
            self.shapes.append(shape)
            print(f"🌈 Created rainbow trail shape {i+1}!")
    
    def create_expanding_circles(self, x, y):
        """Create expanding circles from the mouse position."""
        for i in range(5):
            size = 30 + i * 15
            shape = Shape("circle", "cyan", x, y, size)
            shape.velocity_x = 0  # Keep circles centered
            shape.velocity_y = 0
            self.shapes.append(shape)
            print(f"⭕ Created expanding circle {i+1}!")
    
    def create_star_burst(self, x, y):
        """Create a star burst explosion."""
        for i in range(8):
            angle = i * 45  # 8 directions
            distance = 50
            star_x = x + distance * math.cos(math.radians(angle))
            star_y = y + distance * math.sin(math.radians(angle))
            shape = Shape("star", "gold", star_x, star_y, 25)
            self.shapes.append(shape)
            print(f"⭐ Created star burst {i+1}!")
    
    def create_spiral_effect(self, x, y):
        """Create a spiral effect around the mouse position."""
        for i in range(12):
            angle = i * 30
            radius = 20 + i * 8
            spiral_x = x + radius * math.cos(math.radians(angle))
            spiral_y = y + radius * math.sin(math.radians(angle))
            shape = Shape("spiral", "magenta", spiral_x, spiral_y, 20)
            self.shapes.append(shape)
            print(f"🌀 Created spiral effect {i+1}!")
    
    def create_fireworks(self, x, y):
        """Create fireworks effect at the mouse position."""
        colors = ["red", "blue", "green", "yellow", "purple", "orange"]
        for i in range(10):
            # Random position around the center
            offset_x = random.randint(-30, 30)
            offset_y = random.randint(-30, 30)
            color = random.choice(colors)
            shape = Shape("fireworks", color, x + offset_x, y + offset_y, 15)
            self.shapes.append(shape)
            print(f"🎆 Created firework {i+1}!")
    
    def create_butterfly_swarm(self, x, y):
        """Create a beautiful butterfly swarm effect."""
        colors = ["pink", "purple", "cyan", "yellow", "orange", "magenta"]
        for i in range(8):
            # Create butterflies in a circular pattern
            angle = i * 45
            distance = 40 + i * 10
            butterfly_x = x + distance * math.cos(math.radians(angle))
            butterfly_y = y + distance * math.sin(math.radians(angle))
            color = random.choice(colors)
            shape = Shape("butterfly", color, butterfly_x, butterfly_y, 25)
            self.shapes.append(shape)
            print(f"🦋 Created butterfly {i+1}!")
    
    def create_cosmic_portal(self, x, y):
        """Create a cosmic portal effect."""
        portal_colors = ["cosmic", "neon", "crystal", "shimmer", "metallic"]
        for i in range(6):
            # Create portal rings
            ring_radius = 30 + i * 15
            for j in range(8):
                angle = j * 45
                portal_x = x + ring_radius * math.cos(math.radians(angle))
                portal_y = y + ring_radius * math.sin(math.radians(angle))
                color = portal_colors[i % len(portal_colors)]
                shape = Shape("spiral", color, portal_x, portal_y, 20 - i * 2)
                self.shapes.append(shape)
            print(f"🌀 Created cosmic portal ring {i+1}!")
    
    def update_mouse_tail(self, mouse_pos, dt):
        """Update the mouse tail with current mouse position."""
        self.mouse_tail.update(mouse_pos, dt)
    
    def draw_mouse_tail(self, screen):
        """Draw the mouse tail."""
        self.mouse_tail.draw(screen)
    
    def cleanup(self):
        """Clean up resources."""
        self.sound_manager.cleanup()
"""
Animation Manager module for Baby Games
Handles shape animations and special effects.
"""

import pygame
import random


class AnimationManager:
    def __init__(self):
        """Initialize the animation manager."""
        self.animations = []
        self.particle_systems = []
        
    def add_shape(self, shape):
        """Add a shape to be animated."""
        # Add some special effects based on shape type
        if shape.shape_type in ["fireworks", "explosion", "burst"]:
            self.create_explosion_effect(shape.x, shape.y, shape.color)
        elif shape.shape_type in ["sparkle", "shimmer"]:
            self.create_sparkle_effect(shape.x, shape.y, shape.color)
        elif shape.shape_type in ["rainbow", "sun", "moon"]:
            self.create_glow_effect(shape.x, shape.y, shape.color)
    
    def create_explosion_effect(self, x, y, color):
        """Create an explosion particle effect."""
        particles = []
        for i in range(20):
            particle = {
                'x': x,
                'y': y,
                'vx': random.uniform(-8, 8),
                'vy': random.uniform(-8, 8),
                'life': 60,
                'max_life': 60,
                'color': color,
                'size': random.randint(2, 6)
            }
            particles.append(particle)
        
        self.particle_systems.append({
            'particles': particles,
            'type': 'explosion'
        })
    
    def create_sparkle_effect(self, x, y, color):
        """Create a sparkle effect."""
        particles = []
        for i in range(10):
            particle = {
                'x': x + random.randint(-20, 20),
                'y': y + random.randint(-20, 20),
                'vx': random.uniform(-2, 2),
                'vy': random.uniform(-2, 2),
                'life': 30,
                'max_life': 30,
                'color': color,
                'size': random.randint(1, 3)
            }
            particles.append(particle)
        
        self.particle_systems.append({
            'particles': particles,
            'type': 'sparkle'
        })
    
    def create_glow_effect(self, x, y, color):
        """Create a glow effect around shapes."""
        particles = []
        for i in range(8):
            angle = i * (2 * 3.14159 / 8)
            particle = {
                'x': x + 30 * pygame.math.Vector2(1, 0).rotate(angle * 180 / 3.14159)[0],
                'y': y + 30 * pygame.math.Vector2(1, 0).rotate(angle * 180 / 3.14159)[1],
                'vx': 0,
                'vy': 0,
                'life': 45,
                'max_life': 45,
                'color': color,
                'size': random.randint(3, 8)
            }
            particles.append(particle)
        
        self.particle_systems.append({
            'particles': particles,
            'type': 'glow'
        })
    
    def update(self):
        """Update all animations and particle systems."""
        # Update particle systems
        for system in self.particle_systems[:]:
            for particle in system['particles'][:]:
                # Update position
                particle['x'] += particle['vx']
                particle['y'] += particle['vy']
                
                # Update life
                particle['life'] -= 1
                
                # Remove dead particles
                if particle['life'] <= 0:
                    system['particles'].remove(particle)
            
            # Remove empty particle systems
            if not system['particles']:
                self.particle_systems.remove(system)
    
    def draw_particles(self, screen):
        """Draw all particle effects."""
        for system in self.particle_systems:
            for particle in system['particles']:
                # Calculate alpha based on life
                alpha = int((particle['life'] / particle['max_life']) * 255)
                
                # Create color with alpha
                color_with_alpha = (*particle['color'], alpha)
                
                # Create surface for particle
                particle_surface = pygame.Surface((particle['size'] * 2, particle['size'] * 2), pygame.SRCALPHA)
                pygame.draw.circle(particle_surface, color_with_alpha, 
                                 (particle['size'], particle['size']), particle['size'])
                
                # Draw to screen
                screen.blit(particle_surface, 
                           (particle['x'] - particle['size'], particle['y'] - particle['size']))
    
    def clear_all(self):
        """Clear all animations and particle systems."""
        self.animations.clear()
        self.particle_systems.clear()
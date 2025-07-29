"""
Particle System module for Baby Games
Handles particle effects for shape popping animations.
"""

import pygame
import random
import math


class Particle:
    def __init__(self, x, y, color, particle_type="circle"):
        """Initialize a particle with position, color, and type."""
        self.x = x
        self.y = y
        self.color = color
        self.particle_type = particle_type
        
        # Random velocity for explosion effect
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(2, 8)
        self.velocity_x = math.cos(angle) * speed
        self.velocity_y = math.sin(angle) * speed
        
        # Particle properties
        self.size = random.randint(3, 8)
        self.lifetime = random.randint(30, 60)  # frames
        self.max_lifetime = self.lifetime
        self.alpha = 255
        self.rotation = random.uniform(0, 360)
        self.rotation_speed = random.uniform(-10, 10)
        
    def update(self):
        """Update particle position and properties."""
        self.x += self.velocity_x
        self.y += self.velocity_y
        
        # Slow down over time
        self.velocity_x *= 0.95
        self.velocity_y *= 0.95
        
        # Update rotation
        self.rotation += self.rotation_speed
        
        # Update lifetime and alpha
        self.lifetime -= 1
        if self.lifetime > 0:
            self.alpha = int(255 * (self.lifetime / self.max_lifetime))
        
    def is_alive(self):
        """Check if particle is still alive."""
        return self.lifetime > 0
    
    def draw(self, screen):
        """Draw the particle on screen."""
        if self.alpha <= 0:
            return
            
        # Create surface with alpha
        surface = pygame.Surface((self.size * 2, self.size * 2), pygame.SRCALPHA)
        
        # Create color with alpha
        color_with_alpha = (*self.color, self.alpha)
        
        # Draw based on particle type
        if self.particle_type == "circle":
            pygame.draw.circle(surface, color_with_alpha, (self.size, self.size), self.size)
        elif self.particle_type == "star":
            self.draw_star(surface, self.size, self.size, self.size, color_with_alpha)
        elif self.particle_type == "sparkle":
            self.draw_sparkle(surface, self.size, self.size, self.size, color_with_alpha)
        elif self.particle_type == "square":
            rect = pygame.Rect(0, 0, self.size * 2, self.size * 2)
            pygame.draw.rect(surface, color_with_alpha, rect)
        else:
            # Default to circle
            pygame.draw.circle(surface, color_with_alpha, (self.size, self.size), self.size)
        
        # Rotate if needed
        if self.rotation != 0:
            surface = pygame.transform.rotate(surface, self.rotation)
        
        # Get rect for positioning
        rect = surface.get_rect(center=(int(self.x), int(self.y)))
        
        # Draw to screen
        screen.blit(surface, rect)
    
    def draw_star(self, surface, x, y, size, color):
        """Draw a star particle."""
        points = []
        for i in range(5):
            angle = i * 2 * math.pi / 5
            radius = size if i % 2 == 0 else max(1, size // 2)
            points.append((x + radius * math.cos(angle), y + radius * math.sin(angle)))
        pygame.draw.polygon(surface, color, points)
    
    def draw_sparkle(self, surface, x, y, size, color):
        """Draw a sparkle particle."""
        for i in range(4):
            angle = i * math.pi / 2
            end_x = x + size * math.cos(angle)
            end_y = y + size * math.sin(angle)
            pygame.draw.line(surface, color, (x, y), (end_x, end_y), 2)


class ParticleSystem:
    def __init__(self):
        """Initialize the particle system."""
        self.particles = []
        
    def create_pop_effect(self, x, y, color, num_particles=15):
        """Create a popping effect at the given position."""
        particle_types = ["circle", "star", "sparkle", "square"]
        
        for _ in range(num_particles):
            particle_type = random.choice(particle_types)
            particle = Particle(x, y, color, particle_type)
            self.particles.append(particle)
    
    def update(self):
        """Update all particles."""
        # Update existing particles
        for particle in self.particles:
            particle.update()
        
        # Remove dead particles
        self.particles = [p for p in self.particles if p.is_alive()]
    
    def draw(self, screen):
        """Draw all particles."""
        for particle in self.particles:
            particle.draw(screen)
    
    def get_particle_count(self):
        """Get the current number of particles."""
        return len(self.particles)
    
    def clear_all(self):
        """Clear all particles."""
        self.particles.clear()
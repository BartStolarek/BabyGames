"""
Mouse Tail module for Baby Games
Creates a glowing tail that follows the mouse cursor.
"""

import pygame
import math
import random


class MouseTail:
    def __init__(self, max_length=30):
        """Initialize the mouse tail."""
        self.max_length = max_length
        self.positions = []  # List of (x, y) positions
        self.colors = []     # List of colors for each segment
        self.alpha_values = []  # List of alpha values for fading effect
        self.base_color = (255, 255, 255)  # White base color
        
        # Fiery shooting star colors - warm to cool gradient
        self.glow_colors = [
            (255, 255, 255),  # Bright white center
            (255, 255, 200),  # Warm white
            (255, 255, 150),  # Light yellow
            (255, 255, 100),  # Yellow
            (255, 200, 100),  # Orange-yellow
            (255, 150, 100),  # Orange
            (255, 100, 100),  # Red-orange
            (255, 50, 50),    # Red
            (200, 50, 50),    # Dark red
            (150, 50, 50),    # Darker red
        ]
        
        self.current_glow_index = 0
        self.glow_change_timer = 0
        self.glow_change_interval = 300  # Change glow color every 300ms
        self.smoothing_factor = 0.3  # For smooth interpolation
        self.last_pos = None
        
    def update(self, mouse_pos, dt):
        """Update the tail with new mouse position."""
        x, y = mouse_pos
        
        # Smooth interpolation for less jagged movement
        if self.last_pos is not None:
            smooth_x = x * (1 - self.smoothing_factor) + self.last_pos[0] * self.smoothing_factor
            smooth_y = y * (1 - self.smoothing_factor) + self.last_pos[1] * self.smoothing_factor
            x, y = smooth_x, smooth_y
        
        self.last_pos = (x, y)
        
        # Add new position to the front
        self.positions.insert(0, (x, y))
        
        # Add new color and alpha
        self.colors.insert(0, self.glow_colors[self.current_glow_index])
        self.alpha_values.insert(0, 255)
        
        # Limit the length
        if len(self.positions) > self.max_length:
            self.positions.pop()
            self.colors.pop()
            self.alpha_values.pop()
        
        # Update alpha values for fading effect
        for i in range(len(self.alpha_values)):
            fade_factor = i / len(self.alpha_values) if self.alpha_values else 0
            self.alpha_values[i] = int(255 * (1 - fade_factor * 0.7))  # Less fade for more vibrant tail
        
        # Update glow color change timer
        self.glow_change_timer += dt
        if self.glow_change_timer >= self.glow_change_interval:
            self.current_glow_index = (self.current_glow_index + 1) % len(self.glow_colors)
            self.glow_change_timer = 0
    
    def draw(self, screen):
        """Draw the glowing tail."""
        if len(self.positions) < 2:
            return
        
        # Create a surface for the tail
        tail_surface = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
        
        # Draw tail segments with smooth curves
        for i in range(len(self.positions) - 1):
            if i + 1 >= len(self.positions):
                continue
                
            start_pos = self.positions[i]
            end_pos = self.positions[i + 1]
            
            # Calculate segment properties - bigger and more vibrant
            segment_width = max(8, int(20 * (1 - i / len(self.positions))))
            color = self.colors[i]
            alpha = self.alpha_values[i]
            
            # Create multiple layers for a more fiery effect
            for layer in range(3):
                layer_width = segment_width - layer * 3
                if layer_width <= 0:
                    continue
                    
                layer_alpha = int(alpha * (1 - layer * 0.3))
                layer_color = (*color, layer_alpha)
                
                # Draw smooth curve instead of straight line
                if i > 0 and i < len(self.positions) - 2:
                    # Use quadratic curve for smoother appearance
                    prev_pos = self.positions[i - 1]
                    next_pos = self.positions[i + 1]
                    
                    # Calculate control points for smooth curve
                    cp1_x = start_pos[0] + (end_pos[0] - prev_pos[0]) * 0.25
                    cp1_y = start_pos[1] + (end_pos[1] - prev_pos[1]) * 0.25
                    cp2_x = end_pos[0] + (start_pos[0] - next_pos[0]) * 0.25
                    cp2_y = end_pos[1] + (start_pos[1] - next_pos[1]) * 0.25
                    
                    # Draw curved segment
                    self.draw_curved_line(tail_surface, start_pos, (cp1_x, cp1_y), 
                                        (cp2_x, cp2_y), end_pos, layer_color, layer_width)
                else:
                    # Draw straight line for end segments
                    pygame.draw.line(tail_surface, layer_color, start_pos, end_pos, layer_width)
        
        # Draw the tail surface onto the screen
        screen.blit(tail_surface, (0, 0))
        
        # Draw a bright center point at the mouse position
        if self.positions:
            center_pos = self.positions[0]
            # Draw multiple glow layers for shooting star effect
            for i in range(4):
                glow_size = 15 - i * 3
                glow_alpha = 150 - i * 30
                pygame.draw.circle(screen, (255, 255, 255, glow_alpha), center_pos, glow_size)
            # Draw inner bright point
            pygame.draw.circle(screen, (255, 255, 255, 255), center_pos, 5)
    
    def clear(self):
        """Clear the tail."""
        self.positions.clear()
        self.colors.clear()
        self.alpha_values.clear()
    
    def set_max_length(self, length):
        """Set the maximum length of the tail."""
        self.max_length = max(5, min(50, length))  # Clamp between 5 and 50
    
    def draw_curved_line(self, surface, start, cp1, cp2, end, color, width):
        """Draw a curved line using control points."""
        # Simple approximation using multiple line segments
        steps = 10
        points = []
        
        for i in range(steps + 1):
            t = i / steps
            # Cubic Bezier curve
            x = (1-t)**3 * start[0] + 3*(1-t)**2*t * cp1[0] + 3*(1-t)*t**2 * cp2[0] + t**3 * end[0]
            y = (1-t)**3 * start[1] + 3*(1-t)**2*t * cp1[1] + 3*(1-t)*t**2 * cp2[1] + t**3 * end[1]
            points.append((int(x), int(y)))
        
        # Draw line segments
        for i in range(len(points) - 1):
            pygame.draw.line(surface, color, points[i], points[i+1], width)
    
    def add_sparkle_effect(self, pos):
        """Add a sparkle effect at the given position."""
        # This could be expanded to add particle effects
        pass 
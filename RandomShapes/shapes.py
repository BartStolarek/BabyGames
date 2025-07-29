"""
Shapes module for Baby Games
Defines different shape types and their properties.
"""

import pygame
import random
import math


class Shape:
    def __init__(self, shape_type, color_name, x, y, size=50):
        """Initialize a shape with type, color, position, and size."""
        self.shape_type = shape_type
        self.color_name = color_name
        self.x = x
        self.y = y
        self.size = size
        self.angle = 0
        self.scale = 1.0
        self.alpha = 255
        self.visible = True
        self.creation_time = pygame.time.get_ticks()
        
        # Animation properties
        self.velocity_x = random.uniform(-3, 3)
        self.velocity_y = random.uniform(-3, 3)
        self.rotation_speed = random.uniform(-5, 5)
        self.scale_speed = random.uniform(0.95, 1.05)
        
        # Get the actual color
        self.color = self.get_color_from_name(color_name)
    
    def get_color_from_name(self, color_name):
        """Convert color name to RGB tuple."""
        color_map = {
            # Basic colors
            "red": (255, 0, 0),
            "blue": (0, 0, 255),
            "green": (0, 255, 0),
            "yellow": (255, 255, 0),
            "purple": (128, 0, 128),
            "orange": (255, 165, 0),
            "pink": (255, 192, 203),
            "cyan": (0, 255, 255),
            
            # Number colors
            "gold": (255, 215, 0),
            "silver": (192, 192, 192),
            "bronze": (205, 127, 50),
            "emerald": (0, 128, 0),
            "ruby": (155, 17, 30),
            "sapphire": (15, 82, 186),
            "amethyst": (153, 102, 204),
            "topaz": (255, 200, 124),
            
            # Special colors
            "rainbow": self.get_rainbow_color(),
            "neon": (0, 255, 255),
            "pastel": (255, 182, 193),
            "metallic": (169, 169, 169),
            "glow": (255, 255, 224),
            "sparkle": (255, 255, 255),
            "shimmer": (240, 248, 255),
            "crystal": (176, 196, 222),
            
            # Arrow colors
            "electric": (0, 255, 255),
            "fire": (255, 69, 0),
            "ice": (173, 216, 230),
            "earth": (139, 69, 19),
            "wind": (240, 248, 255),
            "light": (255, 255, 224),
            "dark": (47, 79, 79),
            "cosmic": (138, 43, 226),
        }
        
        return color_map.get(color_name, (255, 255, 255))
    
    def get_rainbow_color(self):
        """Get a random rainbow color."""
        rainbow_colors = [
            (255, 0, 0),    # Red
            (255, 127, 0),  # Orange
            (255, 255, 0),  # Yellow
            (0, 255, 0),    # Green
            (0, 0, 255),    # Blue
            (75, 0, 130),   # Indigo
            (148, 0, 211),  # Violet
        ]
        return random.choice(rainbow_colors)
    
    def update(self):
        """Update shape position and properties."""
        self.x += self.velocity_x
        self.y += self.velocity_y
        self.angle += self.rotation_speed
        self.scale *= self.scale_speed
        
        # Keep scale reasonable
        self.scale = max(0.1, min(3.0, self.scale))
    
    def draw(self, screen):
        """Draw the shape on the screen."""
        if not self.visible:
            return
        
        # Create a surface for the shape
        surface = pygame.Surface((self.size * 2, self.size * 2), pygame.SRCALPHA)
        
        # Apply transformations
        scaled_size = int(self.size * self.scale)
        center_x, center_y = self.size, self.size
        
        # Draw based on shape type
        if self.shape_type == "circle":
            pygame.draw.circle(surface, self.color, (center_x, center_y), scaled_size)
        elif self.shape_type == "square":
            rect = pygame.Rect(center_x - scaled_size, center_y - scaled_size, 
                             scaled_size * 2, scaled_size * 2)
            pygame.draw.rect(surface, self.color, rect)
        elif self.shape_type == "triangle":
            points = [
                (center_x, center_y - scaled_size),
                (center_x - scaled_size, center_y + scaled_size),
                (center_x + scaled_size, center_y + scaled_size)
            ]
            pygame.draw.polygon(surface, self.color, points)
        elif self.shape_type == "star":
            self.draw_star(surface, center_x, center_y, scaled_size)
        elif self.shape_type == "heart":
            self.draw_heart(surface, center_x, center_y, scaled_size)
        elif self.shape_type == "diamond":
            points = [
                (center_x, center_y - scaled_size),
                (center_x + scaled_size, center_y),
                (center_x, center_y + scaled_size),
                (center_x - scaled_size, center_y)
            ]
            pygame.draw.polygon(surface, self.color, points)
        elif self.shape_type == "oval":
            pygame.draw.ellipse(surface, self.color, 
                              (center_x - scaled_size, center_y - scaled_size//2,
                               scaled_size * 2, scaled_size))
        elif self.shape_type == "cross":
            self.draw_cross(surface, center_x, center_y, scaled_size)
        elif self.shape_type == "spiral":
            self.draw_spiral(surface, center_x, center_y, scaled_size)
        elif self.shape_type == "wave":
            self.draw_wave(surface, center_x, center_y, scaled_size)
        elif self.shape_type == "zigzag":
            self.draw_zigzag(surface, center_x, center_y, scaled_size)
        elif self.shape_type == "dots":
            self.draw_dots(surface, center_x, center_y, scaled_size)
        elif self.shape_type == "lines":
            self.draw_lines(surface, center_x, center_y, scaled_size)
        elif self.shape_type == "fireworks":
            self.draw_fireworks(surface, center_x, center_y, scaled_size)
        elif self.shape_type == "sparkle":
            self.draw_sparkle(surface, center_x, center_y, scaled_size)
        elif self.shape_type == "bubble":
            self.draw_bubble(surface, center_x, center_y, scaled_size)
        elif self.shape_type == "flower":
            self.draw_flower(surface, center_x, center_y, scaled_size)
        elif self.shape_type == "butterfly":
            self.draw_butterfly(surface, center_x, center_y, scaled_size)
        elif self.shape_type == "rocket":
            self.draw_rocket(surface, center_x, center_y, scaled_size)
        elif self.shape_type == "rainbow":
            self.draw_rainbow(surface, center_x, center_y, scaled_size)
        elif self.shape_type == "sun":
            self.draw_sun(surface, center_x, center_y, scaled_size)
        elif self.shape_type == "moon":
            self.draw_moon(surface, center_x, center_y, scaled_size)
        elif self.shape_type == "cloud":
            self.draw_cloud(surface, center_x, center_y, scaled_size)
        elif self.shape_type == "explosion":
            self.draw_explosion(surface, center_x, center_y, scaled_size)
        elif self.shape_type == "burst":
            self.draw_burst(surface, center_x, center_y, scaled_size)
        elif self.shape_type == "fade":
            self.draw_fade(surface, center_x, center_y, scaled_size)
        elif self.shape_type == "shimmer":
            self.draw_shimmer(surface, center_x, center_y, scaled_size)
        else:
            # Default to circle
            pygame.draw.circle(surface, self.color, (center_x, center_y), scaled_size)
        
        # Rotate the surface
        rotated_surface = pygame.transform.rotate(surface, self.angle)
        
        # Get the rect for positioning
        rect = rotated_surface.get_rect(center=(self.x, self.y))
        
        # Draw to screen
        screen.blit(rotated_surface, rect)
    
    def draw_star(self, surface, x, y, size):
        """Draw a star shape."""
        points = []
        for i in range(10):
            angle = i * math.pi / 5
            radius = size if i % 2 == 0 else size // 2
            points.append((x + radius * math.cos(angle), y + radius * math.sin(angle)))
        pygame.draw.polygon(surface, self.color, points)
    
    def draw_heart(self, surface, x, y, size):
        """Draw a heart shape."""
        points = []
        for t in range(0, 360, 5):
            angle = math.radians(t)
            px = 16 * math.sin(angle) ** 3
            py = -(13 * math.cos(angle) - 5 * math.cos(2*angle) - 2 * math.cos(3*angle) - math.cos(4*angle))
            points.append((x + px * size // 16, y + py * size // 16))
        if len(points) > 2:
            pygame.draw.polygon(surface, self.color, points)
    
    def draw_cross(self, surface, x, y, size):
        """Draw a cross shape."""
        pygame.draw.line(surface, self.color, (x - size, y), (x + size, y), size // 4)
        pygame.draw.line(surface, self.color, (x, y - size), (x, y + size), size // 4)
    
    def draw_spiral(self, surface, x, y, size):
        """Draw a spiral shape."""
        points = []
        for i in range(0, 720, 10):
            angle = math.radians(i)
            radius = i / 720 * size
            points.append((x + radius * math.cos(angle), y + radius * math.sin(angle)))
        if len(points) > 1:
            pygame.draw.lines(surface, self.color, False, points, 3)
    
    def draw_wave(self, surface, x, y, size):
        """Draw a wave pattern."""
        points = []
        for i in range(-size, size, 5):
            wave_y = y + math.sin(i * 0.1) * size // 3
            points.append((x + i, wave_y))
        if len(points) > 1:
            pygame.draw.lines(surface, self.color, False, points, 3)
    
    def draw_zigzag(self, surface, x, y, size):
        """Draw a zigzag pattern."""
        points = []
        for i in range(-size, size, size // 4):
            zig_y = y + (size // 4) if (i // (size // 4)) % 2 == 0 else y - (size // 4)
            points.append((x + i, zig_y))
        if len(points) > 1:
            pygame.draw.lines(surface, self.color, False, points, 3)
    
    def draw_dots(self, surface, x, y, size):
        """Draw multiple dots."""
        for i in range(5):
            dot_x = x + random.randint(-size, size)
            dot_y = y + random.randint(-size, size)
            pygame.draw.circle(surface, self.color, (dot_x, dot_y), size // 5)
    
    def draw_lines(self, surface, x, y, size):
        """Draw multiple lines."""
        for i in range(3):
            start_x = x + random.randint(-size, size)
            start_y = y + random.randint(-size, size)
            end_x = x + random.randint(-size, size)
            end_y = y + random.randint(-size, size)
            pygame.draw.line(surface, self.color, (start_x, start_y), (end_x, end_y), 3)
    
    def draw_fireworks(self, surface, x, y, size):
        """Draw fireworks effect."""
        for i in range(8):
            angle = i * math.pi / 4
            end_x = x + size * math.cos(angle)
            end_y = y + size * math.sin(angle)
            pygame.draw.line(surface, self.color, (x, y), (end_x, end_y), 3)
    
    def draw_sparkle(self, surface, x, y, size):
        """Draw a sparkle effect."""
        for i in range(4):
            angle = i * math.pi / 2
            end_x = x + size * math.cos(angle)
            end_y = y + size * math.sin(angle)
            pygame.draw.line(surface, self.color, (x, y), (end_x, end_y), 2)
    
    def draw_bubble(self, surface, x, y, size):
        """Draw a bubble with highlight."""
        pygame.draw.circle(surface, self.color, (x, y), size)
        pygame.draw.circle(surface, (255, 255, 255), (x - size//3, y - size//3), size//4)
    
    def draw_flower(self, surface, x, y, size):
        """Draw a flower with petals."""
        for i in range(6):
            angle = i * math.pi / 3
            petal_x = x + size//2 * math.cos(angle)
            petal_y = y + size//2 * math.sin(angle)
            pygame.draw.circle(surface, self.color, (int(petal_x), int(petal_y)), size//3)
        pygame.draw.circle(surface, (255, 255, 0), (x, y), size//4)
    
    def draw_butterfly(self, surface, x, y, size):
        """Draw a butterfly shape."""
        # Left wing
        points_left = [(x, y), (x - size, y - size//2), (x - size//2, y - size)]
        pygame.draw.polygon(surface, self.color, points_left)
        # Right wing
        points_right = [(x, y), (x + size, y - size//2), (x + size//2, y - size)]
        pygame.draw.polygon(surface, self.color, points_right)
    
    def draw_rocket(self, surface, x, y, size):
        """Draw a rocket shape."""
        points = [(x, y - size), (x - size//2, y + size//2), (x + size//2, y + size//2)]
        pygame.draw.polygon(surface, self.color, points)
        pygame.draw.rect(surface, (255, 255, 255), (x - size//4, y, size//2, size//2))
    
    def draw_rainbow(self, surface, x, y, size):
        """Draw a rainbow arc."""
        colors = [(255, 0, 0), (255, 127, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (75, 0, 130), (148, 0, 211)]
        for i, color in enumerate(colors):
            radius = size - i * size//7
            if radius > 0:
                pygame.draw.arc(surface, color, (x - radius, y - radius, radius * 2, radius * 2), 0, math.pi, 5)
    
    def draw_sun(self, surface, x, y, size):
        """Draw a sun with rays."""
        pygame.draw.circle(surface, (255, 255, 0), (x, y), size)
        for i in range(8):
            angle = i * math.pi / 4
            ray_x = x + (size + size//2) * math.cos(angle)
            ray_y = y + (size + size//2) * math.sin(angle)
            pygame.draw.line(surface, (255, 255, 0), (x, y), (ray_x, ray_y), 3)
    
    def draw_moon(self, surface, x, y, size):
        """Draw a crescent moon."""
        pygame.draw.circle(surface, (255, 255, 255), (x, y), size)
        pygame.draw.circle(surface, (0, 0, 0), (x + size//3, y), size)
    
    def draw_cloud(self, surface, x, y, size):
        """Draw a cloud shape."""
        pygame.draw.circle(surface, (255, 255, 255), (x - size//2, y), size//2)
        pygame.draw.circle(surface, (255, 255, 255), (x + size//2, y), size//2)
        pygame.draw.circle(surface, (255, 255, 255), (x, y - size//3), size//2)
    
    def draw_explosion(self, surface, x, y, size):
        """Draw an explosion effect."""
        for i in range(12):
            angle = i * math.pi / 6
            end_x = x + size * math.cos(angle)
            end_y = y + size * math.sin(angle)
            pygame.draw.line(surface, self.color, (x, y), (end_x, end_y), 4)
    
    def draw_burst(self, surface, x, y, size):
        """Draw a burst pattern."""
        for i in range(6):
            angle = i * math.pi / 3
            end_x = x + size * math.cos(angle)
            end_y = y + size * math.sin(angle)
            pygame.draw.line(surface, self.color, (x, y), (end_x, end_y), 5)
    
    def draw_fade(self, surface, x, y, size):
        """Draw a fade effect."""
        for i in range(5):
            alpha = 255 - i * 50
            if alpha > 0:
                color_with_alpha = (*self.color, alpha)
                fade_surface = pygame.Surface((size * 2, size * 2), pygame.SRCALPHA)
                pygame.draw.circle(fade_surface, color_with_alpha, (size, size), size - i * size//5)
                surface.blit(fade_surface, (0, 0))
    
    def draw_shimmer(self, surface, x, y, size):
        """Draw a shimmer effect."""
        for i in range(4):
            angle = i * math.pi / 2 + pygame.time.get_ticks() * 0.01
            shimmer_x = x + size//2 * math.cos(angle)
            shimmer_y = y + size//2 * math.sin(angle)
            pygame.draw.circle(surface, (255, 255, 255), (int(shimmer_x), int(shimmer_y)), size//6)
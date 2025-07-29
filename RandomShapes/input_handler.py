"""
Input Handler module for Baby Games
Manages keyboard input processing and key mapping.
"""

import pygame


class InputHandler:
    def __init__(self):
        """Initialize the input handler."""
        self.key_mappings = {
            # Letter keys
            pygame.K_a: "circle",
            pygame.K_b: "square", 
            pygame.K_c: "triangle",
            pygame.K_d: "star",
            pygame.K_e: "heart",
            pygame.K_f: "diamond",
            pygame.K_g: "oval",
            pygame.K_h: "cross",
            pygame.K_i: "spiral",
            pygame.K_j: "wave",
            pygame.K_k: "zigzag",
            pygame.K_l: "dots",
            pygame.K_m: "lines",
            pygame.K_n: "squares",
            pygame.K_o: "circles",
            pygame.K_p: "triangles",
            pygame.K_q: "stars",
            pygame.K_r: "hearts",
            pygame.K_s: "diamonds",
            pygame.K_t: "ovals",
            pygame.K_u: "crosses",
            pygame.K_v: "spirals",
            pygame.K_w: "waves",
            pygame.K_x: "zigzags",
            pygame.K_y: "dots",
            pygame.K_z: "lines",
            
            # Number keys
            pygame.K_0: "fireworks",
            pygame.K_1: "sparkle",
            pygame.K_2: "bubble",
            pygame.K_3: "flower",
            pygame.K_4: "butterfly",
            pygame.K_5: "rocket",
            pygame.K_6: "rainbow",
            pygame.K_7: "sun",
            pygame.K_8: "moon",
            pygame.K_9: "cloud",
            
            # Special keys
            pygame.K_SPACE: "explosion",
            pygame.K_RETURN: "burst",
            pygame.K_TAB: "spiral",
            pygame.K_BACKSPACE: "fade",
            pygame.K_ESCAPE: "shimmer",
            
            # Arrow keys
            pygame.K_UP: "upward",
            pygame.K_DOWN: "downward",
            pygame.K_LEFT: "leftward",
            pygame.K_RIGHT: "rightward",
        }
        
        # Color mappings for different key types
        self.color_mappings = {
            "letters": ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan"],
            "numbers": ["gold", "silver", "bronze", "emerald", "ruby", "sapphire", "amethyst", "topaz"],
            "special": ["rainbow", "neon", "pastel", "metallic", "glow", "sparkle", "shimmer", "crystal"],
            "arrows": ["electric", "fire", "ice", "earth", "wind", "light", "dark", "cosmic"]
        }
    
    def get_shape_type(self, key):
        """Get the shape type for a given key."""
        return self.key_mappings.get(key, "circle")
    
    def get_color_category(self, key):
        """Get the color category for a given key."""
        if key in range(pygame.K_a, pygame.K_z + 1):
            return "letters"
        elif key in range(pygame.K_0, pygame.K_9 + 1):
            return "numbers"
        elif key in [pygame.K_SPACE, pygame.K_RETURN, pygame.K_TAB, pygame.K_BACKSPACE, pygame.K_ESCAPE]:
            return "special"
        elif key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
            return "arrows"
        else:
            return "letters"  # Default
    
    def get_available_colors(self, key):
        """Get available colors for a given key."""
        category = self.get_color_category(key)
        return self.color_mappings.get(category, self.color_mappings["letters"])
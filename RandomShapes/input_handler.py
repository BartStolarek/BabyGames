"""
Input Handler module for Baby Games
Manages keyboard and mouse input processing and key mapping.
"""

import pygame


class InputHandler:
    def __init__(self):
        """Initialize the input handler."""
        # Mouse button mappings for creative actions
        self.mouse_button_actions = {
            1: "rainbow_trail",      # Left click - Creates rainbow trail effect
            2: "middle_click",       # Middle click - Creates expanding circles
            3: "right_click",        # Right click - Creates star burst
            4: "side_button_1",      # Side button 1 - Creates spiral effect
            5: "side_button_2",      # Side button 2 - Creates fireworks
            6: "side_button_3",      # Side button 3 - Creates butterfly swarm
            7: "side_button_4",      # Side button 4 - Creates cosmic portal
        }
        
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
    
    def get_mouse_action(self, button):
        """Get the action for a mouse button."""
        return self.mouse_button_actions.get(button, "unknown")
    
    def get_mouse_action_description(self, button):
        """Get a description of what a mouse button does."""
        action = self.get_mouse_action(button)
        descriptions = {
            "rainbow_trail": "Creates a beautiful rainbow trail effect",
            "middle_click": "Creates expanding circles from mouse position",
            "right_click": "Creates a star burst explosion",
            "side_button_1": "Creates a spiral effect around the mouse",
            "side_button_2": "Creates fireworks at mouse position",
            "side_button_3": "Creates a beautiful butterfly swarm",
            "side_button_4": "Creates a cosmic portal effect",
            "unknown": "Unknown action"
        }
        return descriptions.get(action, "Unknown action")
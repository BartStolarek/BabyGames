#!/usr/bin/env python3
"""
Test script for shape limit and popping animation
"""

import pygame
import sys
from shape_manager import ShapeManager
from display import Display

def test_shape_limit():
    """Test the shape limit functionality."""
    pygame.init()
    
    # Create display and shape manager
    display = Display()
    shape_manager = ShapeManager()
    
    # Set screen bounds
    width, height = display.get_screen_bounds()
    shape_manager.set_screen_bounds(width, height)
    
    print("🧪 Testing shape limit functionality...")
    print(f"📺 Screen size: {width}x{height}")
    print(f"🎯 Shape limit: {shape_manager.max_shapes}")
    print("⌨️  Press keys to create shapes (up to 10)")
    print("💥 Watch for popping animations when limit is reached!")
    print("🚪 Press Ctrl+Shift+C to exit")
    
    clock = pygame.time.Clock()
    running = True
    
    try:
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    # Check for exit combination
                    if (event.key == pygame.K_c and 
                        pygame.key.get_mods() & pygame.KMOD_CTRL and 
                        pygame.key.get_mods() & pygame.KMOD_SHIFT):
                        running = False
                    else:
                        # Create a shape
                        shape_manager.create_shape_from_key(event.key)
            
            # Update and draw
            shape_manager.update()
            display.clear()
            shape_manager.draw(display.screen)
            display.update()
            
            # Show current counts
            shape_count = shape_manager.get_shape_count()
            particle_count = shape_manager.get_particle_count()
            if particle_count > 0:
                print(f"🎨 Shapes: {shape_count}, ✨ Particles: {particle_count}")
            
            clock.tick(60)
            
    finally:
        shape_manager.cleanup()
        pygame.quit()
    
    print("✅ Test completed!")

if __name__ == "__main__":
    test_shape_limit()
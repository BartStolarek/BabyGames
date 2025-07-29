"""
Sound Manager module for Baby Games
Handles baby-friendly sounds for shape generation and interactions.
"""

import random
import pygame
import math


class SoundManager:
    def __init__(self):
        """Initialize the sound manager with baby-friendly sounds."""
        self.sounds = {}
        self.sound_enabled = True
        self.volume = 0.9  # Increased volume for better audibility
        
        # Initialize pygame mixer
        try:
            pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
        except pygame.error:
            print("⚠️  Could not initialize audio system. Sounds will be disabled.")
            self.sound_enabled = False
            return
        
        # Create simple baby-friendly sounds
        self._create_baby_sounds()
    
    def _create_baby_sounds(self):
        """Create simple, pleasant sounds suitable for babies."""
        if not self.sound_enabled:
            return
            
        # Generate different types of baby-friendly sounds
        sample_rate = 22050
        duration = 1.0  # Longer duration for piano-like notes
        
        # 1. Gentle bell-like sound
        bell_sound = self._generate_bell_sound(sample_rate, duration)
        self.sounds['bell'] = bell_sound
        
        # 2. Soft chime sound
        chime_sound = self._generate_chime_sound(sample_rate, duration)
        self.sounds['chime'] = chime_sound
        
        # 3. Gentle tinkle sound
        tinkle_sound = self._generate_tinkle_sound(sample_rate, duration)
        self.sounds['tinkle'] = tinkle_sound
        
        # 4. Soft pop sound
        pop_sound = self._generate_pop_sound(sample_rate, duration)
        self.sounds['pop'] = pop_sound
        
        # 5. Gentle sparkle sound
        sparkle_sound = self._generate_sparkle_sound(sample_rate, duration)
        self.sounds['sparkle'] = sparkle_sound
    
    def _generate_bell_sound(self, sample_rate, duration):
        """Generate a gentle bell-like sound."""
        samples = int(sample_rate * duration)
        sound_data = []
        
        for i in range(samples):
            # Create a gentle bell-like tone with harmonics
            t = i / sample_rate
            freq = 523  # C5 note
            amplitude = 0.6 * math.exp(-t / 0.8)  # Slower decay for piano-like sustain
            
            # Add harmonics for a richer sound
            wave = (amplitude * 
                   (0.6 * math.sin(2 * math.pi * freq * t) +
                    0.3 * math.sin(2 * math.pi * freq * 2 * t) +
                    0.1 * math.sin(2 * math.pi * freq * 3 * t)))
            
            # Convert to 16-bit integer
            sample = int(wave * 32767)
            sound_data.extend([sample, sample])  # Stereo
        
        # Create a simple sound using pygame's built-in capabilities
        return self._create_sound_from_data(sound_data)
    
    def _generate_chime_sound(self, sample_rate, duration):
        """Generate a soft chime sound."""
        samples = int(sample_rate * duration)
        sound_data = []
        
        for i in range(samples):
            t = i / sample_rate
            freq = 659  # E5 note
            amplitude = 0.5 * math.exp(-t / 1.0)  # Even slower decay
            
            wave = amplitude * math.sin(2 * math.pi * freq * t)
            sample = int(wave * 32767)
            sound_data.extend([sample, sample])
        
        return self._create_sound_from_data(sound_data)
    
    def _generate_tinkle_sound(self, sample_rate, duration):
        """Generate a gentle tinkle sound."""
        samples = int(sample_rate * duration)
        sound_data = []
        
        for i in range(samples):
            t = i / sample_rate
            freq = 784  # G5 note
            amplitude = 0.4 * math.exp(-t / 0.6)  # Medium decay
            
            wave = amplitude * math.sin(2 * math.pi * freq * t)
            sample = int(wave * 32767)
            sound_data.extend([sample, sample])
        
        return self._create_sound_from_data(sound_data)
    
    def _generate_pop_sound(self, sample_rate, duration):
        """Generate a soft pop sound."""
        samples = int(sample_rate * duration)
        sound_data = []
        
        for i in range(samples):
            t = i / sample_rate
            freq = 440  # A4 note
            amplitude = 0.7 * math.exp(-t / 0.4)  # Quick attack, medium decay
            
            wave = amplitude * math.sin(2 * math.pi * freq * t)
            sample = int(wave * 32767)
            sound_data.extend([sample, sample])
        
        return self._create_sound_from_data(sound_data)
    
    def _generate_sparkle_sound(self, sample_rate, duration):
        """Generate a gentle sparkle sound."""
        samples = int(sample_rate * duration)
        sound_data = []
        
        for i in range(samples):
            t = i / sample_rate
            freq = 587  # D5 note
            amplitude = 0.5 * math.exp(-t / 0.7)  # Balanced decay
            
            # Add some randomness for sparkle effect
            wave = amplitude * math.sin(2 * math.pi * freq * t + random.uniform(0, 0.05))
            sample = int(wave * 32767)
            sound_data.extend([sample, sample])
        
        return self._create_sound_from_data(sound_data)
    
    def _create_sound_from_data(self, sound_data):
        """Create a pygame sound from raw audio data."""
        try:
            # Try to use numpy if available for better performance
            import numpy as np
            sound_array = np.array(sound_data, dtype=np.int16)
            stereo_array = sound_array.reshape(-1, 2)
            return pygame.sndarray.make_sound(stereo_array)
        except ImportError:
            # Fallback to simple approach without numpy
            # Create a simple beep sound as fallback
            return self._create_simple_beep()
    
    def _create_simple_beep(self):
        """Create a simple beep sound as fallback."""
        try:
            # Create a simple sine wave sound
            sample_rate = 22050
            duration = 0.2
            samples = int(sample_rate * duration)
            sound_data = []
            
            for i in range(samples):
                t = i / sample_rate
                freq = 800
                amplitude = 0.2 * (1 - t / duration)
                wave = amplitude * math.sin(2 * math.pi * freq * t)
                sample = int(wave * 32767)
                sound_data.extend([sample, sample])
            
            # Convert to pygame sound
            sound_array = pygame.surfarray.pixels3d(
                pygame.Surface((len(sound_data) // 2, 1, 3)))[:, 0, 0].astype(pygame.int16)
            return pygame.sndarray.make_sound(sound_array)
        except:
            # If all else fails, return None (sound will be disabled)
            return None
    
    def play_shape_sound(self):
        """Play a random baby-friendly sound when a shape is created."""
        if not self.sound_enabled or not self.sounds:
            return
        
        # Choose a random sound
        sound_name = random.choice(list(self.sounds.keys()))
        sound = self.sounds[sound_name]
        
        if sound is not None:
            # Set volume and play
            sound.set_volume(self.volume)
            sound.play()
    
    def set_volume(self, volume):
        """Set the volume level (0.0 to 1.0)."""
        self.volume = max(0.0, min(1.0, volume))
    
    def toggle_sound(self):
        """Toggle sound on/off."""
        self.sound_enabled = not self.sound_enabled
        return self.sound_enabled
    
    def cleanup(self):
        """Clean up sound resources."""
        if self.sound_enabled:
            pygame.mixer.quit()
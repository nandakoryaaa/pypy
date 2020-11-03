import pygame

class Audio:
	def __init__(self):
		pygame.mixer.pre_init(44100, -16, 2, 2048)
		pygame.mixer.init()
		pygame.mixer.set_num_channels(2)
		self.channel_music = pygame.mixer.Channel(0)
		self.channel_sfx = pygame.mixer.Channel(1)
		self.audio_map = {}

	def load_audio(self, name, filename):
		sound = pygame.mixer.Sound(filename)
		self.audio_map[name] = sound

	def play_music(self, name):
		if name in self.audio_map:
			music = self.audio_map[name]
			self.channel_music.play(music, -1)

	def play_sfx(self, name):
		if name in self.audio_map:
			sfx = self.audio_map[name]
			self.channel_sfx.play(sfx)


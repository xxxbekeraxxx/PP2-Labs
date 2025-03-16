import pygame

pygame.init()

width, height = 500, 300
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

# songs
songs = ["People.mp3", "Price.mp3", "Cheap_Thrills.mp3"]
index = 0

pygame.mixer.music.load(songs[index])
pygame.mixer.music.play()

pygame.mixer.music.set_endevent(pygame.USEREVENT)

paused = False

def next_song():
    global index
    index = (index + 1) % len(songs)
    pygame.mixer.music.load(songs[index])
    pygame.mixer.music.play()

def prev_song():
    global index
    index = (index - 1) % len(songs)
    pygame.mixer.music.load(songs[index])
    pygame.mixer.music.play()


# text
font = pygame.font.SysFont("comicsansms", 72)

text = font.render("Songs", True, (200, 50, 120))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause() 
                paused = not paused

            if event.key == pygame.K_LEFT:
                next_song()

            if event.key == pygame.K_RIGHT:
                    prev_song()
        
        if event.type == pygame.USEREVENT:  # Song finished -> Play next song
            next_song()
    
    
    screen.fill("lightgreen")
    screen.blit(text, ((width - text.get_width()) // 2, (height  - text.get_height()) // 2))
    pygame.display.flip()
    clock.tick(60)
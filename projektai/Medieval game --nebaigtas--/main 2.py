import pygame,pygame.locals,sprite_module,random,os


pygame.init()
screen = pygame.display.set_mode((780, 640))
pygame.display.set_caption('Tanks and chickens')


def main():
    background = pygame.image.load('Graphics/grass.png')    
    background = background.convert()
    screen.blit(background, (0, 0))
    
    player = sprite_module.Player(screen)
    #waves
    wave = [2, 4, 6, 8, 10, 12,0]
    #s_images
    s_img[]
    for file in os.listdir('Sprites/'):
        s_img.append(pygame.image.load('./Sprites/'+file))
    #soldiers
    s_info=[[3,5,10,100,2],[3,5,20,100,4],[3,5,20,100,6],[3,5,20,100,8]\
                  ,[3,5,20,100,10],[3,5,20,100,12],[15,20,100,100,40]]
    
    soldiers=[]
    #wave gen
    for i in range(10):
        while True:
            a = random.randinit(0,5)
            if wave[a]:
                soldiers.append(sprite_module.Zombie\
                                (screen,s_info[a][0],s_info[a][1],\
                                 s_info[a][2],s_info[a][3],s_info[a][4],s_info[a],a,player.rect.center))
                wave[a]=wave[a]-1
                break

    #Ammo
    ammo = [[20,30],[100,200]]
    ammo_capacity = [20]
    temp_string = ''

    for index in range(len(ammo)):
        #temp string "current ammo,ammo packs"
        temp_string+=str(ammo[index][0])+','+str(ammo[index][1])+','

    ammo_text=sprite_module.Text\
             (20,(0,0,255),(800,80),temp_string.strip(','),\
              '%s/%s          %s/%s',255)

    #Player
    player_status = [[500,500],[300,300],3]
    #Text
    health = sprite_module.StatusBar((0,20),(255,0,0),(0,0,0),(250,30),200,350,0,None)
    armour = sprite_module.StatusBar((0,52),(238,233,233),(139,137,137),(250,30),100,200,0,None)
    
    
    health_text = sprite_module.Text(25,(255,255,255),(125,35),'350,350','%s/%s',255)
    armour_text = sprite_module.Text(25,(0,0,0),(125,70),'200,200','%s/%s',255)
    wave_text = sprite_module.Text\
             (30,(255,255,255),(430,60),'0,1,'+str(sum(wave)),'Score:%s Wave:%s Soldiers Left:%s',255)    
    
    soldierGroup = pygame.sprite.Group(soldiers)
    bullet_img = pygame.sprite.Group()
    bullet_hitbox = pygame.sprite.Group()
    reloading = pygame.sprite.Group()

    allSprites = pygame.sprite.OrderedUpdates\
    (bullet_img,bullet_hitbox,player,soldierGroup,reloading,health,armour,health_text,armour_text,wave_text,ammo_text)

    #Action
    clock =pygame.time.Clock()
    keepGoing = True

    boss_spawn = False

    bullet_images=[]
    for file in os.listdir('bullets/'):
            bullet_images.append(pygame.image.load('./bullets/'+file))
    wave_num = 1
    wave = [2, 4, 6, 8, 10, 12,0]

    active_soldier = 10

    score = 0

    weapon = [True,True]
    current_weapon = 0

    reload_time = [1.5,8.5]
    reload_status = False
    
    while keepGoing:
        clock.tick(60)
        keystate = pygame.key.get_pressed()
        if keystate[pygame.locals.K_w]:
            player.go_up(screen) 
            if reload_status:
                #sets the reload bar above the player
                reload.set_position((player.rect.center[0]-40,player.rect.center[1]+-60))
                
        if keystate[pygame.locals.K_a]:
            player.go_left(screen)
            if reload_status:
                #sets the reload bar above the player
                reload.set_position((player.rect.center[0]-40,player.rect.center[1]+-60))          
        
        if keystate[pygame.locals.K_s]:
            player.go_down(screen)
            if reload_status:
                #sets the reload bar above the player
                reload.set_position((player.rect.center[0]-40,player.rect.center[1]+-60))  
                
        if keystate[pygame.locals.K_d]:
            player.go_right(screen)         
            if reload_status:
                #sets the reload bar above the player
                reload.set_position((player.rect.center[0]-40,player.rect.center[1]+-60))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

            elif event.type==pygame.MOUSEBUTTONDOWN:

                if current_weapon == 0 and ammo[0][0]:
                    ammo[0][0]=ammo[0][0]-1
                    bullet1=sprite_module.Bullet\
                          (bullet_images[0],player.get_angle(),\
                           player.rect.center,pygame.mouse.get_pos(),12,2,double_status)
                    bullet2=sprite_module.Bullet\
                          (None,None,player.rect.center,pygame.mouse.get_pos(),12,2,double_status)
                    bullet_img.add(bullet1)
                    bullet_hitbox.add(bullet2)
                    allSprites = pygame.sprite.OrderedUpdates\
                               (bullet_img,bullet_hitbox,player,\
                                reloading,health,armour,health_text,armour_text,wave_text,ammo_text)

                elif current_weapon==4 and ammo[4][0]:
                    ammo[4][0]=ammo[4][0]-1
                    bullet1=sprite_module.RailGun\
                          (screen,player.rect.center,pygame.mouse.get_pos())
                    bullet2=sprite_module.Bullet\
                          (None,None,player.rect.center,pygame.mouse.get_pos(),20,20,double_status)
                    bullet_img.add(bullet1)
                    bullet_hitbox.add(bullet2)
                    allSprites = pygame.sprite.OrderedUpdates\
                               (bullet_img,bullet_hitbox,player,\
                                reloading,health,armour,health_text,armour_text,wave_text,ammo_text)
                    
                else:
                    #If ammo status does not equal true then generate reload box
                    if reload_status!=True and ammo[current_weapon][1]:
                        reload=sprite_module.StatusBar\
                              ((player.rect.center[0]-40,player.rect.center[1]+-60),\
                               (0,255,0),(0,0,0),(70,7),0,100,1,reload_time[current_weapon])
                        reloading.add(reload)
                        allSprites = pygame.sprite.OrderedUpdates\
                                   (bullet_img,bullet_hitbox,player,soldierGroup,\
                                    reloading,health,armour,health_text,armour_text,wave_text,ammo_text)
                    #sets reload_status to True
                    reload_status=True

            elif event.type == pygame.KEYDOWN:
                #Change player weapon
                if event.key == pygame.K_1 and weapon[0] and reload_status==False:
                    current_weapon=0
                    player.change_image(0)
                    machine_gun_fire=False

                elif event.key == pygame.K_2 and weapon[4] and reload_status==False:
                    current_weapon=4
                    player.change_image(4)
                    machine_gun_fire=False










    
    
    

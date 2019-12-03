import pygame, random, sys

#创建一个包含四张图片地址的列表
skier_images = ["C:\\Users\\高泽静\\PycharmProjects\\test\\bg_img\\skier_down.png",
                "C:\\Users\\高泽静\\PycharmProjects\\test\\bg_img\\skier_right1.png",
                "C:\\Users\\高泽静\\PycharmProjects\\test\\bg_img\\skier_right2.png",
                "C:\\Users\\高泽静\\PycharmProjects\\test\\bg_img\\skier_left1.png"]


class SkierClass(pygame.sprite.Sprite):#Sprite精灵，列表里的图片自动更新画帧，变成动态图像
    # （以下7行）创建滑雪者
    def __init__(self):#初始化，self指实例本身
        pygame.sprite.Sprite.__init__(self)#完成初始化
        self.image = pygame.image.load("C:\\Users\\高泽静\\PycharmProjects\\test\\bg_img\\skier_down.png")#加载图片skier_down.png"
        self.rect = self.image.get_rect()#获取self.image矩形大小
        self.angle = 0

    # (以下10行)滑雪者转向
    def turn(self, direction):
        self.angle = self.angle + direction
        if self.angle < -2:
            self.angle = -2
        if self.angle > 2:
            self.angle = 2
        center = self.rect.center
        self.image = pygame.image.load(skier_images[self.angle])#2和-2都是skier_right2.png
        self.rect = self.image.get_rect()
        self.rect.center = center
        speed_1 = [self.angle, 6 - abs(self.angle) * 2]
        return speed_1

    # （以下4行）滑雪者左右移动
    def move(self, speed_2):
        self.rect.centerX = self.rect.centerX + speed[0]
        if self.rect.centerX < 20:
            self.rect.centerX = 20
        if self.rect.centerX > 620:
            self.rect.centerX = 620


class ObstcleClass(pygame.sprite.Sprite):
    # （以下9行）创建树和小旗
    def __init__(self, image_file, location, type):
        pygame.sprite.Sprite.__init__(self)
        self.image_file = image_file
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.type = type
        self.passed = False

    # （以下3行）让场景向上滚动
    def update(self):
        global speed
        self.rect.center -= speed[1]
        # （以下2行）删除从屏幕上方滚下的障碍物
        if self.rect.centery < -32:
            self.kill()

    # （以下14行）创建一个窗口，包含随机的树和小旗
    def creat_map(self):
        global obstacles
        locations = []
        for i in range(10):
            row = random.randint(0, 9)
            col = random.randint(0, 9)
            lacation = [col * 64 + 20, row * 64 + 20 + 640]
            if not (lacation in locations):
                locations.append(lacation)
                type = random.choice(["tree", "flag"])
                if type == "tree":
                    img = "skier_tree.png"
                elif type == "flag":
                    img = "skier_flag.png"
                obstacle = ObstcleClass(img, lacation, type)
                obstacles.add(obstacle)

    # （以下6行）重绘屏幕
    def animate(self):
        self.screen.fill([255, 255, 255])
        obstacles.draw(self.screen)
        self.screen.blit(self.skier_image, self.skier.rect)
        self.screen.blit(self.score_text, [10, 10])
        pygame.display.flip()

    # （以下10行）做好准备
    pygame.init()
    screen = pygame.display.set_mode([640, 640])
    clock = pygame.time.Clock()
    skier = SkierClass()
    speed = [0, 6]
    obstacles = pygame.sprite.Group()
    map_position = 0
    points = 0
    creat_map()
    font = pygame.font.Font(None, 50)
    # （以下2行）开始主循环
    running = True
    while running:
        clock.tick(30)
        # 每秒更新30次图形（以下9行）检查按键或窗口是否关闭
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    speed = skier.turn(-1)
                elif event.key == pygame.K_RIGHT:
                    speed = skier.turn(1)
            # 移动滑雪者
            skier.move(speed)
            # 滚动场景
            map_position += speed[1]
            # （以下3行）创建一个新窗口，包含场景
            if map_position >= 640:
                creat_map()
                map_position = 0
                hit = pygame.sprite.spritecollide(skier, obstacles, False)
                # （以下13行）检查是否碰到树或得到小旗
                if hit:
                    if hit[0].type == "tree" and not hit[0].passed:
                        points = points - 100
                        skier.image = pygame.image.load("C:\\Users\\高泽静\\PycharmProjects\\test\\bg_img\\skier_crash.png")
                        animate()
                        pygame.time.delay(1000)
                        skier.image = pygame.image.load("C:\\Users\\高泽静\\PycharmProjects\\test\\bg_img\\skier_down.png")
                        skier.angle = 0
                        speed = [0, 6]
                        hit[0].passed = True
                    elif hit[0].type == "flag" and not hit[0].passed:
                        points += 10
                        hit[0].kill()
                obstacles.update()
                # 显示得分
                score_text = font.render("Score:" + str(points), 1, (0, 0, 0))
                animate()
            pygame.quit()

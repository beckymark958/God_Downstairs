class Person:
    def __init__(self, width, height, x, y, photo):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.x_change = 0
        self.photo = photo        
        self.life_count = 12

    def Update():
        ''' Update person's moving and life '''
        # Event Handling
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:            # 若按鍵被按下
                if event.key == pygame.K_LEFT:          # 按左鍵
                    self.x_change += -5
                if event.key == pygame. K_RIGHT:        # 按右鍵
                    self.x_change += 5
            if event.type == pygame.KEYUP:              # 若按鍵放開就不動
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.x_change = 0
        
        # Handles horizontal movements
        self.x += self.x_change
        # Check horizontal bounds
        if self.x <= 0:                                 # 碰到左邊邊線不動
            self.x = 0
        if self.x + self.width >= display_width * 0.6:  # 碰到右邊邊線不動
            self.x = display_width * 0.6 - self.width

        # Handles verticla Movement
        self.y += 10                                    # 自然落下
        if self.y > display_height:                     # 落下超過下邊線就GameEnd
            GameEnd()
        if self.y <= 0:                                 # 若頭刺到上面刺刺
            self.y += 20                                # 繼續自然落下(從梯子上面被擠下)
            self.life_count += -5                       # 命減5
            if self.life_count <= 0:                    # 檢查是否死掉，死了就GameEnd
                GameEnd()

    def General():
        ''' 人碰到一般梯子時 '''
        self.y += -20                                   # 若梯子是-10往上，要抵銷自然落下就要-20
        if self.life_count < 12:                        # 若沒滿血就加一
            self.life_count += 1
            
    def Hurt():
        ''' 人碰到刺刺梯子時 '''
        self.y += -20
        self.life_count += -5                           # 命減5
        if self.life_count <= 12:                       # 檢查是否死掉，死了就GameEnd
            GameEnd()

    def Disappear():
        ''' 人碰到消失梯子 '''
        if self.life_count < 12:                        # 若沒滿血就加一
            self.life_count += 1
    
    



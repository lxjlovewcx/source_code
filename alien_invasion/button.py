import pygame.font  #这样一个模块可以让文本渲染在屏幕上

class Button():

    def __init__(self, screen, msg, setting):  #msg是在按钮中需要显示的文本
                                                #screen，因为需要设置按钮的位置，必然与screen存在联系
                                                #
        """ 初始化按钮的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #设置按钮的尺寸和其他属性
        self.width, self.height = 200, 50   #设置按钮的尺寸

        self.button_color = (0, 255, 0)    #设置按钮的颜色

        self.text_color = (255, 255, 255)   #设置文本的颜色

        self.font = pygame.font.SysFont(None, 48)   #指定使用什么文字来渲染文本，None表示使用默认字体，
                                                    # 48为文本的字号

        #创建按钮的rect对象， 并使其居中
        self.button_rect = pygame.Rect(0, 0, self.width, self.height)   #创建按钮对象
        self.button_rect.center = self.screen_rect.center    #设置按钮的位置

        #标签的按钮只能创建一次， 每次生成按钮是自动执行。
        self.prep_msg(msg)  #将要显示的字符串渲染为图像来处理文本

    def prep_msg(self, msg):
        """将msg渲染为图像， 并使其在按钮上居中"""
        #使用font.render 方法将存储在msg中的文字转换成具有设定字体颜色，字体字号，字体，
        # 以及背景色的图片，并存储在msg_image中，接受的第二个实参表示开启反锯齿功能。
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)

        # 将生成的图片使用get_rect方法获取rect属性值。
        self.msg_image_rect = self.msg_image.get_rect()

        #将按钮实例的中心坐标传递个图片实例，使其重合。
        self.msg_image_rect.center = self.button_rect.center

    def draw_button(self):
        #绘制一个用颜色填充的按钮，再绘制文本。
        #调用screen.fill来绘制表示按钮的矩形。
        self.screen.fill(self.button_color, self.button_rect)

        #再调用screen.blit向他传递一张图像和图像相关联的rect对象。
        self.screen.blit(self.msg_image, self.msg_image_rect)
import pygame.font
class Scoreboard():
    """
    用于记录当前分数，最高分数，等级和剩余外星人数
    """
    def __init__(self, screen, aliens, game_stats, ):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.game_stats = game_stats
        self.aliens = aliens

        """
        计分板相关设置
        """
        self.width, self.height = 80, 150  # 设置计分板的尺寸

        self.scoreboard_color = (255, 255, 255)  # 设置计分板的颜色

        self.text_color = (0, 0, 0)  # 设置文本的颜色

        self.font = pygame.font.SysFont(None, 30)  # 指定使用什么文字来渲染文本，None表示使用默认字体，
        # 48为文本的字号

        # 创建计分板



        #将数字渲染为图像
        self.prep_score()

        #准备最高得分的图像
        self.prep_high_score()

    def prep_score(self):
        """将得分渲染为图像"""
        round_scores= int(round(self.game_stats.score, -1))  #将分数设置为10的倍数
        self.score_str = "{:,}".format(round_scores)
        self.score_image = self.font.render(self.score_str, True, self.text_color, self.scoreboard_color)
        # 将生成的图片使用get_rect方法获取rect属性值。
        self.score_image_rect = self.score_image.get_rect()

        self.score_image_rect.right = self.screen_rect.right  # 设置按钮的位置
        self.score_image_rect.top = self.screen_rect.top

    def prep_high_score(self):
        """将得分渲染为图像"""
        round_high_scores = int(round(self.game_stats.hightest_score, -1))  # 将分数设置为10的倍数
        self.score_high_str = "{:,}".format(round_high_scores)
        self.high_score_image = self.font.render(self.score_high_str, True, self.text_color, self.scoreboard_color)

        # 将生成的图片使用get_rect方法获取rect属性值。
        self.high_score_image_rect = self.high_score_image.get_rect()

        # 将按钮实例的中心坐标传递个图片实例，使其重合。
        self.high_score_image_rect.top = self.screen_rect.top
        self.high_score_image_rect.centerx = self.screen_rect.centerx


    def draw_scoreboard(self):

        # 再调用screen.blit向他传递一张图像和图像相关联的rect对象。
        self.screen.blit(self.score_image, self.score_image_rect)

        self.screen.blit(self.high_score_image, self.high_score_image_rect)
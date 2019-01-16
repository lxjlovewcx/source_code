class Gamestats():
    """用于跟踪游戏里面的统计信息"""

    def __init__(self, setting):
        """初始化统计信息"""
        self.setting = setting

        #初始化时就需要执行下面语句，同时在后面开始新游戏时也可以调用reset_stats,
        #做到一举两得
        self.reset_stats()

        #游戏刚启动时处于非活动状态。
        self.game_active = False

        #玩家得分
        self.score = 0

        #玩家最高得分,因为在任何情况下都不会重置得分，因此我们在__init__中写，而不是reset_stats中编写
        self.hightest_score = 0

    def reset_stats(self):
        """初始化在游戏过程中可能变化的统计信息"""
        #初始化执行这样的语句后，self.ship_left 变成了实例的属性，可以供实例的其他方法使用。
        #相当于在方法中添加了属性
        self.ship_left = self.setting.ship_limit
        self.score = 0



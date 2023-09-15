"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This extension program also
plays a break out game in which players
moving the paddle to make the ball bounce
and break all bricks!

When players break different rows of bricks,
they get different scores which is showed
at the lower left in the canvas
"""

from campy.gui.events.timer import pause
from extensionsgraphics import ExtensionsGraphics
import math

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3		    # Number of attempts


def main():
    graphics = ExtensionsGraphics()

    # Add the animation loop here!
    num_lives = NUM_LIVES
    brick_nums = graphics.b_n  # total bricks
    score = graphics.score  # 計分板
    flag_bonus = False  # bonus rect往下掉的開關
    flag_more_bonus = False  # more bonus rect往下掉的開關
    flag_get_more_bonus = False  # more bonus rect得到一次與否的開關，用來避免重複得到more bonus rect

    while True:
        pause(FRAME_RATE)
        if num_lives == 0:  # lose
            graphics.gameover()
        else:
            if graphics.isclicked:
                num_lives -= 1
                dx = graphics.get_dx()
                dy = graphics.get_dy()

                while True:
                    if brick_nums == 0:  # win
                        graphics.win()
                    else:

                        # Update
                        graphics.ball.move(dx, dy)

                        # Check
                        # 檢查球的4個座標
                        for i in range(2):
                            for j in range(2):

                                # print(maybe_obj)可得maybe_obj是GRect(寬, 高, x=?, y=?)
                                maybe_obj = graphics.window.get_object_at(graphics.ball.x + i * graphics.b_r * 2,
                                                                          graphics.ball.y + j * graphics.b_r * 2)
                                # 當球撞到paddle或bricks
                                if maybe_obj is not None and maybe_obj is not graphics.score_label and maybe_obj is not graphics.rect_bonus and maybe_obj is not graphics.rect_more_bonus:

                                    # self.paddle只有一個，把它寫在if條件
                                    # 上下兩個條件不用and寫在一起之原因: paddle會在下一次碰撞被remove，所以分開寫。
                                    # 當ball撞到paddle，且球的y方向速度為正(表示向下)，才可以改變他的y方向，
                                    # 否則會出現ball卡在paddle裡上下震動
                                    if maybe_obj is graphics.paddle:
                                        if dy > 0:
                                            dy = -dy
                                    else:

                                        # 其餘皆是撞到brick，此題的if...else...不可寫相反，
                                        # 因為self.brick是最後一個被產生的磚塊，其餘的磚塊已不是self.brick
                                        # 所以若把brick寫在if條件，會無法remove bricks
                                        if math.floor(graphics.ball.x + graphics.b_r * 2) % (graphics.brick.width + graphics.bs) == 0 or math.ceil(graphics.ball.x) % (graphics.brick.width + graphics.bs) == graphics.brick.width:
                                            dx = -dx  # 當球撞到brick的左右兩側，x方向改變
                                        else:
                                            # 當球撞到brick的上下兩側，y方向改變
                                            dy = -dy
                                        graphics.window.remove(maybe_obj)
                                        brick_nums -= 1

                                        if maybe_obj.y < 42:  # when ball hits the first row
                                            score += 4

                                            # x_speed gets faster
                                            if dx > 0:
                                                dx += 0.2
                                            else:
                                                dx -= 0.2

                                        elif maybe_obj.y < 83:  # when ball hits the second and third row
                                            score += 2

                                            # x_speed gets faster
                                            if dx > 0:
                                                dx += 0.1
                                            else:
                                                dx -= 0.1

                                            if 315 <= maybe_obj.x <= 355 and 65 <= maybe_obj.y <= 80:  # 當球撞到藏有bonus的磚塊
                                                flag_bonus = True  # bonus rect exists or not
                                                graphics.window.add(graphics.rect_bonus, x=315, y=65)

                                            if 135 <= maybe_obj.x <= 175 and 45 <= maybe_obj.y <= 60 and not flag_get_more_bonus:  # 當球撞到藏有more bonus的磚塊
                                                flag_more_bonus = True  # more bonus rect exists or not
                                                graphics.window.add(graphics.rect_more_bonus, x=135, y=45)
                                        else:
                                            score += 1
                                        graphics.score_label.text = 'Score: ' + str(score)
                                    break

                            # 當球撞到paddle或bricks，用來break for i loop
                            if maybe_obj is not None:
                                break

                        if flag_bonus:
                            graphics.rect_bonus.move(0, 2)
                            for i in range(2):
                                maybe_obj2 = graphics.window.get_object_at(graphics.rect_bonus.x + i * graphics.rect_bonus.width,
                                                                              graphics.rect_bonus.y + graphics.rect_bonus.height+1)  # height若不加1，window會不斷get自己這個rect

                                if maybe_obj2 is graphics.paddle:  # 當paddle接到bonus rect
                                    graphics.window.remove(graphics.rect_bonus)
                                    old_x = graphics.paddle.x  # 存old paddle的x座標
                                    graphics.window.remove(graphics.paddle)
                                    graphics.new_paddle(old_x)
                                    flag_bonus = False
                                    break

                            # 當bonus rect掉出window
                            if graphics.rect_bonus.y + graphics.rect_bonus.height >= graphics.window.height:
                                graphics.window.remove(graphics.rect_bonus)
                                flag_bonus = False

                        if flag_more_bonus:
                            graphics.rect_more_bonus.move(0, 2)
                            for i in range(2):
                                maybe_obj3 = graphics.window.get_object_at(graphics.rect_more_bonus.x + i * graphics.rect_more_bonus.width,
                                                                          graphics.rect_more_bonus.y + graphics.rect_more_bonus.height+1)   # height若不加1，window會不斷get自己這個rect
                                # 當paddle接到more bonus rect
                                if maybe_obj3 is graphics.paddle:
                                    graphics.window.remove(graphics.rect_more_bonus)
                                    graphics.get_more_bonus()  # 在該xy位置補五次磚塊
                                    flag_get_more_bonus = True  # 使more bonus rect只會掉落一次，之後球再撞到該磚塊都不會掉落more bonus rect
                                    brick_nums += 5
                                    flag_more_bonus = False
                                    break

                            # 當more bonus rect掉出window
                            if graphics.rect_more_bonus.y + graphics.rect_more_bonus.height >= graphics.window.height:
                                graphics.window.remove(graphics.rect_more_bonus)
                                flag_more_bonus = False

                        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                            # 當球撞到牆壁，改變x的左右方向
                            dx = -dx

                        if graphics.ball.y <= 0:
                            # 當球撞到牆壁(除了地面)，改變y的上下方向
                            dy = -dy

                        elif graphics.ball.y + graphics.ball.height >= graphics.window.height:
                            graphics.reset_position()
                            break

                        # Pause
                        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This program plays a game called
"break out" in which players
moving the paddle to make the ball bounce
and break all bricks!
"""
# user端

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
import math

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()

    # Add the animation loop here!
    num_lives = NUM_LIVES
    brick_nums = graphics.b_n

    while True:
        pause(FRAME_RATE)
        if num_lives == 0:
            break
        else:
            if graphics.isclicked:
                num_lives -= 1
                dx = graphics.get_dx()
                dy = graphics.get_dy()

                while True:
                    if brick_nums == 0:
                        break
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
                                if maybe_obj is not None:

                                    # self.paddle只有一個，把它寫在if條件
                                    # 上下兩個條件不用and寫在一起之原因: paddle會在下一次碰撞被remove，所以分開寫。
                                    # 當ball撞到paddle，且球的y方向速度為正(表示向下)，才可以改變他的y方向，
                                    # 否則會出現ball卡在paddle裡上下震動
                                    if maybe_obj is graphics.paddle:

                                        # dy = -dy。不用這種寫法!
                                        # 改使用setter function的寫法，來改球的y方向
                                        if dy > 0:
                                            dy = graphics.set_vy(-1)
                                    else:
                                        # 其餘皆是撞到brick，此題的if...else...不可寫相反，
                                        # 因為self.brick是最後一個被產生的磚塊，其餘的磚塊已不是self.brick
                                        # 所以若把brick寫在if條件，會無法remove bricks
                                        if math.floor(graphics.ball.x + graphics.b_r * 2) % (
                                                graphics.brick.width + graphics.bs) == 0 or math.ceil(
                                                graphics.ball.x) % (
                                                graphics.brick.width + graphics.bs) == graphics.brick.width:
                                            dx = -dx  # 當球撞到brick的左右兩側，x方向改變
                                        else:
                                            # 當球撞到brick的上下兩側，y方向改變
                                            dy = -dy
                                        graphics.window.remove(maybe_obj)
                                        brick_nums -= 1
                                    break

                            # 當球撞到paddle或bricks，用來break for i loop
                            if maybe_obj is not None:
                                break

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
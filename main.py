"""
ongeki色图识别器v1.0
编程新手，轻喷
以及do❤氪三百
"""

import pyautogui

'''
name字典定义了第0位是LM按键，第1位是LA按键，以此类推
buttons列表从左往右依次定义了按键在屏幕上的颜色识别坐标，根据不同游戏版本和不同分辨率设定可能需要调整
colors用于临时存储当前状态下各点的颜色
base_color存储的是，在灭灯状态下，各个按键在屏幕上的颜色值
'''
name = {0: "LM", 1: "LA", 2: "LB", 3: "LC", 4: "RA", 5: "RB", 6: "RC", 7: "RM"}
buttons = [[202, 1691], [260, 1767], [333, 1767], [424, 1767], [660, 1767], [750, 1767], [840, 1767], [880, 1691]]
colors = [[], [], [], [], [], [], [], []]
base_color = [[58, 6, 7], [12, 35, 70], [0, 58, 10], [0, 58, 10], [70, 29, 29], [63, 55, 0], [63, 55, 0], [66, 59, 0]]

'''
get_color函数传入坐标，然后输出rgb颜色列表
'''


def get_color(x, y):
    pix = pyautogui.pixel(x, y)
    return [pix[0], pix[1], pix[2]]


'''
main函数用于比较颜色并输出按键的状态
'''


def main():
    while True:
        button_state = 0b00000000  # 使用一个八位的二进制数来存储一共八个按键的亮灭状态，1为亮，0为灭
        for i in range(8):
            colors[i] = get_color(buttons[i][0], buttons[i][1])  # 依次获取按键的颜色值存储至colors
        for i in range(8):
            for j in range(3):  # 分别比较colors和base_color 的rgb通道颜色
                if abs(colors[i][j] - base_color[i][j]) > 5:  # 只要有一个通道的颜色差值大于5就认为这个灯不是灭的
                    button_state = button_state | 0b10000000 >> i  # 将对应位的0改成1
                    break
        print(colors)
        print(bin(button_state))
        '''
        接下来就是把这个二进制数通过串口（pyserial）传给promicro或者esp32什么的，但这里空白太小，写不下
        '''


if __name__ == '__main__':
    main()

# ongeki-cheater
A program for getting ongeki's button light state
一个用于获取ongeki灯光亮灭状态的程序

This program is used for getting the state of the LED.
Cause I didn't know how to hook it from mu3.I wrote a python program, using pyautogui to get the color of certain area. Get the button state by comparing the color with base_color.
因为我根本不会逆向把灯光状态hook出来，所以我写了个屁眼通红程序，用pyautogui库来获取特定像素的颜色，与基准颜色比对来判断灯光的亮灭情况

This program needs customize according to your personal situation.
这个程序需要根据实际情况来修改

But it works on my computer, which has a 1080P display and running ongeki red+
我的电脑是1080P分辨率，运行的是red plus，效果优良

If your situation is not the same as mine.Then you need to change two lists in the source code.
如果你和我情况不同，则需要修改源码中的两个列表

First, you need to change the "buttons", You need to change the value to your own coordinate (You can take a screenshot before in order to get the coordinates of the buttons showing on the buttom of the screen).
首先，你需要去修改“buttons”列表，要将其中的值分别改成你的ongeki在屏幕上显示按钮的坐标（可以全图截个屏（按win+prtsc）然后到画图软件里面去看坐标）

Second, run the program and check the outputs, You need to change the certain "base_color" value to the Corresponding RGB value when the light is off.
然后，运行这个程序，他就会开始输出那些点的RGB颜色值列表，你要将base_color里面的RGB值全改成灯灭时的RGB值

When you finished, rerun the program.
完成之后，保存重新运行程序

If you have any issues, feel free to ask me.

Telegram account: @hlcmkawaii
QQ account: 1239244004

所以谁来帮我适配一下这玩意儿和esp32或者promicro的通信（（（

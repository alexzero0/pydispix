#------------
import graphics  # Здесь и далее импортируемый модуль графических примитивов(скачивается отдельно)
import pyautogui #Здесь и далее импортируемый модуль автоматизации ( скачивается отдельно )
import time # время (Стандартный модуль)
import winsound


def main():# определяем мэйн функцию
    
    win = graphics.GraphWin("DispleyPixel_v1.0", 300, 350, autoflush=True)#GraphWin("pipshot", 200, 200, autoflush=True)#создаем графическую форму размером 200х200 и элементы на ней

    x, y = pyautogui.position()#получаем в x, y координаты мыши
    r, g, b = pyautogui.pixel(x, y)# получаем в r, g, b цвет
    r1, g1, b1 = pyautogui.pixel(x, y)
    r2, g2, b2 = pyautogui.pixel(x, y)
    r3, g3, b3 = pyautogui.pixel(x, y)
    r4, g4, b4 = pyautogui.pixel(x, y)

    # Рисуем круги ====================================================================================
    
    ColorDot = graphics.Circle(graphics.Point(50, 40), 25)# создаем точку, отображающую цвет
    ColorDot.setFill(graphics.color_rgb(r, g, b))# устанавливает ей заливку из ранее полученных цветов
    ColorDot.draw(win)# рисуем на форме win

    ColorDot1 = graphics.Circle(graphics.Point(50, 92), 25)# 2
    ColorDot1.setFill(graphics.color_rgb(r1 , g1, b1))
    ColorDot1.draw(win)

    ColorDot2 = graphics.Circle(graphics.Point(50, 144), 25)# 3
    ColorDot2.setFill(graphics.color_rgb(r2 , g2 , b2))
    ColorDot2.draw(win)

    ColorDot3 = graphics.Circle(graphics.Point(50, 196), 25)# 4
    ColorDot3.setFill(graphics.color_rgb(r3 , g3 , b3))
    ColorDot3.draw(win)

    ColorDot4 = graphics.Circle(graphics.Point(50, 248), 25)# 5
    ColorDot4.setFill(graphics.color_rgb(r4 , g4 , b4))
    ColorDot4.draw(win)

    # Отображаем значения цветов =============================================================================
   
    RGBtext = graphics.Entry(graphics.Point(125 , 25), 10)# создаем RGB вывод 
    RGBtext.draw(win)# рисуем на форме win

    RGBstring = graphics.Entry(graphics.Point(125 , 45), 10)#создаем вывод цвета в web стиле
    RGBstring.draw(win)# рисуем на форме win

    RGBtext1 = graphics.Entry(graphics.Point(125 , 77), 10)# создаем RGB вывод 
    RGBtext1.draw(win)# рисуем на форме win

    RGBstring1 = graphics.Entry(graphics.Point(125 , 97), 10)#создаем вывод цвета в web стиле
    RGBstring1.draw(win)# рисуем на форме win
    
    RGBtext2 = graphics.Entry(graphics.Point(125 , 129), 10)# создаем RGB вывод 
    RGBtext2.draw(win)# рисуем на форме win

    RGBstring2 = graphics.Entry(graphics.Point(125 , 149), 10)#создаем вывод цвета в web стиле
    RGBstring2.draw(win)# рисуем на форме win
    
    RGBtext3 = graphics.Entry(graphics.Point(125 , 181), 10)# создаем RGB вывод 
    RGBtext3.draw(win)# рисуем на форме win

    RGBstring3 = graphics.Entry(graphics.Point(125 , 201), 10)#создаем вывод цвета в web стиле
    RGBstring3.draw(win)# рисуем на форме win

    RGBtext4 = graphics.Entry(graphics.Point(125 , 233), 10)# создаем RGB вывод 
    RGBtext4.draw(win)# рисуем на форме win

    RGBstring4 = graphics.Entry(graphics.Point(125 , 253), 10)#создаем вывод цвета в web стиле
    RGBstring4.draw(win)# рисуем на форме win

    RGBtext5 = graphics.Entry(graphics.Point(125 , 285), 10)# создаем RGB вывод 
    RGBtext5.draw(win)# рисуем на форме win
   
    # координаты пикселей*    ===================================================================

    Coordstring = graphics.Entry(graphics.Point(230, 35), 10)# создаем отображение координат
    Coordstring.draw(win)# рисуем на форме win

    Coordstring1 = graphics.Entry(graphics.Point(230, 87), 10)# создаем отображение координат
    Coordstring1.draw(win)# рисуем на форме win
    
    Coordstring2 = graphics.Entry(graphics.Point(230, 139), 10)# создаем отображение координат
    Coordstring2.draw(win)# рисуем на форме win

    Coordstring3 = graphics.Entry(graphics.Point(230, 191), 10)# создаем отображение координат
    Coordstring3.draw(win)# рисуем на форме win

    Coordstring4 = graphics.Entry(graphics.Point(230, 243), 10)# создаем отображение координат
    Coordstring4.draw(win)# рисуем на форме win

    i = 0

    while True: # цикл перереисовки формы
        #++i
        #f = open("text.txt","a")
        time.sleep(0.01)# задержка в 0.1 с, чтобы питон не сходил с ума# 0.1=9%# 0.2=7%#
        x, y = pyautogui.position()#получаем в x, y координаты мыши

        #y+=60#75 = 800*600 # 
        x1 = x + 3
        x2 = x + 6
        x3 = x - 3
        x4 = x - 6

        r, g, b = pyautogui.pixel(x, y)# получаем в r, g, b цвет
        r1, g1, b1 = pyautogui.pixel(x1, y)#x1 y
        r2, g2, b2 = pyautogui.pixel(x2, y)#x2 y
        r3, g3, b3 = pyautogui.pixel(x3, y)#x3 y
        r4, g4, b4 = pyautogui.pixel(x4, y)#x4 y


        if b!=-1 and b1!=-1 and b2!=-1 and b3!=-1 and b4!=-1 :

            if r>12 :
                if r/3+5>g and r/3+5>b : 
                    pass
                    #f.write(str(i)+" 0 "+graphics.color_rgb(r, g, b)+"\n")
                    #winsound.Beep(500,500)

            if r1>12 :
                if r1/3+5>g1 and r1/3+5>b1 : 
                    pass
                    #f.write(str(i)+" 1 "+graphics.color_rgb(r1, g1, b1)+"\n")
                    #winsound.Beep(500,500)

            if r2>12 :
                if r2/3+5>g2 and r2/3+5>b2 :
                    pass
                    #f.write(str(i)+" 2 "+graphics.color_rgb(r2, g2, b2)+"\n")
                    #winsound.Beep(500,500)

            if r3>12 :
                if r3/3+5>g3 and r3/3+5>b3 :
                    pass
                    #f.write(str(i)+" 3 "+graphics.color_rgb(r3, g3, b3)+"\n")

            if r4>12 :
                if r4/3+5>g4 and r4/3+5>b4 :
                    pass
                    #f.write(str(i)+" 4 "+graphics.color_rgb(r4, g4, b4)+"\n")
                    #winsound.Beep(500,500)

            ColorDot.setFill(graphics.color_rgb(r, g, b))#Обновляем цвет
            RGBtext.setText(pyautogui.pixel(x, y))#Обновляем RGB
            RGBstring.setText(graphics.color_rgb(r, g, b))#Обновляем web цвет

            ColorDot1.setFill(graphics.color_rgb(r1, g1, b1))#Обновляем цвет
            RGBtext1.setText(pyautogui.pixel(x1, y))#Обновляем RGB
            RGBstring1.setText(graphics.color_rgb(r1, g1, b1))#Обновляем web цвет

            ColorDot2.setFill(graphics.color_rgb(r2, g2, b2))#Обновляем цвет
            RGBtext2.setText(pyautogui.pixel(x2, y))#Обновляем RGB
            RGBstring2.setText(graphics.color_rgb(r2, g2, b2))#Обновляем web цвет

            ColorDot3.setFill(graphics.color_rgb(r3, g3, b3))#Обновляем цвет
            RGBtext3.setText(pyautogui.pixel(x3, y))#Обновляем RGB
            RGBstring3.setText(graphics.color_rgb(r3, g3, b3))#Обновляем web цвет

            ColorDot4.setFill(graphics.color_rgb(r4, g4, b4))#Обновляем цвет
            RGBtext4.setText(pyautogui.pixel(x4, y))#Обновляем RGB
            RGBstring4.setText(graphics.color_rgb(r4, g4, b4))#Обновляем web цвет
        
        
        Coordstring.setText(str(x)+" "+ str(y) )#Обновляем координаты
        Coordstring1.setText(str(x1)+" "+ str(y) )#Обновляем координаты #x1 y
        Coordstring2.setText(str(x2)+" "+ str(y) )#Обновляем координаты #x2 y
        Coordstring3.setText(str(x3)+" "+ str(y) )#Обновляем координаты #x3 y
        Coordstring4.setText(str(x4)+" "+ str(y) )#Обновляем координаты #x4 y

        #f.close()

        win.flush()# Даем команду на перерисовку формы
        
        

#основной код начинается ниже.
if __name__=="__main__":
    #f = open("text.txt","w")
    main()#вызываем нашу функцию.
    




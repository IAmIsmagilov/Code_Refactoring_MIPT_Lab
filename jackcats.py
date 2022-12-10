# Программа для рисования картинок

# Импорт требуемых библиотек
import pygame
from pygame.draw import rect, ellipse, circle, arc, polygon

pygame.init()

pi = 3.14
FPS = 30
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Картинка с котами и клубками")


# Рисование наклонного закрашенного эллипса
def angled_ellipse(
        surface, color, rect, angle, width=0, border_color=(255, 255, 255)):
    '''
    Рисует наклоненный на заданный угол закрашенный эллипс

    Parameters
    ----------
    surface : объект pygame.Surface
        Поверхость, на которой происходит рисование.
    color : Кортеж RGB
        Цвет эллипса.
    rect : Четырехэлементный кортеж
        Координаты описаннного около эллипса прямоугольника.
    angle : Число
        Угол наклона (в градусах).
    width : Число, optional
        Толщина окаймления эллипса. The default is 0.
    border_color : Кортеж RGB, optional
        Цвет окаймления эллипса. The default is (255, 255, 255).
    Returns
    -------
    Выводит закрашенный эллипс с заданными характеристиками на экран.

    '''

    target_rect = pygame.Rect(rect)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.ellipse(shape_surf, color, (0, 0, *target_rect.size))
    pygame.draw.ellipse(
        shape_surf, border_color, (0, 0, *target_rect.size), width)
    rotated_surf = pygame.transform.rotate(shape_surf, angle)
    surface.blit(rotated_surf, rotated_surf.get_rect(
        center=target_rect.center))


# Рисование котов
def cat_body(color, x, y, r):
    '''
    Рисует туловище кота.

    Parameters
    ----------
    color : Кортеж RGB
        Цвет туловища кота.
    x : Число
        x-координата положения туловища кота.
    y : Число
        y-координата положения туловища кота.
    r : Число
        Характерные размеры туловища кота.

    Returns
    ---------
    Функция выводит туловище кота с заданными характеристиками на экран.

    '''
    angled_ellipse(
        screen, color, (x+4.5*r, y-1.7*r, 1.2*r, 3.5*r), 65, 1,  (0, 0, 0))
    ellipse(screen, color, (x, y-1.2*1*r, 5*r, 1.2*2*r))
    ellipse(screen, (0, 0, 0), (x, y-1.2*1*r, 5*r, 1.2*2*r), 1)
    ellipse(screen, color, (x-5*r/6, y+r/6, 2.5*r/3, 1.2*r))
    ellipse(screen, (0, 0, 0), (x-5*r/6, y+r/6, 2.5*r/3, 1.2*r), 1)
    ellipse(screen, color, (x+2*r/6, y+0.8*r, 1.5*r, 2*r/3))
    ellipse(screen, (0, 0, 0), (x + 2 * r/6, y+0.8*r, 1.5*r, 2*r/3), 1)
    circle(screen, color, (x+4*r, y+0.7*r), 0.65*r)
    circle(screen, (0, 0, 0), (x+4*r, y+0.7*r), 0.65*r, 1)
    ellipse(screen, color, (x+4*r+0.45*r, y+0.7*r+0.1*r, 0.4*r, 1.1*r))
    ellipse(screen, (0, 0, 0), (x+4*r+0.45*r, y+0.7*r+0.1*r, 0.4*r, 1.1*r), 1)


def cat_head(color, x, y, r):
    '''
    Рисует голову кота.

    Parameters
    ----------
    color : Кортеж RGB
        Цвет головы кота.
    x : Число
        x-координата положения головы.
    y : Число
        y-координата положения головы.
    r : Число
        Характерные размеры головы кота.

    Returns
    ---------
    Функция выводит голову кота с заданными характеристиками на экран.

    '''
    ellipse(screen, color, (x-1.05*r, y-1.05*r, 2*r*1.15, 2*r))
    ellipse(screen, (0, 0, 0), (x - 1.05 * r,
            y - 1.05 * r, 2 * r * 1.15, 2*r), 1)


def cat_ear(color, x, y, r):
    '''
    Рисует уши кота.

    Parameters
    ----------
    color : Кортеж RGB
        Цвет ушей кота.
    x : Число
        x-координата положения ушей кота.
    y : Число
        y-координата положения ушей кота.
    r : Число
        Характерные размеры ушей кота.

    Returns
    ---------
    Функция выводит уши кота с заданными характеристиками на экран.

    '''
    polygon(screen, color, [
        [x+5*r*1.15/15, y-14*r/15],
        [x+12*r*1.15/15, y-8*r/15],
        [x+5.5*r*1.15/6, y-6.5*r/6]])
    polygon(screen, color, [
        [x-5*r*1.15/15, y-14*r/15],
        [x-12*r*1.15/15, y-8*r/15],
        [x-5.5*r*1.15/6, y-6.5*r/6]])
    polygon(screen, (0, 0, 0), [
        [x+5*r*1.15/15, y-14*r/15],
        [x+12*r*1.15/15, y-8*r/15],
        [x+5.5*r*1.15/6, y-6.5*r/6]], 1)
    polygon(screen, (0, 0, 0), [
        [x-5*r*1.15/15, y-14*r/15],
        [x-12*r*1.15/15, y-8*r/15],
        [x-5.5*r*1.15/6, y-6.5*r/6]], 1)


def cat_eyes(color, color_eye, x, y, r):
    '''
    Рисует кота.

    Parameters
    ----------
    color : Кортеж RGB
        Цвет кота.
    color_eye : Кортеж RGB
        Цвет глаз кота.
    x : Число
        x-координата положения глаз кота.
    y : Число
        y-координата положения глаз кота.
    r : Число
        Характерные размеры глаз кота.

    Returns
    ---------
    Функция выводит глаза кота с заданными характеристиками на экран.

    '''
    circle(screen, color_eye, (x+3*r/5, y), r/3)
    circle(screen, color_eye, (x-2.5*r/5, y), r/3)
    circle(screen, (0, 0, 0), (x+3*r/5, y), r/3, 1)
    circle(screen, (0, 0, 0), (x-2.5*r/5, y), r/3, 1)
    ellipse(screen, (0, 0, 0), (x+3.2*r/5, y-r/4, r/10, r/2))
    ellipse(screen, (0, 0, 0), (x-2.3*r/5, y-r/4, r/10, r/2))
    polygon(screen, color, [
        [x+r*8/15, y-13.3*r/15],
        [x+13*r/15, y-10*r/15],
        [x+5.5*r*1/6, y-6*r/6]])
    polygon(screen, color, [
        [x-r*8/15, y-13.3*r/15],
        [x-13*r/15, y-10*r/15],
        [x-5.5*r*1/6, y-6*r/6]])
    polygon(screen, color, [
        [x-2*r/30, y+r*9/30],
        [x+4*r/30, y+r*9/30],
        [x+r/30, y+r*14/30]])
    polygon(screen, (0, 0, 0), [
        [x-2*r/30, y+r*9/30],
        [x+4*r/30, y+r*9/30],
        [x+r/30, y+r*14/30]], 1)
    polygon(screen, (0, 0, 0), [
        [x+r/30, y+r*20/30], [x+r/30, y+r*14/30]], 1)
    angled_ellipse(
        screen, (255, 255, 255), (x+2.45*r/5, y-r/4, r/8, r/3), 30, 2)
    angled_ellipse(
        screen, (255, 255, 255), (x-3.05*r/5, y-r/4, r/8, r/3), 30, 2)


def cat_nose(color, x, y, r):
    '''
    Рисует кота.

    Parameters
    ----------
    color : Кортеж RGB
        Цвет кота.
    x : Число
        x-координата положения носа кота.
    y : Число
        y-координата положения носа кота.
    r : Число
        Характерные размеры носа кота.

    Returns
    ---------
    Функция выводит нос кота с заданными характеристиками на экран.

    '''
    arc(screen, (0, 0, 0), (x+r/30, y+r*20/30 -
                            r/10, 2*r/10, 2*r/10), 2*pi/2, 2*pi-pi/4)
    arc(screen, (0, 0, 0), (x+r/30-2*r/10, y+r*20 /
                            30-r/10, 2*r/10, 2*r/10), 2*pi/2+pi/4, 2*pi)
    arc(screen, (0, 0, 0), (x+r/30+r/4,
                            y+r*16/30-r/8, r, r/4), pi/6, pi)
    arc(screen, (0, 0, 0), (x+r/30+r/4,
                            y+r*18/30-r/8, r, r/4), pi/6, pi)
    arc(screen, (0, 0, 0), (x+r/30+r/4,
                            y+r*20/30-r/8, r, r/4), pi/6, pi)
    arc(screen, (0, 0, 0), (x+r/30-r/4-r,
                            y+r*16/30-r/8, r, r/4), 0, 5*pi/6)
    arc(screen, (0, 0, 0), (x+r/30-r/4-r,
                            y+r*18/30-r/8, r, r/4), 0, 5*pi/6)
    arc(screen, (0, 0, 0), (x+r/30-r/4-r,
                            y+r*20/30-r/8, r, r/4), 0, 5*pi/6)
    angled_ellipse(
        screen, (255, 255, 255), (x+2.45*r/5, y-r/4, r/8, r/3), 30, 2)
    angled_ellipse(
        screen, (255, 255, 255), (x-3.05*r/5, y-r/4, r/8, r/3), 30, 2)


def cat(color, color_eye, x, y, r):
    '''
    Рисует кота.

    Parameters
    ----------
    color : Кортеж RGB
        Цвет кота.
    color_eye : Кортеж RGB
        Цвет глаз кота.
    x : Число
        x-координата положения кота.
    y : Число
        y-координата положения кота.
    r : Число
        Характерные размеры кота.

    Returns
    ---------
    Функция выводит кота с заданными характеристиками на экран.

    '''
    cat_body(color, x, y, r)
    cat_head(color, x, y, r)
    cat_ear(color, x, y, r)
    cat_eyes(color, color_eye, x, y, r)
    cat_nose(color, x, y, r)


# Рисование клубка
def tangle(x, y, r):
    '''
    Рисует клубок

    Parameters
    ----------
    x : Число
        x-координата центра клубка.
    y : Число
        y-координата центра клубка.
    r : Число
        Радиус клубка.

    Returns
    -------
    Возвращает клубок с заданными характеристиками.

    '''
    circle(screen, (139, 139, 122), (x, y), r)
    circle(screen, (0, 0, 0), (x, y), r, 1)
    arc(screen, (0, 0, 0), (x-r/2, y-r/4, r, r/2), pi/2, pi)
    arc(screen, (0, 0, 0), (x-r/4, y-r/6, 4*r, r/2), 5*pi/6, pi)
    arc(screen, (0, 0, 0),
        (x-r/1.4, y-r/2, 6*r, r/2), 4.5*pi/6, pi)
    arc(screen, (0, 0, 0), (x+r/4, y -
                            r/2, r/2, r), 4.5*pi/6, 4.8*pi/6)
    arc(screen, (0, 0, 0), (x+r/6, y-r /
                            4, r/2, 4*r), 4.5*pi/6, 4.9*pi/6)
    arc(screen, (0, 0, 0), (x+r/2, y-r /
                            1.4, r/2, 6*r), 4.5*pi/6, 4.9*pi/6)
    arc(screen, (0, 0, 0), (x, y+r-r/4, 8*r, r/2), pi, 3*pi/2)


# Начало отрисовки картинки


# Первое окно
rect(screen, (245, 245, 245), (0, 0, 800, 360))
rect(screen, (210, 210, 210), (0, 360, 800, 800-360))
rect(screen, (132, 112, 255), (500, 50, 270, 270))
rect(screen, (190, 190, 190), (500, 50, 270, 20))
rect(screen, (190, 190, 190), (500, 50, 20, 270))
rect(screen, (190, 190, 190), (500, 270+50, 290, 20))
rect(screen, (190, 190, 190), (500+270, 50, 20, 270))
rect(screen, (190, 190, 190), (500+270/2, 50, 20, 270))
rect(screen, (190, 190, 190), (500+270/2, 50+270/2, 270/2, 20))


# Второе окно
rect(screen, (132, 112, 255), (200, 50, 270, 270))
rect(screen, (190, 190, 190), (200, 50, 270, 20))
rect(screen, (190, 190, 190), (200, 50, 20, 270))
rect(screen, (190, 190, 190), (200, 270+50, 290, 20))
rect(screen, (190, 190, 190), (200+270, 50, 20, 270))
rect(screen, (190, 190, 190), (200+270/2, 50, 20, 270))
rect(screen, (190, 190, 190), (200+270/2, 50+270/2, 270/2, 20))


# Третье окно
rect(screen, (132, 112, 255), (-100, 50, 270, 270))
rect(screen, (190, 190, 190), (-100, 50, 270, 20))
rect(screen, (190, 190, 190), (-100, 50, 20, 270))
rect(screen, (190, 190, 190), (-100, 270+50, 290, 20))
rect(screen, (190, 190, 190), (-100+270, 50, 20, 270))
rect(screen, (190, 190, 190), (-100+270/2, 50, 20, 270))
rect(screen, (190, 190, 190), (-100+270/2, 50+270/2, 270/2, 20))


# Отрисовка котов
cat((240, 255, 255), (0, 154, 205), 500, 500, 30)
cat((105, 105, 105), (0, 0, 255), 600, 600, 20)
cat((255, 255, 255), (49, 255, 1), 300, 600, 30)
cat((255, 165, 0), (0, 250, 154), 100, 450, 20)
cat((222, 184, 135), (255, 215, 0), 600, 700, 25)
cat((139, 134, 130), (30, 144, 255), 100, 650, 20)
cat((255, 215, 0), (173, 255, 47), 700, 400, 20)


# Отрисовка клубков
tangle(100, 750, 20)
tangle(350, 720, 20)
tangle(500, 730, 10)
tangle(100, 500, 25)
tangle(350, 400, 20)
tangle(500, 400, 28)
tangle(340, 500, 28)


pygame.display.update()
clock = pygame.time.Clock()
finished = False


while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

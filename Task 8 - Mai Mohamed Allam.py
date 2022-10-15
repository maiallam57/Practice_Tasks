from tkinter import *
import cv2
import numpy as np
from PIL import ImageTk, Image


car1 = cv2.imread('photomosaic-test-1a_51268762011_o.png')
car1 = cv2.resize(car1, (400, 200))

car2 = cv2.imread('photomosaic-test-1b_51269493179_o.png')
car2 = cv2.resize(car2, (400, 200))

car3 = cv2.imread('photomosaic-test-1c_51268761941_o.png')
car3 = cv2.resize(car3, (400, 200))

car4 = cv2.imread('photomosaic-test-1d_51268021482_o.png')
car4 = cv2.resize(car4, (230, 200))

car5 = cv2.imread('photomosaic-test-1e_51268761836_o.png')
car5 = cv2.resize(car5, (230, 200))

circles = []

cropping_instructions = np.zeros_like(car1)
cropping_instructions = cv2.resize(cropping_instructions, (500, 160))

subway_instructions = np.zeros_like(car1)
subway_instructions = cv2.resize(subway_instructions, (850, 300))
aim = cv2.imread("Capture.PNG")
img = aim[:, :, ]
pos1 = img[0:1000, 0:1000]
subway_instructions[20:118, 292:557] = pos1

def instructions1(img):
    menu_pos1 = (10, 25)
    menu_pos2 = (10, 50)
    menu_pos3 = (10, 75)
    menu_pos4 = (10, 100)
    menu_pos5 = (10, 125)
    menu_pos6 = (10, 150)

    cv2.putText(img, 'Simple left click: Add a circle.', menu_pos1, cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255))
    cv2.putText(img, 'Simple right click: Delete last circle.', menu_pos2, cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                (255, 255, 255))
    cv2.putText(img, 'Double right click: Delete all circle.', menu_pos3, cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                (255, 255, 255))
    cv2.putText(img, "Press'q' to go to show croped image", menu_pos4, cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255))
    cv2.putText(img, "         and go to the next image,", menu_pos5, cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255))
    cv2.putText(img, "Else to reattempt the cropping process.", menu_pos6, cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                (255, 255, 255))


def instructions2(img):
    menu_pos1 = (10, 160)
    menu_pos2 = (10, 190)
    menu_pos3 = (10, 220)
    menu_pos4 = (10, 250)
    menu_pos5 = (10, 280)

    cv2.putText(img, '\'up, down, left, right\': Control the car 1.[up, down, left, right] respectively', menu_pos1, cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255))
    cv2.putText(img, '\'w, s, a, d\': Control the car 2.[up, down, left, right] respectively', menu_pos2, cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255))
    cv2.putText(img, '\'W, S, A, D\': Control the car 3.[up, down, left, right] respectively', menu_pos3, cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255))
    cv2.putText(img, '\'t, g, f, h\': Control the car 4.[up, down, left, right] respectively', menu_pos4, cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255))
    cv2.putText(img, '\'T, G, F, H\': Control the car 5.[up, down, left, right] respectively', menu_pos5, cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255))


def draw_circle(event, x, y, flags, param):
    global circles
    if event == cv2.EVENT_LBUTTONDOWN:  # Add the circle
        circles.append((x, y))

    if event == cv2.EVENT_RBUTTONDBLCLK:  # Delete all circles
        circles[:] = []

    elif event == cv2.EVENT_RBUTTONDOWN:  # Delete last added circle
        try:
            circles.pop()
        except (IndexError):
            print("no circles to delete")


def program(namedWindow, image, perespective_txt_window):
    instructions1(cropping_instructions)
    cv2.imshow("instructions", cropping_instructions)

    cv2.namedWindow(namedWindow)

    cv2.setMouseCallback(namedWindow, draw_circle)
    h, w, c = image.shape

    clone = image.copy()

    while True:
        im = clone.copy()

        for pos in circles:
            cv2.circle(im, pos, 5, (255, 0, 0), 3)

        cv2.imshow(namedWindow, im)

        key = cv2.waitKey(1)
        if key == ord('q') or key == ord("Q"):
            break

    try:
        key = cv2.waitKey(1)
        if key == ord('q') or key == ord("Q"):
            cv2.destroyAllWindows()
            return image

        temp = image.copy()
        pts_1 = np.float32(circles)
        pts_2 = np.float32([[0, 0], [w, 0], [0, h], [w, h]])
        M = cv2.getPerspectiveTransform(pts_1, pts_2)

        dst_image = cv2.warpPerspective(temp, M, (w, h))

        cv2.imshow(perespective_txt_window, dst_image)

        key = cv2.waitKey(1)
        if key == ord('q') or key == ord("Q"):
            cv2.destroyAllWindows()

        else:
            circles[:] = []
            program(namedWindow, image, perespective_txt_window)

        return dst_image
    except:
        print(" ")
        cv2.destroyAllWindows()


car1_croped = program("car 1 ", car1, 'after perespective transform of car 1')
cv2.waitKey(0)
cv2.destroyAllWindows()

car2_croped = program("car 2 ", car2, 'after perespective transform of car 2')
cv2.waitKey(0)
cv2.destroyAllWindows()

car3_croped = program("car 3 ", car3, 'after perespective transform of car 3')
cv2.waitKey(0)
cv2.destroyAllWindows()

car4_croped = program("car 4 ", car4, 'after perespective transform of car 4')
cv2.waitKey(0)
cv2.destroyAllWindows()

car5_croped = program("car 5 ", car5, 'after perespective transform of car 5')
cv2.waitKey(0)
cv2.destroyAllWindows()

car1_croped = cv2.cvtColor(car1_croped, cv2.COLOR_BGR2RGB)
car2_croped = cv2.cvtColor(car2_croped, cv2.COLOR_BGR2RGB)
car3_croped = cv2.cvtColor(car3_croped, cv2.COLOR_BGR2RGB)
car4_croped = cv2.cvtColor(car4_croped, cv2.COLOR_BGR2RGB)
car5_croped = cv2.cvtColor(car5_croped, cv2.COLOR_BGR2RGB)

instructions2(subway_instructions)
cv2.imshow("Rules and aim", subway_instructions)


window = Tk("subway car")


def car1_move_up(event):
    canvas.move(car_image1, 0, -10)
def car1_move_down(event):
    canvas.move(car_image1, 0, 10)
def car1_move_left(event):
    canvas.move(car_image1, -10, 0)
def car1_move_right(event):
    canvas.move(car_image1, 10, 0)

def car2_move_up(event):
    canvas.move(car_image2, 0, -10)
def car2_move_down(event):
    canvas.move(car_image2, 0, 10)
def car2_move_left(event):
    canvas.move(car_image2, -10, 0)
def car2_move_right(event):
    canvas.move(car_image2, 10, 0)

def car3_move_up(event):
    canvas.move(car_image3, 0, -10)
def car3_move_down(event):
    canvas.move(car_image3, 0, 10)
def car3_move_left(event):
    canvas.move(car_image3, -10, 0)
def car3_move_right(event):
    canvas.move(car_image3, 10, 0)

def car4_move_up(event):
    canvas.move(car_image4, 0, -10)
def car4_move_down(event):
    canvas.move(car_image4, 0, 10)
def car4_move_left(event):
    canvas.move(car_image4, -10, 0)
def car4_move_right(event):
    canvas.move(car_image4, 10, 0)

def car5_move_up(event):
    canvas.move(car_image5, 0, -10)
def car5_move_down(event):
    canvas.move(car_image5, 0, 10)
def car5_move_left(event):
    canvas.move(car_image5, -10, 0)
def car5_move_right(event):
    canvas.move(car_image5, 10, 0)


window.bind("<Up>", car1_move_up)
window.bind("<Down>", car1_move_down)
window.bind("<Left>", car1_move_left)
window.bind("<Right>", car1_move_right)

window.bind("<w>", car2_move_up)
window.bind("<s>", car2_move_down)
window.bind("<a>", car2_move_left)
window.bind("<d>", car2_move_right)

window.bind("<W>", car3_move_up)
window.bind("<S>", car3_move_down)
window.bind("<A>", car3_move_left)
window.bind("<D>", car3_move_right)

window.bind("<t>", car4_move_up)
window.bind("<g>", car4_move_down)
window.bind("<f>", car4_move_left)
window.bind("<h>", car4_move_right)

window.bind("<T>", car5_move_up)
window.bind("<G>", car5_move_down)
window.bind("<F>", car5_move_left)
window.bind("<H>", car5_move_right)


canvas = Canvas(window, width=1300, height=600)
canvas.pack()

car1_croped = ImageTk.PhotoImage(image=Image.fromarray(car1_croped))
car_image1 = canvas.create_image(0, 0, image=car1_croped, anchor=NW)

car2_croped = ImageTk.PhotoImage(image=Image.fromarray(car2_croped))
car_image2 = canvas.create_image(0, 0, image=car2_croped, anchor=NW)

car3_croped = ImageTk.PhotoImage(image=Image.fromarray(car3_croped))
car_image3 = canvas.create_image(0, 0, image=car3_croped, anchor=NW)

car4_croped = ImageTk.PhotoImage(image=Image.fromarray(car4_croped))
car_image4 = canvas.create_image(0, 0, image=car4_croped, anchor=NW)

car5_croped = ImageTk.PhotoImage(image=Image.fromarray(car5_croped))
car_image5 = canvas.create_image(0, 0, image=car5_croped, anchor=NW)


window.mainloop()
cv2.waitKey(0)
cv2.destroyAllWindows()
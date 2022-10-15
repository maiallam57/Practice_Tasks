import cv2
import numpy as np
import matplotlib.pyplot as plt

def show_with_matplotlib(img, title, pos):
    img_RGB = img[:, :, ::-1]
    plt.imshow(img_RGB)
    plt.title(title)
    plt.tight_layout(pad=3)
    plt.show()

# Dictionary containing some colors:
colors = {'blue': (255, 0, 0), 'green': (0, 255, 0), 'red': (0, 0, 255), 'yellow': (0, 255, 255),
          'magenta': (255, 0, 255), 'cyan': (255, 255, 0), 'white': (255, 255, 255), 'black': (0, 0, 0),
          'gray': (125, 125, 125), 'rand': np.random.randint(0, high=256, size=(3,)).tolist(),
          'dark_gray': (50, 50, 50), 'light_gray': (220, 220, 220)}

computer_vision_book = cv2.imread("C:/Users/Mai_Allam/Desktop/vision/assets/images/computer vision.PNG")
points = []

def circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP:
        cv2.circle(computer_vision_book, (x, y), 5, colors['blue'], 3)
        points.append([x, y])
        print(points)

cv2.namedWindow("computer vision book")

cv2.setMouseCallback("computer vision book", circle)

while True:
    cv2.imshow("computer vision book", computer_vision_book)
    key = cv2.waitKey(1)

    if key == ord("q") or key == ord("Q"):
        break

pts_1 = np.float32(points)
pts_2 = np.float32([[0, 0], [700, 0], [0, 700], [600, 700]])
M = cv2.getPerspectiveTransform(pts_1, pts_2)

dst_image = cv2.warpPerspective(computer_vision_book, M, (600, 700))
show_with_matplotlib(dst_image, 'after perespective transform', 3)
key = cv2.waitKey(0)


cv2.destroyAllWindows()
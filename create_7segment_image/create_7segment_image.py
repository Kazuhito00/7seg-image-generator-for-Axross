#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import cv2 as cv
import numpy as np


def create_7segment_image(
        number=0,
        image_size=(128, 128),
        bg_color=(110, 120, 120),
        line_color=(10, 20, 20),
        line_bg_color=(90, 100, 100),
        number_width=0.5,
        number_height=0.7,
        thickness=0.2,
        blank_ratio=0.05,
        shear_x=10,
        shift=(0, 0),
):
    # 背景画像生成
    image = np.zeros((image_size[1], image_size[0], 3), dtype=np.uint8)
    image = cv.rectangle(image, (0, 0), (image_size[0], image_size[1]),
                         bg_color, cv.FILLED)

    # 7セグメント 点灯位置対応リスト
    segment_array = [
        # a  b  c  d  e  f  g
        [[1, 1, 1, 1, 1, 1, 0]],  # 0
        [[0, 1, 1, 0, 0, 0, 0]],  # 1
        [[1, 1, 0, 1, 1, 0, 1]],  # 2
        [[1, 1, 1, 1, 0, 0, 1]],  # 3
        [[0, 1, 1, 0, 0, 1, 1]],  # 4
        [[1, 0, 1, 1, 0, 1, 1]],  # 5
        [[1, 0, 1, 1, 1, 1, 1]],  # 6
        [[1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 1, 0]],  # 7
        [[1, 1, 1, 1, 1, 1, 1]],  # 8
        [[1, 1, 1, 1, 0, 1, 1]],  # 9
        [[0, 0, 0, 0, 0, 0, 1]],  # マイナス記号
        [[0, 0, 0, 0, 0, 0, 0]],  # 空白
    ]

    # 該当番号のリストを取得
    id_list = random.choice(segment_array[number])

    # セグメント描画
    for id, value in enumerate(id_list):
        if value == 1:
            draw_line_color = line_color
        elif value == 0:
            draw_line_color = line_bg_color

        image = _draw_segment(
            image,
            id,
            draw_line_color,
            number_width,
            number_height,
            thickness,
            blank_ratio,
        )

    # 傾き・位置シフト
    image = _image_shear_x(image, shear_x, borderValue=bg_color)
    image = _image_shift(image, shift, borderValue=bg_color)

    return image


def _draw_segment(
    image,
    id=0,
    line_color=(0, 0, 0),
    number_width=0.5,
    number_height=0.7,
    thickness=0.2,
    blank_ratio=0.05,
):
    image_width, image_height = image.shape[1], image.shape[0]

    offset_left = (1 - number_width) / 2
    offset_top = (1 - number_height) / 2

    point01 = (int(image_width * offset_left), int(image_height * offset_top))
    point02 = (int(image_width * (1 - offset_left)),
               int(image_height * offset_top))
    point03 = (int(image_width * (1 - offset_left)), int(image_height * 0.5))
    point04 = (int(image_width * (1 - offset_left)),
               int(image_height * (1 - offset_top)))
    point05 = (int(image_width * offset_left),
               int(image_height * (1 - offset_top)))
    point06 = (int(image_width * offset_left), int(image_height * 0.5))

    is_vertical = False
    if id == 0:  # a
        width = point02[0] - point01[0]
        height = width
        point_start = point01
        point_end = point02
    elif id == 1:  # b
        # height = point03[1] - point02[1]
        # width = height
        width = point02[0] - point01[0]
        height = width
        point_start = point02
        point_end = point03
        is_vertical = True
    elif id == 2:  # c
        # height = point04[1] - point03[1]
        # width = height
        width = point02[0] - point01[0]
        height = width
        point_start = point03
        point_end = point04
        is_vertical = True
    elif id == 3:  # d
        # width = point04[0] - point05[0]
        # height = width
        width = point02[0] - point01[0]
        height = width
        point_start = point05
        point_end = point04
    elif id == 4:  # e
        # height = point05[1] - point06[1]
        # width = height
        width = point02[0] - point01[0]
        height = width
        point_start = point06
        point_end = point05
        is_vertical = True
    elif id == 5:  # f
        # height = point06[1] - point01[1]
        # width = height
        width = point02[0] - point01[0]
        height = width
        point_start = point01
        point_end = point06
        is_vertical = True
    elif id == 6:  # g
        # width = point03[0] - point06[0]
        # height = width
        width = point02[0] - point01[0]
        height = width
        point_start = point06
        point_end = point03

    offset_thickness = (thickness / 2)

    if not is_vertical:
        contours = np.array([
            [point_start[0] + int(width * blank_ratio), point_start[1]],
            [
                int(point_start[0] + (width *
                                      (offset_thickness + blank_ratio))),
                int(point_start[1] - (height * offset_thickness))
            ],
            [
                int(point_end[0] - (width * (offset_thickness + blank_ratio))),
                int(point_end[1] - (height * offset_thickness))
            ],
            [point_end[0] - int(width * blank_ratio), point_end[1]],
            [
                int(point_end[0] - (width * (offset_thickness + blank_ratio))),
                int(point_end[1] + (height * offset_thickness))
            ],
            [
                int(point_start[0] + (width *
                                      (offset_thickness + blank_ratio))),
                int(point_start[1] + (height * offset_thickness))
            ],
        ])
    else:
        contours = np.array([
            [point_start[0], point_start[1]],
            [
                int(point_start[0] + (width * offset_thickness)),
                int(point_start[1] + (height * offset_thickness))
            ],
            [
                int(point_end[0] + (width * offset_thickness)),
                int(point_end[1] - (height * offset_thickness))
            ],
            [point_end[0], point_end[1]],
            [
                int(point_end[0] - (width * offset_thickness)),
                int(point_end[1] - (height * offset_thickness))
            ],
            [
                int(point_start[0] - (width * offset_thickness)),
                int(point_start[1] + (height * offset_thickness))
            ],
        ])

    cv.fillConvexPoly(image, points=contours, color=line_color)

    return image


def _image_shear_x(image, shear_x, borderValue=(255, 255, 255)):
    h, w = image.shape[:2]

    src = np.array([[0.0, 0.0], [0.0, 1.0], [1.0, 0.0]], np.float32)
    dest = src.copy()

    dest[:, 0] -= int(shear_x / 2)
    dest[:, 0] += (shear_x / h * (h - src[:, 1])).astype(np.float32)
    affine = cv.getAffineTransform(src, dest)

    return cv.warpAffine(image, affine, (w, h), borderValue=borderValue)


def _image_shift(image, shift=(0, 0), borderValue=(255, 255, 255)):
    h, w = image.shape[:2]

    src = np.array([[0.0, 0.0], [0.0, 1.0], [1.0, 0.0]], np.float32)
    dest = src.copy()

    dest[:, 0] += shift[0]
    dest[:, 1] += shift[1]
    affine = cv.getAffineTransform(src, dest)

    return cv.warpAffine(image, affine, (w, h), borderValue=borderValue)


def main():
    for number_id in range(12):
        image = create_7segment_image(
            number=number_id,
            image_size=(128, 128),
            bg_color=(110, 120, 120),
            line_color=(10, 20, 20),
            line_bg_color=(90, 100, 100),
            number_width=0.5,
            number_height=0.7,
            thickness=0.1,
            blank_ratio=0.05,
            shear_x=10,
            shift=(0, 0),
        )
        cv.imshow('7seg generator', image)
        cv.waitKey(500)


if __name__ == '__main__':
    main()
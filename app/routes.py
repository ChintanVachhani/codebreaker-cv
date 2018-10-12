from app import application as app, util
from flask import render_template, request
from codebreaker_cv import *
import cv2
import numpy as np


@app.route('/')
def index():
    return render_template('index.html', title='Code Breaker', page='Computer Vision API')


@app.route('/test', methods=['GET'])
def test():
    data = {
        'key': 'value'
    }
    return util.success_response(200, 'This is a test response.', data)


@app.route('/solve/sudoku', methods=['POST'])
def solveSudoku():
    data = request.get_json() or {}
    if len(data) > 0:
        buffer = data['image'].strip().split(' ')
        buffer = [int(p) for p in buffer]

        print(data['stride'] / data['bufferWidth'])

        # Vuforia Pixels to Image
        imageBuffer = []
        for row in range(0, data['bufferHeight']):
            line = []
            for col in range(0, data['bufferWidth']):
                if data['format'] == 'GRAYSCALE':
                    pixel = buffer[(row * data['stride']) + col]
                    line.append(pixel)
                else:
                    red = buffer[(row * data['stride']) + (col * 3) + 0]
                    green = buffer[(row * data['stride']) + (col * 3) + 1]
                    blue = buffer[(row * data['stride']) + (col * 3) + 2]
                    pixel = [red, blue, green]
                    line.append(pixel)
            imageBuffer.append(line)

        # Image to Vuforia Pixels
        # pixelBuffer = []
        # for row in range(0, len(imageBuffer)):
        #     for col in range(0, len(imageBuffer[0])):
        #         print(row, col)

        imageBuffer = np.asarray(imageBuffer, dtype=np.uint8)
        # print(imageBuffer)
        extension = '.PNG'
        _, result = cv2.imencode(extension, imageBuffer)
        res = cv2.imdecode(result, cv2.IMREAD_COLOR)
        print(res)

        cv2.imshow('Image', imageBuffer)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # find and fill Sudoku
        # obj = PuzzleDetection()
        # success, data = obj.detectSudokuPuzzle(imageBuffer, 9)
        # if success:
        #     print(data)
        #     success, filledImage = obj.fillSudokuPuzzle(imageBuffer, data, 9)
        #     if success:
        #         cv2.imshow('Puzzle', cv2.resize(filledImage, (600, 600)))
        #         cv2.waitKey(0)
        #         cv2.destroyAllWindows()
        #     else:
        #         print('Error occurred while filling the image with solution!')
        # else:
        #     print('Invalid image!')

    return util.success_response(200, 'This is a test response.', data)

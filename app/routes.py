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

        # print(data['stride'] / data['bufferWidth'])

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
        _, imageEncoded = cv2.imencode(extension, imageBuffer)
        imageDecoded = cv2.imdecode(imageEncoded, cv2.IMREAD_COLOR)
        # print(imageDecoded)
        #
        # cv2.imshow('Image', imageDecoded)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        # find and fill Sudoku
        # obj = PuzzleDetection()
        # success, data = obj.detectSudokuPuzzle(imageDecoded, 9)
        # if success:
        #     print(data)
        #     success, filledImage = obj.fillSudokuPuzzle(imageDecoded, data, 9)
        #     if success:
        #         # Decoded image to string
        #         imageString = ''
        #         for r in range(0, filledImage.shape[0]):
        #             for c in range(0, filledImage.shape[1]):
        #                 for p in range(0, 3):
        #                     imageString += str(filledImage[r][c][p]) + ' '
        #
        #         response = {
        #             'imageHeight': filledImage.shape[0],
        #             'imageWidth': filledImage.shape[1],
        #             'image': imageString.strip()
        #         }
        #         return util.success_response(200, 'Puzzle detected and returned.', response)
        #         # cv2.imshow('Puzzle', cv2.resize(filledImage, (600, 600)))
        #         # cv2.waitKey(0)
        #         # cv2.destroyAllWindows()
        #     else:
        #         print('Error occurred while filling the image with solution!')
        #         return util.error_response(400, 'Error occurred while filling the image with solution.')
        #
        # else:
        #     print('Invalid image!')
        #     return util.error_response(400, 'Invalid image.')

        # To return success always

        # Decoded image to string
        imageString = ''
        for r in range(0, imageDecoded.shape[0]):
            for c in range(0, imageDecoded.shape[1]):
                for p in range(0, 3):
                    imageString += str(imageDecoded[r][c][p]) + ' '

        response = {
            'imageHeight': imageDecoded.shape[0],
            'imageWidth': imageDecoded.shape[1],
            'image': imageString.strip()
        }
        return util.success_response(200, 'Puzzle detected and returned.', response)

    return util.error_response(400, 'Error detecting the puzzle.')

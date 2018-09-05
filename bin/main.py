import sys
from codebreaker_cv import *


def main():
    image = cv2.imread(sys.argv[1], 1)
    obj = PuzzleDetection()
    success, data = obj.detectSudokuPuzzle(image, int(sys.argv[2]))
    if success:
        print(data)
    else:
        print('Invalid image!')
    # obj = CharacterRecognitionWithKNN()
    # obj.generateDataForCharacterRecognitionUsingKNN()


if __name__ == "__main__":
    main()

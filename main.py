import sys
from codebreaker_cv import *


def main():
    image = cv2.imread(sys.argv[1], 1)
    obj = PuzzleDetection()
    success, data, table = obj.detect(image)
    if success:
        print(data)
        print(table)
    else:
        print('Invalid image!')
    # obj = CharacterRecognitionWithKNN()
    # obj.generateDataForCharacterRecognitionUsingKNN()


if __name__ == "__main__":
    main()

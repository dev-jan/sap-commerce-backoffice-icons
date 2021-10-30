import numpy as np
import argparse
import os
from PIL import Image


class BackofficeIconConverter:
    """
    Icon creator to convert an input file into the correct format needed by
    the SAP Commerce Backoffice framework to be used as icon in the
    explorer-tree.
    """

    #: Side length of a single image (height = width)
    SINGLE_IMAGE_SIDE_LENGTH = 16

    #: The backoffice icon file must be 16x80 as RGBA
    BACKOFFICE_ICON_SIZE = (80, 16, 4)

    def __init__(self, inputFilename: str) -> None:
        """
        Initialises a new BackofficeIconCreator that can be used to convert a
        single icon.

        :param inputFilename: Input file used as source for the conversation.
        """
        self.sourceFilename = inputFilename

    def getDefaultTargetPath(self) -> str:
        """ Create the default output path from the input name. """
        head, tail = os.path.split(self.sourceFilename)
        outFilename = f"backoffice-{tail}"
        return os.path.join(head, outFilename)

    def convertToDefault(self) -> None:
        """Convert the current file and place it under the default
        output location. If the target file already exists, it will be
        overridden.
        """
        self.convertTo(self.getDefaultTargetPath())

    def convertTo(self, targetPath: str) -> None:
        """Convert the current file and place it under the targetPath.
        If there is already a file in the given location, it will be
        overridden.
        :param targetPath: The path including filename.
        """
        sourceImage = Image.open(self.sourceFilename).convert('RGBA')
        width, height = sourceImage.size
        if (width != self.SINGLE_IMAGE_SIDE_LENGTH or
                height != self.SINGLE_IMAGE_SIDE_LENGTH):
            raise ValueError("input image must be {}x{} but {} was actually \
                    {}x{}!".format(
                self.SINGLE_IMAGE_SIDE_LENGTH,
                self.SINGLE_IMAGE_SIDE_LENGTH,
                self.sourceFilename,
                width,
                height
            ))
        sourceImg = sourceImage.load()
        outImg = np.zeros(self.BACKOFFICE_ICON_SIZE, dtype=np.uint8)

        self.__fillImageWithColor(outImg, sourceImg, 0, (127, 144, 165, 255))
        self.__fillImageWithColor(outImg, sourceImg, 1, (85, 102, 122, 255))
        self.__fillImageWithColor(outImg, sourceImg, 2, (4, 134, 224, 255))
        self.__fillImageWithColor(outImg, sourceImg, 3, (4, 134, 224, 255))
        self.__fillImageWithColor(outImg, sourceImg, 4, (190, 196, 209, 255))
        outImage = Image.fromarray(outImg)
        outImage.save(targetPath)

    def __fillImageWithColor(
        self,
        outImg: np.ndarray,
        sourceImg,
        heightDisplace: int,
        color: tuple
    ) -> None:
        heightDisplaceInPixel = heightDisplace * self.SINGLE_IMAGE_SIDE_LENGTH
        for y in range(self.SINGLE_IMAGE_SIDE_LENGTH):
            for x in range(self.SINGLE_IMAGE_SIDE_LENGTH):
                sourcePx = sourceImg[x, y]
                # take alpha value from source, the color from the target color
                color = (color[0], color[1], color[2], sourcePx[3])
                outImg[heightDisplaceInPixel + y, x] = color


def main():
    parser = argparse.ArgumentParser(
        description="Convert simple icons to the SAP Commerce Backoffice \
         explorer tree icon format. The icon must be a sprite consist of 5 \
         different color shades of the icon itself."
    )
    parser.add_argument("inputIcons", nargs="+", help="files to convert")
    parser.add_argument("-o", "--output", dest="output")
    args = parser.parse_args()

    for file in args.inputIcons:
        print(f"Process icon {file}...")
        iconConverter = BackofficeIconConverter(file)
        if args.output:
            # combine the current filename with the out folder name
            head, tail = os.path.split(file)
            targetPath = os.path.join(args.output, tail)
            iconConverter.convertTo(targetPath)
            print(f"{file} => {targetPath}")
            pass
        else:
            iconConverter.convertToDefault()
            print(f"{file} => {iconConverter.getDefaultTargetPath()}")


if __name__ == "__main__":
    main()

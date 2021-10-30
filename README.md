# SAP Commerce Cloud Backoffice icon converter

Simple Tool to create explorer tree icons for the SAP Commerce Backoffice
interface from simple icon files.

## Why is this needed?

![screenshotBackoffice](doc/screenshotBackoffice.png)

The SAP Commerce Cloud Backoffice interface requires a special crafted sprite
image to show it as icon in the explorer tree. This tool helps creating this
sprites based on a simple icon file.

![overview](doc/overview.png)

## How to use it?

The simplest case is to convert a single icon. For this you must have an input
icon meeting the following criterias:

 - Size is 16x16 pixels (given by SAP Commerce)
 - Transparent background (otherwise it will not really work)
 - File format should be "png"

To run the icons creator, make sure to have Poetry installed (see https://python-poetry.org/docs/).

Run the following command to create the sprite (replace the example icon with
your own):

```
$ poetry run backofficeIconConverter exampleIcons/star.png
Process icon exampleIcons/star.png...
exampleIcons/star.png => exampleIcons/backoffice-star.png
```

That's it! Now you can use this icon sprite in your custom Backoffice extension
as icon for your custom types. For more help on how to do this, see
[Tutorial](doc/Tutorial.md).

You can also convert multiple icons:

```
$ poetry run backofficeIconConverter ~/FolderWithSomeIcons/* --output converted
```

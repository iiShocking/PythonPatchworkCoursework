from graphics import *
import math


# region Main Program Functions
# Draws a Line
def drawLine(win, start, end, colour):
    line = Line(start, end)
    line.setFill(colour)
    line.draw(win)
    return line


# Draws a circle
def drawCircle(win, center, radius, colour):
    circle = Circle(center, radius)
    circle.setFill(colour)
    circle.setOutline(colour)
    circle.draw(win)
    return circle


# The middle section of the pill
def drawMiddle(win, topLeft, size, colour):
    middle = Rectangle(Point(topLeft.x, topLeft.y), Point(topLeft.x + size / 2, topLeft.y + size))
    middle.setFill(colour)
    middle.setOutline(colour)
    middle.draw(win)
    return middle


# Creates the 'oval' objects in the Penultimate patch
def drawPill(win, leftmostPoint, radius, colour):
    pill = []
    section1 = drawCircle(win, Point(leftmostPoint.x, leftmostPoint.y), radius, colour)
    section2 = drawMiddle(win, Point(leftmostPoint.x, leftmostPoint.y - radius), 20, colour)
    section3 = drawCircle(win, Point(leftmostPoint.x + radius, leftmostPoint.y), radius, colour)
    pill.append(section1)
    pill.append(section2)
    pill.append(section3)
    return pill


# Draw the 'Final' patch in given window, x and y being the top left corner of the patch, with a given colour Uses
# four loops to draw diagonal lines across the screen, each loop covers a section of the patch (e.g. the bottom right
# towards the middle) Uses the drawLine function to draw the patch
# Uses the drawLine function to draw the patch
def drawFinalPatch(win, x, y, colour):
    allGraphics = []
    for i in range(0, 100, 20):
        line = drawLine(win, Point(i + x, y), Point(x, i + y), colour)
        allGraphics.append(line)
    for i in range(100, -1, -20):
        line = drawLine(win, Point(x + i, y + 100), Point(x + 100, y + i), colour)
        allGraphics.append(line)
    for i in range(0, 100, 20):
        line = drawLine(win, Point(i + x, y), Point(x + 100, 100 - i + y), colour)
        allGraphics.append(line)
    for i in range(0, 100, 20):
        line = drawLine(win, Point(i + x, y + 100), Point(x, 100 - i + y), colour)
        allGraphics.append(line)
    return allGraphics


# Draw the 'Penultimate' patch in given window, x and y being the top left corner of the patch, with a given colour
# Alternates between drawing a row of shapes starting with either a circle or oval
# Uses the drawCircle and drawPill functions to draw the shapes within the row
def drawPenultimatePatch(win, x, y, colour):
    allGraphics = []
    switcher = True
    y += 10
    for i in range(0, 100, 20):
        if switcher:
            circle1 = drawCircle(win, Point(x + 10, y + i), 10, colour)
            pill1 = drawPill(win, Point(x + 30, y + i), 10, colour)
            circle2 = drawCircle(win, Point(x + 60, y + i), 10, colour)
            pill2 = drawPill(win, Point(x + 80, y + i), 10, colour)
            switcher = False
        else:
            pill1 = drawPill(win, Point(x + 10, y + i), 10, colour)
            circle1 = drawCircle(win, Point(x + 40, y + i), 10, colour)
            pill2 = drawPill(win, Point(x + 60, y + i), 10, colour)
            circle2 = drawCircle(win, Point(x + 90, y + i), 10, colour)
            switcher = True
        allGraphics.append(circle1)
        allGraphics.append(circle2)
        for item in pill1:
            allGraphics.append(item)
        for item in pill2:
            allGraphics.append(item)
    return allGraphics


# Draw the 'Plain' patch in given window, x and y being the top left corner of the patch, with a given colour
# Uses a Rectangle to create the patch
def drawPlainPatch(win, x, y, colour):
    allGraphics = []
    patch = Rectangle(Point(x, y), Point(x + 100, y + 100))
    patch.setOutline(colour)
    patch.setFill(colour)
    patch.draw(win)
    allGraphics.append(patch)
    return allGraphics


# Optional function to draw grid lines on the patchwork
def drawGridLines(win, size):
    for y in range(0, size, 100):
        for x in range(0, size, 100):
            gridLines = Rectangle(Point(x, y), Point(x + 100, y + 100))
            gridLines.draw(win)


# Check if a colour is a valid colour (e.g. in the list) and if it hasn't been chosen yet
def validateColour(colour, chosenColours):
    validColours = ["red", "green", "blue", "magenta", "orange", "yellow", "cyan"]
    newColour = colour
    newColour.lower()
    while True:
        if newColour not in validColours:
            print("Please enter a valid colour (red, green, blue, magenta, orange, yellow, cyan): ")
            newColour = input()
        elif newColour in chosenColours:
            print("Please do not repeat colours, use unique ones each time!\nEnter your next colour: ")
            newColour = input()
        else:
            return newColour


# Gathers all inputs (size, colours) and validates them
def gatherInputs():
    validSizes = ["5", "7", "9", "11"]
    chosenColours = []
    size = input("Please enter the size of the patchwork: ")
    while size not in validSizes:
        print("Please enter a correct size (5,7,9): ")
        size = input()

    colour1 = validateColour(input("Please enter the first colour: "), chosenColours)
    chosenColours.append(colour1)

    colour2 = validateColour(input("Please enter the next colour: "), chosenColours)
    chosenColours.append(colour2)

    colour3 = validateColour(input("Please enter the next colour: "), chosenColours)
    chosenColours.append(colour3)
    return int(size) * 100, chosenColours


# Mathematical function to round to the nearest 100
def roundUp(number):
    return int(math.ceil(number / 100) * 100)


# Decides which patches are the 'Final' patches
# Goes down rows and works out which two patches should be 'Final'
# Makes use of a set because otherwise the center would be duplicated
def calculateFPatches(size):
    fPatches = set()
    yLevel = 100
    center = roundUp(size / 2)
    for i in range(100, center, 100):
        fPatches.add((i, yLevel))
        fPatches.add((size - i - 100, yLevel))
        yLevel += 100
    for i in range(center, size - 100, 100):
        fPatches.add((i, yLevel))
        fPatches.add((size - i - 100, yLevel))
        yLevel += 100
    return fPatches


# endregion
# region Challenge Content
# BELOW IS CHALLENGE CONTENT:
# CHALLENGE
def updateColours(selected, keyInput):
    for patch in selected:
        for graphic in patch:
            graphic.setFill(keyInput)
            graphic.setOutline(keyInput)


# CHALLENGE
def updatePatch(win, selectedPatches, keyInput):
    updatedSelectedPatches = []
    patchesToRemove = []
    for patch in selectedPatches:
        topLeftX = patch[0].getP1().x
        topLeftY = patch[0].getP1().y
        currentColour = patch[0].config["fill"]
        if keyInput == "f":
            x = isinstance(patch[0], Line)
            if not x:
                removeDrawings(patch)
                newPatch = drawFinalPatch(win, topLeftX, topLeftY, currentColour)
                patchesToRemove.append(patch)
                updatedSelectedPatches.append(newPatch)
        elif keyInput == "p":
            x = isinstance(patch[0], Circle)
            if not x:
                removeDrawings(patch)
                newPatch = drawPenultimatePatch(win, topLeftX, topLeftY, currentColour)
                patchesToRemove.append(patch)
                updatedSelectedPatches.append(newPatch)
        elif keyInput == "q":
            x = isinstance(patch[0], Rectangle)
            if not x:
                removeDrawings(patch)
                newPatch = drawPlainPatch(win, topLeftX, topLeftY, currentColour)
                patchesToRemove.append(patch)
                updatedSelectedPatches.append(newPatch)
        else:
            pass
    return updatedSelectedPatches, patchesToRemove


# CHALLENGE
def removeDrawings(items):
    for item in items:
        item.undraw()


# CHALLENGE
def drawButton(win, text, position):
    graphicObject = []
    box = Rectangle(position, Point(position.x + 50, position.y + 30))
    box.setFill("black")
    text = Text(box.getCenter(), text)
    text.setFill("white")
    box.draw(win)
    text.draw(win)
    graphicObject.append(box)
    graphicObject.append(text)
    return graphicObject


# CHALLENGE
def highlightPatch(win, patch):
    topLeftX = patch[0].getP1().x
    topLeftY = patch[0].getP1().y
    bottomRight = Point(topLeftX + 100, topLeftY + 100)
    r = Rectangle(Point(topLeftX, topLeftY), bottomRight)
    r.setOutline("black")
    r.setWidth(3)
    r.draw(win)
    return r


# CHALLENGE
def deselectAll(currentBorders):
    removeDrawings(currentBorders)
    return []


# CHALLENGE
def imagination(allPatches):
    for patch in allPatches:
        patch[0].setFill("white")
        removeDrawings(patch)


# CHALLENGE
def selectionMode(win, allPatches, selectedPatches, currentBorders, size):
    print("Entered Selection Mode")
    button1 = drawButton(win, "OK", Point(10, 20))
    button2 = drawButton(win, "Close", Point(size - 60, 20))
    currentBorders = deselectAll(currentBorders)
    borders = currentBorders
    var = True
    while var:
        mouseClick = win.getMouse()
        if 10 < mouseClick.x < 60 and 20 < mouseClick.y < 50:
            var = False
        elif size - 60 < mouseClick.x < size - 10 and 20 < mouseClick.y < 50:
            win.close()
        else:
            x = (roundUp(mouseClick.x) - 100)
            y = (roundUp(mouseClick.y) - 100)
            for patch in allPatches:
                patchX = patch[0].getP1().x
                patchY = patch[0].getP1().y
                if patchX == x and patchY == y or patchX - 10 == x and patchY - 10 == y:
                    if patch in selectedPatches:
                        for border in borders:
                            if border.getP1().x == x and border.getP1().y == y:
                                border.undraw()
                                borders.remove(border)
                                selectedPatches.remove(patch)
                    else:
                        selectedPatches.append(patch)
                        borders.append(highlightPatch(win, patch))
    removeDrawings(button1)
    removeDrawings(button2)
    editMode(win, selectedPatches, allPatches, currentBorders, size)


# CHALLENGE
def editMode(win, selectedPatches, allPatches, currentBorders, size):
    print("Entered Edit Mode")
    allPatchesNew = allPatches
    key = win.getKey()
    while key != "=":
        if key == "s":
            selectionMode(win, allPatchesNew, [], currentBorders, size)
        elif key == "f":
            newPatches = (updatePatch(win, selectedPatches, "f"))
            for patch in allPatchesNew:
                for removalPatch in newPatches[1]:
                    if removalPatch[0].getP1().x == patch[0].getP1().x and removalPatch[0].getP1().y == patch[
                        0].getP1().y:
                        # allPatchesNew.remove(removalPatch)
                        pass
            for patch in newPatches[0]:
                allPatchesNew.append(patch)
                selectedPatches.append(patch)
        elif key == "p":
            newPatches = (updatePatch(win, selectedPatches, "p"))
            for patch in allPatchesNew:
                for removalPatch in newPatches[1]:
                    if removalPatch[0].getP1().x == patch[0].getP1().x and removalPatch[0].getP1().y == patch[
                        0].getP1().y:
                        # allPatchesNew.remove(removalPatch)
                        pass
            for patch in newPatches[0]:
                allPatchesNew.append(patch)
                selectedPatches.append(patch)
        elif key == "q":
            newPatches = (updatePatch(win, selectedPatches, "q"))
            for patch in allPatchesNew:
                for removalPatch in newPatches[1]:
                    if removalPatch[0].getP1().x == patch[0].getP1().x and removalPatch[0].getP1().y == patch[
                        0].getP1().y:
                        # allPatchesNew.remove(removalPatch)
                        pass
            for patch in newPatches[0]:
                allPatchesNew.append(patch)
                selectedPatches.append(patch)
        elif key == "d":
            selectedPatches = deselectAll(currentBorders)
            currentBorders = selectedPatches
        elif key == "c":
            updateColours(selectedPatches, "cyan")
        elif key == "b":
            updateColours(selectedPatches, "blue")
        elif key == "r":
            updateColours(selectedPatches, "red")
        elif key == "g":
            updateColours(selectedPatches, "green")
        elif key == "y":
            updateColours(selectedPatches, "yellow")
        elif key == "m":
            updateColours(selectedPatches, "magenta")
        elif key == "o":
            updateColours(selectedPatches, "orange")
        elif key == "x":
            imagination(allPatches)
        drawGridLines(win, size)
        key = win.getKey()
    win.close()


# endregion
# region Patchwork
# BELOW IS MAIN FUNCTION
# This function draws all the patches onto the window
def drawPatchwork(win, size, colours):
    allPatches = []
    center = roundUp(size / 2)
    finalPatches = calculateFPatches(size)
    yLevel = 0
    leftBlue = Point(0, yLevel)
    rightBlue = Point(size - 100, yLevel)
    for y in range(0, size, 100):
        for x in range(0, size, 100):
            if x == leftBlue.x or x == rightBlue.x:
                colour = 0
            elif leftBlue.x < x < rightBlue.x:
                colour = 1
            else:
                colour = 2

            if (x, y) in finalPatches:
                allPatches.append(drawFinalPatch(win, x, y, colours[colour]))
            elif 0 < x < size - 100 and 0 < y < size - 100:
                allPatches.append(drawPenultimatePatch(win, x, y, colours[colour]))
            else:
                allPatches.append(drawPlainPatch(win, x, y, colours[colour]))
        yLevel += 100
        if yLevel > center - 100:
            leftBlue.x -= 100
            rightBlue.x += 100
        else:
            leftBlue.x += 100
            rightBlue.x -= 100
    drawGridLines(win, size)
    return allPatches


# endregion
# region Main
def main():
    size, colours = gatherInputs()
    win = GraphWin("Patchwork Coursework", size, size)
    allPatches = drawPatchwork(win, size, colours)
    win.getMouse()
    # Challenge
    selectionMode(win, allPatches, [], [], size)


# endregion


main()

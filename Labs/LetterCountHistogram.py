__author__ = 'lena'
import turtle


def count(wrd):
    """
    Create dictionary with keys == letters in a word and
    values == no. of occurrences of that letter
    :param wrd: word
    :return: dictionary of letters / values
    """
    ltrs = {}
    for i in wrd:
        ltrs[i] = wrd.count(i)
    return ltrs


def draw_rect(trtl, h, w, lbl):
    """
    Use a turtle to draw a histogram, labeling the center of each column
    :param trtl: the turtle!
    :param h: height
    :param w: width
    :param lbl: column label
    :return: None
    """
    trtl.left(90)
    trtl.forward(h)
    trtl.right(90)
    trtl.forward(w/2)
    trtl.write(lbl, False, align='center', font=('Calibri', 11, 'bold'))
    trtl.forward(w/2)
    trtl.right(90)
    trtl.forward(h)
    trtl.left(90)


def dict_max(dic):
    """
    Find the maximum value in a dictionary
    :param dic: the dictionary
    :return: the maximum value in the dictionary
    """
    cnt = 0
    for i in dic:
        if dic[i] > cnt:
            cnt = dic[i]
    return cnt


def main():
    myword = "supercalifragilicousexpealidocious"
    letters = count(myword)
    keys = list(count(myword).keys())
    keys.sort()
    maxletter = dict_max(letters)

    wn = turtle.Screen()
    wn.setworldcoordinates(-10, 0, len(keys)*50+10, maxletter+2)
    slim = turtle.Turtle()
    slim.speed(10)


    for i in keys:
        draw_rect(slim, letters[i], 50, "{} ({})".format(i, str(letters[i])))

    wn.exitonclick()

if __name__ == '__main__':
    main()
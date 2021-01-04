"""
手机的九宫格输入法中，输入数字的键位是可以和字母键位对应的。如“2”对应“ABC”，“9”对应“WXYZ”，现假设“1”和“0”为空字符，以此规则试设计一个程序，将单词用一串数字来进行表示。
举例：
输入：cat（不区分大小写）
输出：228
"""
import string


def word_to_num(word):
    chart, arr = [], []
    num = range(2, 10)
    for i in num:
        #  2   3   4    5       6       7       8         9    ....
        # 012 345 678 91011  121314  151617  18192021  22232425  ....
        all_string = string.ascii_lowercase + string.ascii_uppercase
        if i == 8 or i == 9:
            chart.append(all_string[(4 * i - 14):(4 * i - 10)] + all_string[(4 * i + 12):(4 * i + 16)])
        else:
            chart.append(all_string[(3 * i - 6):(3 * i - 3)] + all_string[(3*i+20):(3*i+23)])
    for i in word:
        for k, v in zip(num, chart):
            if i in v:
                arr.append(str(k))
    print(int(''.join(arr)))


if __name__ == '__main__':
    # word = input("请输入转换的英文单词:\t")
    word = "AvD"
    word_to_num(word)

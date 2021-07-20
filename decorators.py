
# def decorator(func):
#     def decorated(input_text):
#         print('함수 시작')
#         func(input_text)
#         print('함수 끝')
#     return decorated
#
# @decorator
# def hello_world(input_text):
#     print(input_text)

def decorator(func):
    def decorated(w,h):
        # if isinstance(w, int) and isinstance(h,int) and w > 0 and h > 0:
        if w > 0 and h > 0:
            print('계산 시작')
            func(w,h)
        else:
            raise ValueError('양수가 아닙니다.')
    return decorated

@decorator
def rec_volume(w,h):
    print('사각형 너비:', w*h)

@decorator
def tri_volume(w,h):
    print('삼각형 너비:', w*h/2)


#hello_world('hello world')
tri_volume(5,2)
rec_volume(5,2)
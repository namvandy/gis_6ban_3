
class User:
    def __init__(self, auth):
        self.is_authenticated = auth

def login_check(func):
    def decorated(user, w, h):
        if user.is_authenticated:
            print('로그인 체크 시작')
            func(w,h)
        else:
            raise NotImplementedError("로그인 되지 않았습니다.")
    return decorated

def decorator(func):
    def decorated(w, h):
            # if isinstance(w, int) and isinstance(h,int) and w > 0 and h > 0:
            if w > 0 and h > 0:
                print('계산 시작')
                func(w, h)
            else:
                raise ValueError('양수가 아닙니다.')


    return decorated

@login_check
@decorator
def rec_volume(w,h):
    print('사각형 너비:', w*h)

@decorator
def tri_volume(w,h):
    print('삼각형 너비:', w*h/2)


tri_volume(5, 2)
rec_volume(User(False), 5,2)
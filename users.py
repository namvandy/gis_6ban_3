class User:
    def __init__(self, auth):
        self.is_authenticated = auth

    def decorator(self,func):

        def decorated(w, h):
            if self.is_authenticated:
                # if isinstance(w, int) and isinstance(h,int) and w > 0 and h > 0:
                if w > 0 and h > 0:
                    print('계산 시작')
                    func(w, h)
                else:
                    raise ValueError('양수가 아닙니다.')
            else:
                raise NotImplementedError("로그인 되지 않았습니다.")

        return decorated

    @decorator
    def rec_volume(self, w, h):
        print('사각형 너비:', w * h)

    @decorator
    def tri_volume(self, w, h):
        print('삼각형 너비:', w * h / 2)

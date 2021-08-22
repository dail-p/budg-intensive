from django.utils.deprecation import MiddlewareMixin

import time

class FakeUser:

    # определите у пользователя аттрибуты auth
    pass


# Необходимо изменить поведение указанных методов.
# Помните про __call__()
class MyMiddleware(MiddlewareMixin):

    def process_request(self, request):
        self.begin = time.time()
        time.sleep(1)
        user = FakeUser()
        if request.auth == 'VALID_TOKEN':
            user.auth = True
            request.auth = True
        else:
            user.auth = False
            request.auth = False

        return self.get_response(request)

    def process_response(self, request, response):
        runtime = time.time() - self.begin
        request.runtime = runtime
        return response

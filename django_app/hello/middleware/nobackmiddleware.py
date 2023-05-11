from django.http import HttpResponseRedirect
from django.urls import reverse

class NoBackMiddleware:
    """
    ブラウザバックを制限するmiddleware
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # 遷移前のURLを取得
        prev_url = request.session.get('prev_url')
        # 現在のURLを取得
        curr_url = request.path_info
        # 遷移前のURLと現在のURLが異なる場合は、遷移前のURLを更新
        print(f"Before if: prev_url={prev_url}, curr_url={curr_url}")
        if prev_url != curr_url:
            print("OK")
            request.session['prev_url'] = curr_url
            print(f"After if: prev_url={request.session.get('prev_url')}, curr_url={curr_url}")
        # 遷移前のURLと現在のURLが同じ場合は、ブラウザバックを制限する
        else:
            return HttpResponseRedirect(reverse('home'))
        return response

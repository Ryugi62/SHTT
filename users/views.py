from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

def logout_view(request):
    if 'user_id' in request.session:
        del request.session['user_id']  # 세션 삭제
    
    return redirect('home')  # 로그아웃 후 사용자를 로그인 페이지로 리다이렉트

def login_view(request):
    if 'user_id' in request.session:
        return redirect('home')  # 'home'은 홈페이지의 URL 이름입니다.
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 사용자 인증
        user = User.objects.filter(username=username, password=password).first()
        if user:
            # 여기서는 간단히 세션을 사용하여 로그인 상태를 관리합니다.
            request.session['user_id'] = user.id
            return redirect('home')  # 성공적으로 로그인한 후에 리다이렉트할 페이지
        else:
            messages.error(request, "로그인에 실패하였습니다.")
            return redirect('login')

    # GET 요청에 대한 처리
    return render(request, 'login.html')


def signup_view(request):
    if 'user_id' in request.session:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        # 이미 존재하는 아이디인지 체크
        if User.objects.filter(username=username).exists():
            messages.error(request, "이미 존재하는 아이디입니다.")
            return redirect('signup')

        # 사용자 입력 데이터 추출 및 저장
        nickname = request.POST.get('nickname')
        password = request.POST.get('password')
        address = request.POST.get('address')
        User.objects.create(username=username, nickname=nickname, password=password, address=address)
        
        # 회원가입 후 로그인 페이지로 리다이렉트
        return redirect('login')

    # GET 요청시 회원가입 폼 페이지 렌더링
    return render(request, 'signup.html')

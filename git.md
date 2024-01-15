## ***GUI vs CLI***
- 둘 다 인터페이스 방식
  - GUI : 그래픽 기반 (버튼 이용) 
    
    -> GitHub Desktop, **소스트리**
  - CLI : 텍스트 기반 (코드 입력) 
  
    -> GitBash(리눅스), power shell(윈도우)
- GitBash 의 장점
  
  -> 우리는 윈도우를 쓰는데 왜 리눅스 기반인 Bash를 쓸까?

  -> Bash 의 Tab 자동완성 기능이 너무 편해서

- CLI 장점 : 빠르다. 명령어 입력만 하면 바로 됨
- GUI 장점 : 그래프 보기 좋음, diff 파일 비교에 용이


---
## ***CLI 기본 문법***
- ~ : 홈 디렉토리 (리눅스는 항상 홈 디렉토리에서 시작)
- cd ~ : 홈 디렉토리
- cd - : 뒤로가기
- cd .. : 상위 폴더
- cd 폴더명 : 해당 경로로 이동
    
    -> CLI에서 가장 중요한 것: 내가 어디 있는지 (현재 디렉토리) 알아야 함
- touch 파일명.txt : 파일 생성
- mk dir 폴더명 : 폴더 생성
- ls : 현재 경로에 있는 모든 파일이나 경로 나옴
- start 파일명.확장자명 (Tab키 누르면 확장자 명 자동완성)
- rm 이름.확장자명 : 파일 삭제
- rm -r 폴더명 : 경로 삭제
- ctrl + c : 터미널 강제 종료
- ctrl + l : 터미널 Clear
- ***ctrl + shift + c : 복사***
- shift + insert : 붙여넣기

---
## ****git****
- 분산 버전 관리 시스템 (변화를 기록하고 추적하는 것)
- 인터넷 연결이 안돼도 작업 가능
- 변경 이력을 기록하고 협업을 원활하게 하는 도구

1. ***master 가 뭘까 ?***

   - Branch 명
   - Branch 기본설정 : Master
    
     (Main 일 경우 Master로 바꿔주자)
    

2. ***Branch 가 뭘까 ?***

   - Git Hub에 있는 작업 공간
   - 코드를 개발하거나 수정하는 데에 사용되는 작업 공간

3. ***Head → Master***

   - Head : 현재 작업 중인 커밋
   - Master : Head 가 가리키는 브랜치 명

---
# ****★ Git 사용법****
1. 깃 실행 ***# 1, 2번은 폴더 처음 만들 때만***
    
    git init → master(Branch 명)라고 나타남
    
2. 작성자 설정
    
    git config —global [user.name](http://user.name/) 김민채 (commit 작성자 설정)
    
    git config —global user.email [alsco9707@gmail.com](mailto:alsco9707@gmail.com)
    
    git config —global -l ***#영어 L (잘 작성되었는지 확인)***
    
3. add
    
    git add . ***# . :모든 파일을 add하라는 뜻***
    
    git status ***# add 잘 됐는지 확인 (잘 안 함)***
    
4. commit
    
    git commit -m “1월 11일 git 연습” ***# message***
    
    git log ***# commit 잘 됐는지 확인***
    
5. push ***(=업로드 **업로드 라는 말은 깃에서 안 씀)***
    
    git remote add origin URL : 로컬 저장소에 원격 저장소 주소 등록
    
    git remote -v  ***#* *어느 repository 에 연결되어있는지 나옴***
    
    git push -u 별칭 master(Branch: 작업 공간) ***# U: 처음 push할 때 하는 것***
    
    git push 별칭 +master(Branch명) ***# 강제로 push 하는 것 (덮어 씌우더라도)***
    * 최초 push 시 로그인 필요
    * 원격 저장소에는 commit이 올라가는 것 (commit 이력 없으면 못 올림)
    
        ->git log 를 해서 commit잘 됐는지 확인하자 
    
6. 특정 파일만 올리려면?
    
    일부 파일만 add를 해야함.
    
    *git add d.txt*

### ****Pull & Clone****
- pull 은 수정사항이 있을 때만 (이미 clone 있을 때-> url필요 X)
  
    git pull origin master ***→Update***

    ***원격 저장소의 변경사항만을 받아옴***
- 처음 사용하는 자리 (자리 바꿨을 때) - clone
    
    → git hub 에 있는 자료 다운받고 싶을 때
    
    git clone url ***→Download***

    원격 저장소 전체를 복제(다운로드) 
    
    → clone으로 받은 프로젝트는 이미 git init이 되어있음.

---


## ****Git과 GitHub (≠GitLab)****

*싸피에서는 보안때문에 GitHub 대신 GitLab을 쓴다*

- Git : local repository (로컬 저장소- 컴퓨터)
- GitHub : Remote repository (원격 저장소)
    
    Ex) GitLab, GitHub(多多), Bitbucket,…
    
    - 개인 프로젝트 작업 공간 (공부한 것 저장)
    - 포트폴리오
    - 프로젝트 **협업 (코드 공유)**
- Push : Git → GitHub  ***# 업로드***
- Pull : GitHub → Git  ***# 다운로드***
- Git 내의 working directory (실제 작업중인 파일)
    
    ***→ ADD :*** staging area *(git status: add 잘 됐는지 확인)*
    
    ***→ COMMIT (버전) :*** repository -영구 저장
    
    *(git log: commit 잘 됐는지 확인)*
    

★ *push 하지 않아도 git 폴더만 삭제 안 하면 add나 commit 한 거는 bash껐다 켜도 다 남아있음.*

---
# ****실습****


1. 바탕화면에 git_commit 폴더를 만들고 git저장소 생성
2. 해당 폴더 안에 a.txt 라는 텍스트 파일을 만들고,
    
    “add a.txt” 라는 커밋 메세지로 커밋 생성
    
3. 이번에는 b.txt 라는 텍스트 파일을 만들고,
    
    “add b.txt” 라는 커밋 메세지로 커밋 생성
    
4. a.txt 파일을 수정하고
    
    “update a.txt” 라는 커밋 메세지로 커밋 생성
    
5. 커밋 목록 확인
---
# **★ gitignore**

[사이트 링크](https://www.toptal.com/developers/gitignore/)

- 평소엔 파일 하나하나 add하지 않고 전체를 add함
- gitignore 을 설정해두면 필요없는 파일을 제외해둘 수 있음.
- API 키 ?? 결제 ?? public 으로 올라오면 안됨
- gitignore도 같이 push가 됨
- 파일명 : .gitignore < 여기있는거 제외
- gitignore 로 파일이나 디렉토리 정해두면 그것만 제외하고 전부 add 가 됨
- database 처럼 보안이 중요한 건 push 안되게 해야 해서 사용
- venv ← 장고를 할 때 독립적인 개발환경을 만들려고 하는 가상환경 : gitignore 설정을 해 둠

★ 이미 git의 관리를 받은 파일이나 디렉토리는 나중에 gitignore에 작성해도 적용되지 않음. -> 처음에 push하기 전부터 미리 gitignore에 만들어 둬야함.

---

## ****실습1****

1. 폴더에서 vscode로 열어서 터미널에 touch .gitignore <입력하면
    
    텍스트파일 생성.
    
2. gitignore 에다가 c.txt (ignore시키고 싶은 파일) 작성
3. 또는, 터미널에 ***echo c.txt >> .gitignore*** (ctrl + l : 터미널 clear)

## ****실습2****

1. .gitignore 파일 생성
2. c.txt 파일 .gitignore에 추가
3. add, commit, push

---

*git remote add origin(별칭) url*

*→ 로컬 저장소에 원격 저장소 주소 등록*

**git init → add , commit → remote → push (익숙해져야함)**

git init → ***clone ???*** (remote 안 해도 됨) → add, commit

git hub repository → **clone or pull** → local repository

local repository → **push** → git hub repository

최초에 push시에는 로그인 필요.

원격저장소에는 commit 이 올라가는 것. (commit 이력이 없으면 못 올림) → ***git log 해서 commit 잘 됐는지 확인!***

git pull origin master ***→Update***

원격 저장소의 변경사항만을 받아옴. (update)

→ url 안들어감 (이미 clone 했음)

git clone url ***→Download***

원격 저장소 전체를 복제(다운로드) → clone으로 받은 프로젝트는 이미 git init이 되어있음.

### pull과 clone 의 차이는 ?

- 처음 사용하는 자리 (자리 바꿨을 때) - clone
    
    → git hub 에 있는 자료 다운받고 싶을 때
    
- pull 은 수정사항이 있을 때만 (이미 clone 있음)

---

## 실습1

GitHub 활용

### TIL (Today I Learn)

1. TIL이름의 Github Repository 생성
2. 로컬 저장소 설정
3. Readme 파일생성 → 거기에 자유롭게 자기소개
4. TIL 원격저장소 추가
5. commit 목록을 push

## ****실습2****

1. clone : ***git clone url***
2. ***git pull origin master***

## 실습3

1. 기존에 이미 origin 을 추가한 로컬 저장소에 이어서 진행
2. 새로운 github repository 생성
3. origin 이 아닌 다른 이름으로 원격 저장소 추가
    
    git remote add 새로운 이름 URL
    
4. commit 목록 push
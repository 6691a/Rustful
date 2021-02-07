from rest_framework.permissions import SAFE_METHODS, BasePermission



#권한 커스텀
class PostUserPermission(BasePermission):
    messages = '게시물 편집은 작성자에게만 제한됩니다.'

    def has_object_permission(self, request, view, obj):
        #읽기 권한은 가능
        if request.method in SAFE_METHODS:
            return True
        #작성자가 같다면 혀용
        return obj.author == request.user
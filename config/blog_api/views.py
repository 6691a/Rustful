from django.shortcuts import render
from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from .permissions import PostUserPermission
from rest_framework.permissions import AllowAny,IsAdminUser, IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


# class PostList(viewsets.ModelViewSet):
#     permission_classes =[PostUserPermission]
#     serializer_class = PostSerializer
#     # queryset = Post.objects.all()

#     def get_object(self, queryset=None, **kwargs):
#         item = self.kwargs.get('pk')
#         return get_object_or_404(Post, slug=item)

#     #Custom Queryset
#     def get_queryset(self):
#         return Post.objects.all()

class PostList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)

#     def retrieve(self, request, pk=None):
#         post = get_object_or_404(self.queryset, pk = pk)
#         serializer_class = PostSerializer(post)
#         return Response(serializer_class.data)


    #가능 옵션
    # def list(self, request):
   

    # def create(self, request):
   

    # def retrieve(self, request, pk=None):
    

    # def update(self, request, pk=None):
    

    # def partial_update(self, request, pk=None):
    

    # def destroy(self, request, pk=None):
    

# ListCreateAPIView GET / POST 읽기 쓰기 지원
# class PostList(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     queryset = Post.postObjects.all()
#     serializer_class = PostSerializer

# class PostListAll(generics.ListCreateAPIView):
#     permission_classes = [ IsAuthenticated]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer



# # RetrieveDestroyAPIView GET / DELETE단일 모델의 읽기,삭제 기능 제공
# class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserPermission):
#     permission_classes = [PostUserPermission]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer



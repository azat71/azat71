from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from branch.models import Branch
from branch.serializers import BranchSerializer
from user.permissions import IsAdminUser, IsSeller, IsClient


class BranchListApiView(ListAPIView):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()
    permission_classes = (IsClient,)


class BranchCreateAPIView(CreateAPIView):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()
    permission_classes = (IsAdminUser,)


class BranchUpdateAPIView(RetrieveUpdateAPIView):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()
    permission_classes = (IsAdminUser,)


class BranchDestroyAPIView(RetrieveDestroyAPIView):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()
    permission_classes = (IsAdminUser,)

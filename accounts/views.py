from rest_framework.generics import CreateAPIView
from accounts.models import Account
from accounts.serializers import AccountSerializer


# Create your views here.
class CreateAccountView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

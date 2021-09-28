from django.forms import ModelForm
from app.models import Empresa, Produto

# Create the form class.
class EmpresaForm(ModelForm):
    class Meta:
        model = Empresa
        fields = ['nome', 'ramo']

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'quantidade', 'valor', 'empresa']
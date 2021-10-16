from django.core.exceptions import ValidationError


class ContainsLetterValidator:
    def validate(self, password, user=None):
        if not any(char.isalpha() for char in password):
            raise ValidationError(
                'Le mot de passe doit contenir une lettre', code='password_no_letters')
                
    def get_help_text(self):
        return 'Votre mot de passe doit contenir au moins une lettre majuscule ou minuscule.'





"""
Si vous voulez vérifier par exemple qu’un code postal est valide, vous pouvez définir un  PostCodeValidator  dans votre fichier de validateurs, puis le spécifier dans le formulaire.

from . import validators


class PostCodeForm(forms.Form):
    post_code = forms.CharField(max_length=10, validators=[validators.PostCodeValidator])
"""        
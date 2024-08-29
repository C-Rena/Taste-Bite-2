from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30, label="Username")
    email = forms.EmailField(max_length=254, label="Email")
    password = forms.CharField(max_length=128, label="Password", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

    
        if not username:
            self.add_error('username', "Username is required.")
        if not email:
            self.add_error('email', "Email is required.")
        if not password:
            self.add_error('password', "Password is required.")
        
        
        values = {
            "username": username,
            "email": email,
            "password": password
        }

        return cleaned_data


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=254, label="Email")
    password = forms.CharField(max_length=128, label="Password", widget=forms.PasswordInput)

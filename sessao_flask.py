from flask import Flask, session, redirect, url_for, request, render_template

app = Flask(__name__)
app.secret_key = "sua_chave_secreta"  # Troque por uma chave segura!

# Dados de usuário (simplificado - em apps reais use banco de dados)
USUARIOS = {
    "admin": "senha123"
}

# Rota pública (qualquer um pode acessar)
@app.route('/')
def home():
    return "<h1>Página Inicial - Pública</h1> <a href='/restrita'>Área Restrita</a>"

# Rota de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        
        if usuario in USUARIOS and USUARIOS[usuario] == senha:
            session['logado'] = True
            session['usuario'] = usuario
            return redirect('/restrita')
        else:
            return "Usuário ou senha incorretos! <a href='/login'>Tentar novamente</a>"
    
    return """
    <form method="POST">
        Usuário: <input type="text" name="usuario"><br>
        Senha: <input type="password" name="senha"><br>
        <button type="submit">Entrar</button>
    </form>
    """

# Rota restrita (só acessa se estiver logado)
@app.route('/restrita')
def restrita():
    if not session.get('logado'):
        return redirect('/login')
    
    return f"""
    <h1>Bem-vindo, {session['usuario']}!</h1>
    <p>Esta é uma área restrita.</p>
    <a href='/logout'>Sair</a>
    """

# Rota de logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

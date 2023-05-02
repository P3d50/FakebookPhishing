# Como criei minha ferrramenta de Phishing com Python e Django


Não me responsabilizo pelo uso indevido dessas informações, e esse conteúdo foi postado para fins educacionais.


No formulário após ter clonado a página do facebook(com python) e salvado um html dela na minha máquina, eu alterei o formulário do html salvo para enviar um POST para a url do Django que criei. Atribuí uma tag name para cada atributo do form que eu quero logar:

<img src="https://github.com/P3d50/dio-cybersecurity/blob/master/Screenshot%20from%202023-05-02%2006-27-39.png">

Na minha app do Django que exibe o html clonado e recebe o POST do formulário, eu criei essas views respectivamente para essas funcionalidades:

<img src="https://github.com/P3d50/dio-cybersecurity/blob/master/Screenshot%20from%202023-05-02%2006-33-40.png">


Essa é a página exibida:

<img src="https://github.com/P3d50/dio-cybersecurity/blob/master/Screenshot%20from%202023-05-02%2006-25-16.png">



Esse é o console onde foi logado o usuário e senha digitados:


<img src="https://github.com/P3d50/dio-cybersecurity/blob/master/Screenshot%20from%202023-05-02%2006-25-49.png">


Caso tenham dúvida de como executar o projeto na documentação do Django mostra como criar um ambiente virtual e executar um projeto Django.


https://docs.djangoproject.com/en/4.2/intro/install/


https://docs.djangoproject.com/en/4.2/intro/tutorial01/

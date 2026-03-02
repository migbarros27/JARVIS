# _Jarvis - Usando o README como diário_
Data de Começo: 06/02/2026

Basicamente esse repositório é uma tentativa de criar uma IA no estilo do JARVIS do filme Homem de Ferro. Inicialmente o plano é integrar IA de forma que auxilie no cotidiano de forma que futuramente possa ser integrados em projetos de IOT.

Para isso o primeiro passo é criar uma IA em python que funcione como um 'chatbot', e então aprimoramos para um sistema de voz no qual daria para ouvir as respostas do Sistema, criando um bate papo com ele. Após isso, criar um meio dessa IA ter acesso a documentos pessoais (penso em utilizar o Google Workspace) e poder edita-los: enviar e-mails, adicionar eventos ao calendário, planilhas dinâmicas etc - Se for fácil de integrar, gostaria de por workspaces do N8N para esses processo, mas ainda não pretendo fazer isso. Depois, tambem se for possível aos projetos de automação de casa, como ligar luzes, pré aquecer a cafeteira, coisas que facilitem a vida do usuário, ainda não sei se uso o Node-RED e MQTT ou se há algum método mais simples e funcional.
Depois desse sistema funcionando, a meta é focar na visão computacional - onde a IA poderá auxiliar com processos simples como identificação de objetos que no futuro possa ajudar em processos de organização.

25/02/2026
Encontrei uma conta no tiktok no qual eles criaram o jarvis, mas porque não melhorar? Ao invés de eu pegar o repositório, vou tentar fazer o meu próprio, então vamos continuar/começar né. O bom é que a partir do que eu vi já tenho uma base melhor para me basear. 
Pretendo começar com a captura de áudio (audioCapture), tive alguns problemas com o PyAudio agora estou utilizando um venv com python 3.13.12 onde baixaremos os programas, a princípio o SpeechRecognition e o PyAudio. Começamos, ainda tem alguns problemas de reconhecimento de fala mas vai ser funcional, comecei a implementar o pyttsx3 e estou considerando o vosk para o STT (Speech-to-Text), enfim depois de 30 min, não compensa. No processo de procurar a biblioteca do Vosk para python, encontrei "https://github.com/manipanw143/PythonTuts/blob/main/Jarvis.py",  deve ter algum proveito.

26/02/2026
Funciona, mas ainda não tem nada de IA mesmo, somente um simples assistente que faz funções básicas. Agora vou tentar implementar um pouco mais de "dinâmica", "pessoalidade" e independência nele, mas sei la bora.

Pedi para o GPT analisar o básico e ele indicou novamente o vosk como um meio offline, logo estou dando mais uma chance e está indo bem, não testei fielmente mas pela a lógica funcionará, depois irei ver a do site: https://www.freecodecamp.org/news/python-project-how-to-build-your-own-jarvis-using-python/ , o gemini o adicionou na lista então acho que verificar mais um pouco possa ajudar. Além do mais hoje eu pretendo lançar o repositório(dia 02/03)

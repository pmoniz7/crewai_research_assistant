
### **APLICATIVO MULTIAGENTE - Usando Framework CrewAI**                       

**OBJETIVO :** Criar um aplicativo multiagente para pesquisar como uma determinada tecnologia ou Framework usada na IA GEN que pode ser utilizada no setor de trabalho ou negócio.
Após o trabalho dos agentes o aplicativo irá gerar um relatório com Insight muito interessantes que ajudarão na tomada de decisão no uso OU Não 
da tecnologia ou estudo. 

O aplicativo é composto por 8 agentes de IA onde cada um tem uma função específica:

Cada função e cada tarefa dos agentes estão devidamente definidas com detalhes nos arquivos agents.Yaml e tasks.Yaml em research\config\.
**Aqui farei uma breve descrição de cada agente:**

1 - **Agent: Senior Engineer Generative AI Specialist :**
    Analisa o topic (assunto ou tecnologia ou estudo ) que o usuário deseja e extrai (**3 subtopicos**) que serão usados pelos Analistas.

2 - **Agent: Senior Business Analyst :**
    Usará o primeiro subtópico para fazer a 4 perguntas a um especialista em IA GEN e assim obter informações e conhecimento sobre o primeiro subtópico. 

3 - **Agent: Security Analyst :**
    Usará o segundo subtópico para fazer a 4 perguntas a um especialista em IA GEN e assim obter informações e conhecimento sobre o segundo subtópico.

4 - **Agent: Industry Consultant :**
    Usará o terceiro subtópico para fazer a 4 perguntas a um especialista em IA GEN e assim obter informações e conhecimento sobre o terceiro subtópico.

5 - **Agent: Senior AI Engineer I :**    
    Agente especialista em IA GEN que irá responder as perguntas feitas pelo analista (**Senior Business Analyst**).

6 - **Agent: Senior AI Engineer II :**    
    Agente especialista em IA GEN que irá responder as perguntas feitas pelo analista (**Security Analyst**).

7 - **Agent: Senior AI Engineer III :**    
    Agente especialista em IA GEN que irá responder as perguntas feitas pelo analista (**Industry Consultant**).

8 - **Agent: Technical Writer :** 
    Agente especialista em fazer relatórios, sumários, etc de forma concisa com as imformações obtidas dos Analistas e especialistas. 

---

### **Fluxo de Instalações e Execução do Projeto**.
**NOTA :** Para esse projeto usando o Framwork crewAI usaremos O UV. O UV  é um novo e moderno gerenciador de dependências para Python, desenvolvido pela Astral, mesma empresa por trás do Ruff. Ele foi criado para ser extremamente rápido, seguro e compatível com ferramentas populares como pip, pip-tools, Poetry e PDM.

#### ✅ 1. **Instale o Python**

* Acesse: [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
* Instale o python versão >=3.11 OU <3.14 (**CASO AINDA NÃO POSSUA**)
* Durante a instalação, **marque a opção "Add Python to PATH"**.

Verifique se deu certo:

```sh
python --version
```

---

#### ✅ 2. **Instale o "uv"**

```sh
pip install uv
```

---

#### ✅ 3. **Instale o Git (caso ainda não tenha)**

* Acesse: [https://git-scm.com/download/win](https://git-scm.com/download/win)
* Durante a instalação, aceite as configurações padrão.

Verifique:

```sh
git --version
```

---

#### ✅ 4. **Clone o projeto do GitHub e Crie um ambiente Virtual com o "uv"**

No terminal ou Git Bash:
**4.1 **Clone o projeto do GitHub**
```sh
git clone pmoniz7/crewai_research_assistant
cd crewai_research_assistant/research_assistant
```

**4.2 Crie um ambiente Virtual com o "uv"**
```sh
uv venv --python=3.12
.venv\Scripts\activate
```

---

#### ✅ 5. **Instale o crewai**

Vá para o diretório crewai_research_assistant/research_assistant

```sh
cd crewai_research_assistant/research_assistant
crewai install
  
```
**NOTA IMPORTANTE:**
Para este projeto você vai precisar obter algumas API KEY para execução deste aplicativo, bem como criar um arquivo .env:

Ainda no diretório crewai_research_assistant/research_assistant crie o arquivo **.env**.
O arquivo **.env** ficará como abaixo:
   
```sh
MODEL=gpt-4o-mini
OPENAI_API_KEY="sua openai api key"
```

**Aqui os links para a obtenção das API KEY:**

1-Passos para criar sua OPENAI_API_KEY

  https://platform.openai.com/settings/organization/api-keys

---

#### ✅ 6. Execute o backend 

Com o ambiente virtual ativado, vá para a pasta **research_assistant\src\research_assistant** e execute o aplicativo como abaixo:

```sh
cd ...\crewai_research_assitant\research_assistant\src\research_assistant 
uv run --active run_crew
```

---

#### ✅ 7. Verificar o resultado final do processo***

Após a execução do aplicativo será criada uma pasta chamada **outputs**
Nesta pasta teremos o arquivo Relatório com extensão Markdown sobre o que foi pesquisado pelos agentes:

Arquivo : Research_Assistant_Report_ano-mes-dia_hora_minuto -  (exemplo) -> Research_Assistant_Report_2025-07-28_15-51

---


   

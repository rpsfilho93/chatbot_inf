# chatbot_inf

Este repositório contém os arquivos referentes ao sistemas de perguntas e respostas para o chatbot do Instituto de Informática da Universidade Federal de Goiás.

## inf_corpus:

Esta pasta contém os documentos oficiais do INF/UFG que compõe a base de dados de onde as repostas são extraídas.

* ### docs:

Documentos do INF/UFG no  formato original (pdf).

* ### splits:

Documentos do INF/UFG no formato em que são utilizados pelo sistema, ou seja, secionados em trecos de 100 palavras.

## preprocessing.py:

Algoritmo usado para pré-processar os documentos INF/UFG.

## inf_qa.json:

Conjunto de teste com perguntas e respostas retiradas dos documentos INF/UFG no formato SQuAD.

## pipelines.yml:

Arquivo de configurações para usar o modelo Bert_base_faquad na REST API Haystack (https://haystack.deepset.ai/guides/rest-api).

# Como rodar localmente a REST API utilizando o modelo Bert_base_faquad e os arquivos do INF/UFG:

* Clone este repositório:
```
git clone https://github.com/rpsfilho93/chatbot_inf
```

* Instale o framework Haystack:

```
$git clone https://github.com/deepset-ai/haystack.git

cd haystack

pip install --upgrade pip
pip install -e '.[all]' ## or 'all-gpu' for the GPU-enabled dependencies

pip install rest_api/
pip install ui/

```
* Copie o arquivo 'pipelines.yml' deste repositório para a pasta /haystack/rest_api/pipeline:

```
cp ../chatbot_inf/pipelines.yml ./rest_api/pipeline

```
* Altere o arquivo 'docker-compose.yml' na pasta /haystack/rest_api: 
- Altere o valor do campo 'PIPELINE_YAML_PATH' para '/home/user/rest_api/pipeline/pipelines.yml'. 
- E retire o símbolo de comentário nas linhas abaixo:
```
# volumes:
#      - ./rest_api/pipeline:/home/user/rest_api/pipeline
```

* Use docker-compose para carregar as imagens dos serviços:
```
docker-compose pull
```

* Ative o container elasticsearch:
```
docker-compose up elasticsearch
```

* Insira os documentos do corpus INF/UFG no DocumenStore ElasticSearch com o algoritmo de pré-processamento 'preprocessing.py' contido nesse repositório:
```
python -m preprocessing
```

* Ative o container haystack_api:
```
docker-compose up haystack-api 
```

* Nesse momento a API já estará disponível na porta 8000 para requisições (http://127.0.0.1:8000/).

* A documentação sobre os endpoints da API pode ser encontrada em https://haystack.deepset.ai/guides/rest-api-definition.

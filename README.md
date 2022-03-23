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

## res_api:

Arquivos referentes à API criada para acessar o sistema de perguntas e respostas. A API é baseada na API protótipo Haystack. Mais informações em: https://github.com/deepset-ai/haystack.

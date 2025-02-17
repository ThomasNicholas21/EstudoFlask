# API
Application Programming Interface ou API, é uma forma aonde dois softwares de funções distintas realizam uma comunicação de serviços entre os dois. Application ou aplicação se refere a essas funções, e Interface significa o contrato de serviço entre duas aplicações. O contrato define como as duas aplicações se comunicam, utilizando solicitações (cliente) e respostas (servidor).

A API é um conjunto de rotinas para acesso do aplicativo/software/plataforma podendo ser baseado na Web e em programas. Sendo assim, se torna fundamental quando se tem a intenção de realizar integração com outros serviços.

**Tipo de arquitetura para APIs**
- __APIs Soap__: usam Simple Object Access Protocol (SOAP), aonde utilizam XML para troca de informações. Dessa forma, ela é menos flexível e utilizada no passado.
- __APIs RPC__: conhecidas como Remote Procedure Calls (RPC), onde o cliente conclui um procedimento no servidor e o mesmo retorna uma saída de volta ao cliente.
- __APIs WebSocket__: desenvolvimento de API quie uiso JSON para transmitir dados, oferecendo suporte bidirecional entre aplicativos clientes e o servidor. O mesmo pode enviar mensagens de retorno de chamadas de clientes conectados, podendo ser mais eficiente que API Rest.
- __APIs Rest__: esta é a mais flexível, onde o cliente envia solicitações ao servidor como dados, o servidor utilizar o mesmo para iniciar suas funções internas e retorna o mesmo.

## APIs Rest
Sendo REST transferrência representacional de estado, o mesmo define um conjunto de ações como GET, PUT E DELETE, que os cliente pode utilizar para acessar os dados de um servidor, usando HTTP. Sua ausência de estado, significa que o servidor não irá salvar os dados do cliente entre as solicitações.

O Rest API é consumido através de requisições HTTP, geralmente são representados em JSON e XML, podendo ser usádos em páginas HTML, PDF e arquivos de imagem. Na sua implementação cada método deve ser responsáverl por um tipo diferente de ação, como: 
- GET: Método que solicita recurso.
- POST: Método para envio de arquivos/dados/formulários
- PUT: Método de criar ou modificar um objeto.
- DELETE: Método de deletar através da URI

### URL x URN x URI
- _URL_: Localizador de Recursos Universal. Ex: web.dio.me
- _URN_: Nome do Recurso Universal. Ex: /category/blog
- _URI_: Identificador de Recurso Universal. Ex: https://web.dio.me/category/blog

URI une com protocolo HTTPS, URL (web.dio.me), e a URN (/category/blog)
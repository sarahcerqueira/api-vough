# vough_backend


### GET /api/orgs/<login>
	Busca uma determinada organização através do login. Se a organização for encontrada no Github, ela é salva no banco de dados, e é retornado um json com o login, nome e score.
	Caso a organização não seja encontrada é retornado o código de erro 404.
É possível também que esse get retorne o código 503, isso porque se houver requisições excessivas à API do GitHub bloqueia temporariamente o acesso à ela. 


### GET /api/orgs
	Busca todas as organizações já pesquisadas anteriormente, ordenadas por score de forma decrescente.
	É possível que algumas organizações retorne com o nome nulo, mas isso ocorre porque o próprio GitHub a organização não tem nome cadastrado.

### DELETE /api/orgs/<login>
	Remove do banco de dados uma determinada organização salva. Se a organização existir ela é removida, e retorna o código 204. Caso contrário é retornado o erro 404


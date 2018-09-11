$(document).ready(function(e) {
// evento click no botão login (quando eu clicar no botão login ele vai executar esses comandos)
$("#btnLogin").click(function(e){ // Ao clicar no botão login do formulário, irá executar os comandos abaixo.
	var vLogin = $("#cmpLogin").val(); // Estou recebendo o valor do campo Login
	var vSenha = $("#cmpSenha").val(); // Estou recebendo o valor do campo Senha
	
	if (vLogin.length == 0) { // Aqui eu verifico se digitou algo no login
		alert("Atenção\nO campo Login é obrigatório.");
		$("#cmpLogin").focus(); // Faço o foco voltar para o campo de login
	} else if (vSenha.length == 0) { // Aqui eu verifico se digitou algo no login
		alert("Atenção\nO campo Senha é obrigatório.");
		$("#cmpSenha").focus();// Faço o foco voltar para o campo de senha
	} else { // Caso o login e senha estiverem preenchidos, entra aqui.
		// Aqui vou usar o ajax (jquery), onde ele vai verificar em outro arquivo se o usuário e senha existe
		$.post("info.php", {login: vLogin, senha: vSenha}, function(retorno){
			if(retorno) { // caso o retorno for TRUE
				$("#sucessoLogin").fadeIn("fast", function(e){ // Exibir o bloco de mensagem de sucesso
					$("#sucessoLogin").delay(1500).fadeOut("fast"); // Depois de exibido, eu dou um tempo de 1,5 segundos
					$("body").delay(1500).fadeOut('fast', function(e){ // Depois oculto toda o body e redireciono (apenas efeitos.)
						window.location="https://www.scriptbrasil.com.br/forum/";
					})
				});
			} else { // caso o retorno for FALSE
				$("#cmpLogin").focus().select(); // defino o foco e seleciono o campo todo
				$("#falhaLogin").fadeIn("fast", function(e){ // Exibir o bloco de mensagem de erro
					$("#falhaLogin").delay(1500).fadeOut("fast"); // Depois de exibido, eu dou um tempo de 1,5 segundos e escondo.
				});
			}
		});
	}
})

});
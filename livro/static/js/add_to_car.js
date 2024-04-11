jQuery.noConflict();
jQuery(document).ready(function ($) {
  $(".buy-btn").click(function () {
    console.log("botão clicado =D");
    var livroId = $(this).data("livroId"); // Alterado para livroId
    var formData = $("form").serialize();

    $.ajax({
      type: "POST",
      url: "/adicionar-ao-carrinho/",
      data: {
        livro_id: livroId,
      },
      success: function (response) {
        console.log("Produto adicionado ao carrinho com sucesso!");
      },
      error: function (xhr, status, error) {
        console.error("Erro ao adicionar produto ao carrinho:", error);
      },
    });
  });
});

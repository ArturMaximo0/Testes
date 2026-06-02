
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<title>Lojinha Camargo</title>

<style>
body{
    font-family: Arial, sans-serif;
}

.container{
    width: 900px;
    margin: auto;
}

h1{
    color: #444;
}

table{
    width: 100%;
    border-collapse: collapse;
}

th, td{
    border: 1px solid #ccc;
    padding: 10px;
    text-align: center;
}

img{
    width: 120px;
}

.btn{
    border: none;
    padding: 5px 10px;
    color: white;
    cursor: pointer;
}

.menos{
    background-color: red;
}

.mais{
    background-color: green;
}

.subtotal{
    margin-top: 10px;
    text-align: right;
    font-weight: bold;
}
</style>
</head>

<body>

<div class="container">

<h1>🛒 Lojinha Camargo</h1>

<table>

<tr>
    <th>Imagem</th>
    <th>Produto</th>
    <th>Preço Unitário</th>
    <th>Qtd</th>
    <th>Total</th>
</tr>

<tr>
    <td>
        <img src="https://via.placeholder.com/120" alt="">
    </td>

    <td>
        Celular Top Motorola<br>
        Código 1234ABC<br>
        Cor Preto
    </td>

    <td>1000</td>

    <td>
        <button class="btn menos">-</button>
        3
        <button class="btn mais">+</button>
    </td>

    <td>3000</td>
</tr>

<tr>
    <td>
        <img src="https://via.placeholder.com/120" alt="">
    </td>

    <td>
        Televisão Ultra<br>
        Código 1111ABC<br>
        Cor Preto
    </td>

    <td>9000</td>

    <td>
        <button class="btn menos">-</button>
        0
        <button class="btn mais">+</button>
    </td>

    <td>0</td>
</tr>

<tr>
    <td>
        <img src="https://via.placeholder.com/120" alt="">
    </td>

    <td>
        Notebook Dell Ultra<br>
        Código 2378ABC<br>
        Cor Preto
    </td>

    <td>9000</td>

    <td>
        <button class="btn menos">-</button>
        3
        <button class="btn mais">+</button>
    </td>

    <td>27000</td>
</tr>

</table>

<div class="subtotal">
    SUBTOTAL: 30000
</div>

</div>

</body>
</html>
<?php
	$db = mysqli_connect('localhost','root','1234','mysitedb') or die('Fail');
?>
<html>
<body>
<h1>Conexión establecida</h1>
<?php
	// Lanzar una query
	$query = 'SELECT * FROM tCanciones';
	$result = mysqli_query($db,$query) or die('Query error');
	// Recorrer el resultado
	while ($row = mysqli_fetch_array($result)) {
	echo $row['nombre'];
	echo '<br>';
	echo '<img src="' . $row[2] . '" alt="Imagen de la cancion">';
	echo '<br>';
	echo $row['3'];
	echo  '<br>';
	echo $row['4'];
	echo '<br>';
	echo "<a href='detail.php?cancion_id={$row['id']}'>Detalles</a>";
	echo "<hr>";
	}
	mysqli_close($db);
?>
</body>
</html>

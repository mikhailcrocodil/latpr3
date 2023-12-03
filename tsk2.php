<?php
if( isset( $_GET[ 'Login' ] ) ) {

	// CWE-20: Improper Input Validation. Требуется проверять username и password, например, с помощью isset ($_POST["username"], 	//["password"]), и использовать метод POST для предотвращения утечки пароле.

	$user = $_GET[ 'username' ];
	$pass = $_GET[ 'password' ];

	// CWE-328: Use of Weak Hash
	//Криптографический алгоритм md5 устарел и является слабым на сегодняшний день. Лучше заменить его на любой алгоритм семейства sha-2 или sha-3. (Пример: sha512)

	$pass = md5( $pass );

	// CWE-89 : Improper Neutralization of Special Elements used in an SQL Command ('SQL Injection'). Для предотвращения SQL-инъекций 	//рекомендуется использовать метод mysql_real_escape_string() или параметризированные запросы. Это позволит правильно 	//нейтрализовать специальные символы, которые могут быть использованы для выполнения вредоносного SQL-кода.

	// CWE-306: Missing Authentication for Critical Function
	//для обеспечения безопасности необходимо настроить запросы к базе данных таким образом, чтобы только пользователи с правами 	//чтения имели доступ к критическим функциям

	// CWE-307: Improper Restriction of Excessive Authentication Attempts
	// Необходимо установить ограничение на количество запросов

	$query  = "SELECT * FROM `users` WHERE user = '$user' AND password = '$pass';";
	$result = mysqli_query($GLOBALS["___mysqli_ston"],  $query ) or die( '<pre>' . ((is_object($GLOBALS["___mysqli_ston"])) ? mysqli_error($GLOBALS["___mysqli_ston"]) : (($___mysqli_res = mysqli_connect_error()) ? $___mysqli_res : false)) . '</pre>' );

	if( $result && mysqli_num_rows( $result ) == 1 ) {
		$row    = mysqli_fetch_assoc( $result );
		$avatar = $row["avatar"];
		$html .= "<p>Welcome to the password protected area {$user}</p>";
		$html .= "<img src=\"{$avatar}\" />";
	}
	else {
		$html .= "<pre><br />Username and/or password incorrect.</pre>";
	}
	((is_null($___mysqli_res = mysqli_close($GLOBALS["___mysqli_ston"]))) ? false : $___mysqli_res);
}
?>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $name = $_POST["name"];
  $email = $_POST["email"];
  $message = $_POST["message"];
  
  // Відправка повідомлення електронною поштою
  $to = "danaatatum@gmail.com"; // Замініть на свою електронну адресу
  $subject = "Нове повідомлення від $name";
  $body = "Ім'я: $name\nЕлектронна пошта: $email\n\nПовідомлення:\n$message";
  $headers = "From: $email";
  
  if (mail($to, $subject, $body, $headers)) {
    echo "Ваше повідомлення було успішно надіслане.";
  } else {
    echo "Сталася помилка при відправці повідомлення.";
  }
}
?>
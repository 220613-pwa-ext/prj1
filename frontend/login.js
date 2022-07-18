let usernameInput = document.getElementById('username');
let passwordInput = document.getElementById('password');
let loginSubmitButton = document.getElementById('login-submit-btn');


loginSubmitButton.addEventListener('click', async (e) => {
  console.log("usr,pass", usernameInput.value, passwordInput.value);
  e.preventDefault();
  let res = await fetch('http://127.0.0.1:8080/login', {
    'credentials': 'same-origin',
    'credentials': 'include',
    'method': 'POST',
    'headers': {
      'Content-Type': 'application/json'
    },
    'body': JSON.stringify({
      "username": usernameInput.value,
      "password": passwordInput.value
    })
  })
  if (res.status == 200) {
    window.location.href = '/reimb-view.html';

  } else if (res.status == 401) {
    let data = await res.json();
    console.log("message data", data.message);
    let loginErrorMessageDiv = document.getElementById('login-error-message')
    loginErrorMessageDiv.innerHTML = '';

    let errorElement = document.createElement('p');
    errorElement.innerHTML = data.message;
    errorElement.style.color = 'red';
    errorElement.style.fontWeight = 'bold';

    loginErrorMessageDiv.appendChild(errorElement);

  }
});

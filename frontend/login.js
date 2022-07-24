let usernameInput = document.getElementById('username');
let passwordInput = document.getElementById('password');
let loginSubmitButton = document.getElementById('login-submit-btn');
let loginErrorMessageDiv = document.getElementById('login-error-message')

loginSubmitButton.addEventListener('click', async (e) => {
  e.preventDefault();
  try {
    let res = await fetch('http://127.0.0.1:8080/login', {
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
      let errorElement = document.createElement('p');
      errorElement.innerHTML = data.message;
      errorElement.style.color = 'red';
      errorElement.style.fontWeight = 'bold';
      loginErrorMessageDiv.appendChild(errorElement);
    }
  } catch (err) {
    if (err.message == "Failed to fetch") {
      let errorElement = document.createElement('p');
      errorElement.innerHTML = "Server issue: contact IT Admin";
      errorElement.style.color = 'red';
      errorElement.style.fontWeight = 'bold';
      loginErrorMessageDiv.appendChild(errorElement);
    }
  }
});

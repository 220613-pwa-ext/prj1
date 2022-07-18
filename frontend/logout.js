
let logoutSuccess = document.getElementById('logout-message');


document.addEventListener("DOMContentLoaded", async () => {
  let res = await fetch('http://127.0.0.1:8080/logout', {
    'credentials': 'include',
    'method': 'POST',
    'headers': {
      'Content-Type': 'application/json'
    },
  })
  if (res.status == 200) {
    logoutSuccess.innerText = "You have successfully logged out. To access your data please: ";

  }
});

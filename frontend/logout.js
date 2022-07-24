
let logoutSuccess = document.getElementById('success-messages');


document.addEventListener("DOMContentLoaded", async () => {
  let res = await fetch('http://127.0.0.1:8080/logout', {
    'credentials': 'include',
    'method': 'POST',
    'headers': {
      'Content-Type': 'application/json'
    },
  })
  if (res.status == 200) {
    logoutSuccess.innerText += "Thank you for using the Employee Reimbursement Management System!";
    logoutSuccess.innerHTML += '<br><br><br>';
    logoutSuccess.innerText += "You have successfully logged out. ";
    logoutSuccess.innerHTML += '<br><br>';
    logoutSuccess.innerText += "To access your data again please login!";

  }
});

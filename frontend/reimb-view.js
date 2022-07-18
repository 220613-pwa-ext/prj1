// let usernameInput = document.getElementById('username');
// let passwordInput = document.getElementById('password');
let loginStatusButton = document.getElementById('login-status');
let greeting = document.getElementById('welcome');

document.addEventListener("DOMContentLoaded", async () => {
  try {
    let res = await fetch('http://127.0.0.1:8080/reimbursements', {
      'credentials': 'include',
      'method': 'GET',
      'headers': {
        'Content-Type': 'application/json'
      }
    })

    let data = await res.json();
    console.log(data)
    if (data) {
      greeting.innerText = "Welcome back, " + data.user + "!"
      loginStatusButton.innerText = "Logout"
      loginStatusButton.setAttribute('href', '/logout.html');
    }
    addReimbursementsToTable(data);
  } catch (err) {
    console.log(err);
  }

});

function addReimbursementsToTable(data) {
  let reimbursementTbodyElement = document.querySelector('#reimb-tbl');

  let row = document.createElement('tr');

  let idCell = document.createElement('td');
  idCell.innerHTML = data.reimbursements.r_id;
  let amountCell = document.createElement('td');
  nameCell.innerHTML = data.reimbursements.amount;
  let submittedCell = document.createElement('td');
  nameCell.innerHTML = data.reimbursements.submitted;
  let status_nameCell = document.createElement('td');
  nameCell.innerHTML = data.reimbursements.status_name;
  let r_nameCell = document.createElement('td');
  idCell.innerHTML = data.reimbursements.r_name;
  let descriptionCell = document.createElement('td');
  nameCell.innerHTML = data.reimbursements.description;
  let authorCell = document.createElement('td');
  nameCell.innerHTML = data.reimbursements.author;
  let imageCell = document.createElement('td');
  let imageElement = document.createElement('img');
  imageCell.appendChild(imageElement);
  imageElement.setAttribute('src', data.reimbursements.receipt);

  row.appendChild(idCell);
  row.appendChild(amountCell);
  row.appendChild(submittedCell);
  row.appendChild(status_nameCell);
  row.appendChild(r_nameCell);
  row.appendChild(descriptionCell);
  row.appendChild(imageCell);
  row.appendChild(authorCell);

  reimbursementTbodyElement.appendChild(row);
}

// function isLogedIn() {
//   const token = localStorage.getItem('token');
//   return token ? true : false
// };

// const logedIn = isLogedIn();
// if (logedIn) {
//   console.log('the user is logged in')
// }

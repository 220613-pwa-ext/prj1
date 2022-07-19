
let welcome = document.getElementById('welcome');
let loginStatusButton = document.getElementById('login-status');

document.addEventListener("DOMContentLoaded", async () => {
  try {
    let res = await fetch('http://127.0.0.1:8080/handle-reimbursements', {
      'credentials': 'same-origin',
      'credentials': 'include',
      'method': 'GET',
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Credentials': 'true'
      }
    })
    let data = await res.json();
    console.log("new data", data);
    loginStatusButton.innerText = "Logout"
    welcome.innerText = "Welcome back, " + data.user + "!"
    addReimbursementsToTable(data);
  } catch (err) {
    console.log(err);
  }
});

function addReimbursementsToTable(data) {

  let reimbursementTbodyElement = document.querySelector('#reimb-tbl');
  for (reimb of data.reimbursements) {
    let row = document.createElement('tr');

    let idCell = document.createElement('td');
    idCell.innerHTML = reimb.r_id;
    let amountCell = document.createElement('td');
    amountCell.innerHTML = reimb.amount;
    let submittedCell = document.createElement('td');
    submittedCell.innerHTML = reimb.submitted;
    let status_nameCell = document.createElement('td');
    status_nameCell.innerHTML = reimb.status_name;
    let r_nameCell = document.createElement('td');
    r_nameCell.innerHTML = reimb.r_name;
    let descriptionCell = document.createElement('td');
    descriptionCell.innerHTML = reimb.description;
    let authorCell = document.createElement('td');
    authorCell.innerHTML = reimb.author;
    let imageCell = document.createElement('td');
    let imageElement = document.createElement('img');
    imageCell.appendChild(imageElement);
    imageElement.setAttribute('src', reimb.receipt);

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
}

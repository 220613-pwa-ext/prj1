
let welcome = document.getElementById('welcome');
let loginStatusButton = document.getElementById('login-status');
let header3 = document.getElementById('header3');
let tbody = document.getElementById('reimb-tbl-tbody');

let filter = document.getElementById('filter');
let url = "http://127.0.0.1:8080/reimbursements"

document.addEventListener("DOMContentLoaded", async () => {
  try {
    let res = await fetch(url, {
      'credentials': 'same-origin',
      'credentials': 'include',
      'method': 'GET',
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Credentials': 'true'
      }
    })
    let data = await res.json();
    console.log(data);
    if (data.role == 1) {
      header3.removeAttribute('hidden');
    }

    welcome.innerText = "Welcome back, " + data.user + "!"
    addReimbursementsToTable(data);
  } catch (err) {
    if (err.message == "Failed to fetch") {
      welcome.innerHTML = "Server unreachable: contact IT Admin";
      welcome.style.color = 'red';
      welcome.style.fontWeight = 'bold';
    }
  }
});

filter.addEventListener('change', async (e) => {
  console.log(filter.value);

  while (tbody.hasChildNodes()) {
    tbody.removeChild(tbody.lastChild);
  }
  try {
    let res = await fetch(url + "?status=" + filter.value, {
      'credentials': 'same-origin',
      'credentials': 'include',
      'method': 'GET',
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Credentials': 'true'
      }
    })
    let data = await res.json();
    console.log(data);
    addReimbursementsToTable(data);
  } catch (err) {
    if (err.message == "Failed to fetch") {
      welcome.innerHTML = "Server unreachable: contact IT Admin";
      welcome.style.color = 'red';
      welcome.style.fontWeight = 'bold';
    }
  }
});


function addReimbursementsToTable(data) {
  console.log("datta passed to table", data)
  for (reimb of data.reimbursements) {
    let row = document.createElement('tr');

    let idCell = document.createElement('td');
    idCell.innerHTML = reimb.r_id;
    let amountCell = document.createElement('td');
    amountCell.innerHTML = reimb.amount;
    let submittedCell = document.createElement('td');
    submittedCell.innerHTML = reimb.submitted;
    let status_nameCell = document.createElement('td');

    if (reimb.status_name == "pending") {
      status_nameCell.innerHTML = reimb.status_name;
    } else if (reimb.status_name == "denied") {
      status_nameCell.innerHTML = reimb.status_name;
      status_nameCell.style.color = 'red';
    } else if (reimb.status_name == "approved") {
      status_nameCell.innerHTML = reimb.status_name;
      status_nameCell.style.color = 'green';
    }
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

    tbody.appendChild(row);
  }
}

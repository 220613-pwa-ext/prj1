
let welcome = document.getElementById('welcome');
let loginStatusButton = document.getElementById('login-status');
let header3 = document.getElementById('header3');
let header2 = document.getElementById('header2');
let newReimb = document.getElementById('new-reimb');
let tbody = document.getElementById('reimb-tbl-tbody');
let submitButton = document.getElementById('submit-btn');
let filter = document.getElementById('filter');
let error = document.getElementById('error-message');
let success = document.getElementById('success-messages');
let amount = document.getElementById('amount');
let description = document.getElementById('description');
let category = document.getElementById('category');
let receipt = document.getElementById('receipt');
let url = "http://127.0.0.1:8080/reimbursement"
let data = null;

const grabDataAndFeedtoPage = async () => {
  try {
    let res = await fetch(url + 's?status=' + filter.value, {
      'credentials': 'include',
      'method': 'GET',
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Credentials': 'true'
      }
    })
    data = await res.json();
    console.log(data);
    if (data.role == 1) {
      header3.removeAttribute('hidden');
    }
    welcome.innerText = "Welcome back, " + data.user + "!"
    addReimbursementsToTable(data);
  } catch (err) {
    if (err.message == "Failed to fetch") {
      welcome.innerText = "Server unreachable: contact IT Admin";
      welcome.style.color = 'red';
      welcome.style.fontWeight = 'bold';
    }
    else {
      console.log(err)
    }
  }
};

document.addEventListener("DOMContentLoaded", grabDataAndFeedtoPage);

header2.addEventListener('click', () => {
  newReimb.removeAttribute('hidden');
})

submitButton.addEventListener('click', async (e) => {

  if (!amount.value || !description.value || category.value == 4) {
    error.innerText = "All fields must contain data";
    error.style.color = 'red';
    error.style.fontWeight = 'bold';
  } else {
    error.innerText = '';
    const formData = new FormData();
    const image = new Blob([JSON.stringify({
      receipt: receipt.value,
    })], {
      type: 'image/jpeg'
    });
    formData.append("receipt", receipt.files[0])
    formData.append("description", description.value)
    formData.append("amount", amount.value)
    formData.append("type_id", category.value)
    console.log(...formData)
    try {
      let res = await fetch(url, {
        'credentials': 'same-origin',
        'credentials': 'include',
        'method': 'POST',
        'body': formData
      })
      console.log(res);
      while (tbody.hasChildNodes()) {
        tbody.removeChild(tbody.lastChild);
      }
      data = await res.json();
      addReimbursementsToTable(data);
      newReimb.setAttribute('hidden', true);
      if (res.status == 201) {

        console.log(data);
        success.removeAttribute('hidden');
        success.innerText = data.message;
        setTimeout(() => {
          success.setAttribute('hidden', true);
        }, 5000)
      }
    } catch (err) {
      if (err.message == "Failed to fetch") {
        welcome.innerText = "Server unreachable: contact IT Admin";
        welcome.style.color = 'red';
        welcome.style.fontWeight = 'bold';
      }
    }
  }
})

filter.addEventListener('change', async (e) => {

  while (tbody.hasChildNodes()) {
    tbody.removeChild(tbody.lastChild);
  }
  try {
    let res = await fetch(url + "s?status=" + filter.value, {
      'credentials': 'same-origin',
      'credentials': 'include',
      'method': 'GET',
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Credentials': 'true'
      }
    })
    data = await res.json();
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
    let aElement = document.createElement('a');
    aElement.setAttribute('href', reimb.receipt);
    aElement.innerText = 'view receipt'
    imageCell.appendChild(aElement);

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

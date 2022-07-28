
let welcome = document.getElementById('welcome');
let loginStatusButton = document.getElementById('login-status');
let tbody = document.getElementById('reimb-tbl-tbody');
let filter = document.getElementById('filter');
let success = document.getElementById('success-messages');
let url = "http://127.0.0.1:8080/handle-reimbursements"


const grabDataAndFeedtoPage = async (data) => {
  try {
    let res = await fetch(url, {
      'credentials': 'include',
      'method': 'GET',
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Credentials': 'true'
      }
    })
    if (res.status == 200) {
      data = await res.json();
      if (data.role == 1) {
        header3.removeAttribute('hidden');
      }
      welcome.innerText = "Welcome back, " + data.user + "!"
      addReimbursementsToTable(data);
    }
    if (res.status == 401) {
      window.location.href = '/index.html';
    }
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

window.addEventListener('popstate', grabDataAndFeedtoPage);

document.addEventListener("DOMContentLoaded", grabDataAndFeedtoPage);

loginStatusButton.addEventListener('click', async () => {
  let res = await fetch('http://127.0.0.1:8080/logout', {
    'credentials': 'include',
    'method': 'POST',
    'headers': {
      'Content-Type': 'application/json'
    },
  })
  if (res.status == 200) {
    success.removeAttribute('hidden');
    success.innerText += "Thank you for using the Employee Reimbursement Management System!";
    success.innerHTML += '<br><br>'
    success.innerText += "Logging you out ";
    success.innerHTML += '<br><br>'
    for (let i = 0; i < 1500; i += 200) {
      setTimeout(() => { success.innerText += "."; }, i)
    }

    setTimeout(() => { window.location.href = '/index.html'; }, 2000)


  }
})


filter.addEventListener('change', async (e) => {

  while (tbody.hasChildNodes()) {
    tbody.removeChild(tbody.lastChild);
  }
  try {
    let res = await fetch(url + '?status=' + filter.value, {
      'credentials': 'include',
      'method': 'GET',
      'headers': {
        'Content-Type': 'application/json'
      }
    })
    let data = await res.json();
    addReimbursementsToTable(data);
  } catch (err) {
    if (err.message == "Failed to fetch") {
      welcome.innerHTML = "Server unreachable: contact IT Admin";
      welcome.style.color = 'red';
      welcome.style.fontWeight = 'bold';
    }
  }

});

document.addEventListener('click', (e) => {
  e.stopPropagation();
  e.target.addEventListener('change', async (e) => {
    if (String(e.target.innerHTML).includes('class="my-class dropdown-item"')) {
      console.log(e.target.value)
      while (tbody.hasChildNodes()) {
        tbody.removeChild(tbody.lastChild);
      }
      try {
        let res = await fetch("http://127.0.0.1:8080/handle-reimbursements/" + e.target.value, {
          'credentials': 'include',
          'method': 'PUT',
          'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Credentials': 'true'
          }
        })
        let data = await res.json();

        welcome.innerText = "Welcome back, " + data.user + "!"
        addReimbursementsToTable(data);
      } catch (err) {
        if (err.message == "Failed to fetch") {
          welcome.innerHTML = "Server unreachable: contact IT Admin";
          welcome.style.color = 'red';
          welcome.style.fontWeight = 'bold';
        }
      }
    }
  })
})



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
      status_nameCell.innerHTML = '<select name="status-in-row" class="filter-in-row"> <option class="my-class dropdown-item" value=1' +
        '>Pending</option> <option class="my-class dropdown-item" value="2' + reimb.r_id + '">Approved</option>' +
        '<option class="my-class dropdown-item" value="3' + reimb.r_id + '">Denied</option> </select>';
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
    let imageElement = document.createElement('a');
    imageCell.appendChild(imageElement);
    imageElement.setAttribute('href', reimb.receipt);
    imageElement.setAttribute('target', '_Blank');
    imageElement.innerText = 'view receipt';

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

// Handle login
document.getElementById('loginForm').addEventListener('submit', function (e) {
  e.preventDefault();
  document.querySelector('.login-container').style.display = 'none';
  document.querySelector('.dashboard').style.display = 'block';
});

// Delete confirmation popup logic
let rowToDelete = null;

document.addEventListener('DOMContentLoaded', function () {
  const tableBody = document.querySelector('.table-section table tbody');
  const deletePopup = document.getElementById('deletePopup');
  const confirmDelete = document.getElementById('confirmDelete');
  const cancelDelete = document.getElementById('cancelDelete');

  tableBody.addEventListener('click', function (e) {
    if (e.target.closest('.delete-btn')) {
      rowToDelete = e.target.closest('tr');
      deletePopup.style.display = 'flex';
    }
  });

  confirmDelete.addEventListener('click', function () {
    if (rowToDelete) {
      rowToDelete.remove();
      rowToDelete = null;
    }
    deletePopup.style.display = 'none';
  });

  cancelDelete.addEventListener('click', function () {
    deletePopup.style.display = 'none';
    rowToDelete = null;
  });
});
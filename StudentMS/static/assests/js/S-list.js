
    // Search functionality
    document.getElementById('searchInput').addEventListener('input', function() {
      const searchValue = this.value.toLowerCase();
      const rows = document.querySelectorAll('#studentTable tbody tr');
      
      rows.forEach(row => {
        const name = row.cells[1].textContent.toLowerCase();
        const rollNo = row.cells[2].textContent.toLowerCase();
        const program = row.cells[3].textContent.toLowerCase();
        
        if (name.includes(searchValue) || rollNo.includes(searchValue) || program.includes(searchValue)) {
          row.style.display = '';
        } else {
          row.style.display = 'none';
        }
      });
    });

    // Filter functionality
    document.getElementById('programFilter').addEventListener('change', function() {
      const filterValue = this.value;
      const rows = document.querySelectorAll('#studentTable tbody tr');
      
      rows.forEach(row => {
        const program = row.cells[3].textContent;
        
        if (filterValue === '' || program === filterValue) {
          row.style.display = '';
        } else {
          row.style.display = 'none';
        }
      });
    });

    // Delete confirmation with sweet animation
    function confirmDelete(event) {
      event.preventDefault();
      
      const row = event.target.closest('tr');
      row.style.transition = 'all 0.3s ease';
      row.style.backgroundColor = 'rgba(247, 37, 133, 0.1)';
      
      if (confirm('Are you sure you want to delete this student record?')) {
        row.style.transform = 'translateX(100%)';
        row.style.opacity = '0';
        
        setTimeout(() => {
          row.remove();
          // In a real app, you would make an AJAX call to delete from database
          showNotification('Student record deleted successfully!', 'success');
        }, 300);
      } else {
        row.style.backgroundColor = '';
      }
    }

    // Notification function
    function showNotification(message, type) {
      const notification = document.createElement('div');
      notification.className = `notification ${type}`;
      notification.textContent = message;
      document.body.appendChild(notification);
      
      setTimeout(() => {
        notification.classList.add('show');
      }, 10);
      
      setTimeout(() => {
        notification.classList.remove('show');
        setTimeout(() => {
          notification.remove();
        }, 300);
      }, 3000);
    }

    // Add some sample animations when page loads
    document.addEventListener('DOMContentLoaded', () => {
      const rows = document.querySelectorAll('#studentTable tbody tr');
      rows.forEach((row, index) => {
        row.style.opacity = '0';
        row.style.transform = 'translateY(20px)';
        row.style.transition = `all 0.3s ease ${index * 0.1}s`;
        
        setTimeout(() => {
          row.style.opacity = '1';
          row.style.transform = 'translateY(0)';
        }, 100);
      });
    });
 